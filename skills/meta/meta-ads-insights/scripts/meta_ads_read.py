#!/usr/bin/env python3
"""Read-only client for Meta's official MCP. Credentials stay in Keychain/memory."""
import argparse
import json
import re
import secrets
import string
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

ENDPOINT = 'https://mcp.facebook.com/ads'
READ_TOOLS = frozenset({
    'ads_get_ad_accounts', 'ads_get_field_context', 'ads_get_ad_entities',
    'ads_get_creatives', 'ads_get_creative_ads', 'ads_get_ad_images',
    'ads_get_ad_videos', 'ads_get_ad_preview', 'ads_insights_performance_trend',
})
ACCOUNT_TOOLS = READ_TOOLS - {
    'ads_get_ad_accounts', 'ads_get_field_context',
    'ads_get_creative_ads', 'ads_get_ad_preview',
}
SECRET_KEYS = {'access_token', 'app_secret', 'authorization', 'token', 'password'}


def load_registry(path):
    registry = json.loads(Path(path).expanduser().read_text())
    if not isinstance(registry, dict):
        raise ValueError('Registry must be a JSON object.')
    def inspect(value):
        if isinstance(value, dict):
            if SECRET_KEYS.intersection(str(k).lower() for k in value):
                raise ValueError('Registry must contain references, never credentials.')
            for item in value.values():
                inspect(item)
        elif isinstance(value, list):
            for item in value:
                inspect(item)
    inspect(registry)
    if registry.get('endpoint', ENDPOINT) != ENDPOINT:
        raise ValueError('Only the official Meta Ads MCP endpoint is supported.')
    account = str(registry.get('approved_ad_account_id', ''))
    if not re.fullmatch(r'[0-9]+', account):
        raise ValueError('Registry needs a numeric approved_ad_account_id.')
    registry['approved_ad_account_id'] = account
    for key in ('keychain_service', 'keychain_account'):
        if not isinstance(registry.get(key), str) or not registry[key].strip():
            raise ValueError('Registry needs ' + key + '.')
    return registry


def keychain_token(registry):
    try:
        result = subprocess.run(
            ['/usr/bin/security', 'find-generic-password', '-s', registry['keychain_service'],
             '-a', registry['keychain_account'], '-w'],
            check=True, capture_output=True, text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        raise ValueError('The registered Keychain credential is unavailable.') from None
    token = result.stdout.strip()
    if not token or '\n' in token or '\r' in token:
        raise ValueError('The Keychain credential is empty or invalid.')
    return token


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def structured(result):
    if result.get('isError'):
        raise ValueError('Meta read failed; inspect the scoped tool error.')
    if isinstance(result.get('structuredContent'), dict):
        return result['structuredContent']
    for block in result.get('content', []):
        if block.get('type') == 'text':
            try:
                value = json.loads(block['text'])
                if isinstance(value, dict):
                    return value
            except (ValueError, KeyError):
                pass
    return {}


def rows(result, field):
    value = structured(result).get(field, [])
    if isinstance(value, str):
        value = json.loads(value)
    return value if isinstance(value, list) else []


class MetaReader:
    def __init__(self, registry, token):
        self.registry = registry
        self.token = token
        self.headers = {'Authorization': 'Bearer ' + token,
                        'Content-Type': 'application/json',
                        'Accept': 'application/json, text/event-stream'}
        self.opener = urllib.request.build_opener(NoRedirect)
        self.sequence = 0

    def redact(self, value):
        return json.dumps(value, ensure_ascii=False, indent=2).replace(self.token, '<REDACTED>')

    def rpc(self, method, params=None, notification=False):
        self.sequence += 1
        request_id = self.sequence
        body = {'jsonrpc': '2.0', 'method': method}
        if not notification:
            body['id'] = request_id
        if params is not None:
            body['params'] = params
        request = urllib.request.Request(ENDPOINT, data=json.dumps(body).encode(),
                                         headers=self.headers, method='POST')
        try:
            with self.opener.open(request, timeout=90) as response:
                session = response.headers.get('Mcp-Session-Id')
                if session:
                    self.headers['Mcp-Session-Id'] = session
                raw = response.read().decode()
        except urllib.error.HTTPError as error:
            # Omit raw response and URL: a remote diagnostic can contain credentials.
            raise ValueError('Meta HTTP ' + str(error.code) + '; no redirect followed.') from None
        except (OSError, urllib.error.URLError):
            raise ValueError('Meta transport failed; no credential details logged.') from None
        if not raw.strip():
            return {}
        if raw.lstrip().startswith('{'):
            payload = json.loads(raw)
        else:
            payload = None
            for line in raw.splitlines():
                if line.startswith('data:'):
                    candidate = json.loads(line[5:].strip())
                    if candidate.get('id') == request_id:
                        payload = candidate
                        break
            if payload is None:
                raise ValueError('Meta returned no matching JSON-RPC result.')
        if 'error' in payload:
            raise ValueError('Meta JSON-RPC request failed; no credential details logged.')
        return payload.get('result', {})

    def initialize(self):
        hello = self.rpc('initialize', {
            'protocolVersion': '2025-03-26', 'capabilities': {},
            'clientInfo': {'name': 'meta-ads-insights-readonly', 'version': '1'},
        })
        self.headers['MCP-Protocol-Version'] = hello.get('protocolVersion', '2025-03-26')
        self.rpc('notifications/initialized', notification=True)

    def arguments(self, name, params):
        if name not in READ_TOOLS:
            raise ValueError('Write or unknown tools are blocked.')
        if not isinstance(params, dict):
            raise ValueError('Tool arguments must be a JSON object.')
        args = dict(params)
        account = self.registry['approved_ad_account_id']
        for key in ('ad_account_id', 'account_id', 'adaccount_id'):
            if key in args and str(args[key]).removeprefix('act_') != account:
                raise ValueError('Account is outside the selected registry scope.')
        if name in ACCOUNT_TOOLS:
            args['ad_account_id'] = account
        if not args.get('client_conversation_id'):
            args['client_conversation_id'] = ''.join(
                secrets.choice(string.ascii_letters + string.digits) for _ in range(20))
        if not re.fullmatch(r'[A-Za-z0-9]{20}', args['client_conversation_id']):
            raise ValueError('Conversation ID must contain 20 alphanumeric characters.')
        args.setdefault('scheduled_task_run', False)
        return args

    def raw_call(self, name, args):
        return self.rpc('tools/call', {'name': name, 'arguments': args})

    def verify_object(self, kind, object_id, args):
        if not re.fullmatch(r'[0-9]+', str(object_id)):
            raise ValueError('A numeric ' + kind + ' ID is required.')
        account = self.registry['approved_ad_account_id']
        context = {key: args[key] for key in (
            'advertiser_request', 'advertiser_job', 'client_conversation_id', 'scheduled_task_run'
        ) if key in args}
        context['ad_account_id'] = account
        if kind == 'ad':
            result = self.raw_call('ads_get_ad_entities', dict(
                context, level='ad', object_ids=[str(object_id)], fields=['id', 'name'],
                reporting_purpose=['entity_lookup']))
            found = rows(result, 'ad_entities')
            valid = any(str(row.get('id')) == str(object_id) for row in found)
        else:
            result = self.raw_call('ads_get_creatives', dict(
                context, creative_ids=[str(object_id)], fields=['id', 'account_id']))
            found = rows(result, 'ad_creatives')
            valid = any(str(row.get('id')) == str(object_id)
                        and str(row.get('account_id')) == account for row in found)
        if not valid:
            raise ValueError('Object ownership could not be verified in the selected account.')

    def call(self, name, params):
        args = self.arguments(name, params)
        if name == 'ads_get_ad_preview':
            if bool(args.get('ad_id')) == bool(args.get('creative_id')):
                raise ValueError('Provide exactly one ad_id or creative_id.')
            kind = 'ad' if args.get('ad_id') else 'creative'
            self.verify_object(kind, args[kind + '_id'], args)
        elif name == 'ads_get_creative_ads':
            self.verify_object('creative', args.get('creative_id'), args)
        return self.raw_call(name, args)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--registry', required=True)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('list-tools')
    sub.add_parser('headers', help='Secret output; only for a private host header-helper channel')
    call = sub.add_parser('call')
    call.add_argument('tool')
    call.add_argument('--args', required=True)
    options = parser.parse_args()
    try:
        registry = load_registry(options.registry)
        # Validate tool and account before reading any credential or opening a connection.
        params = None
        if options.command == 'call':
            params = json.loads(Path(options.args).read_text())
            MetaReader(registry, '').arguments(options.tool, params)
        token = keychain_token(registry)
        if options.command == 'headers':
            print(json.dumps({'Authorization': 'Bearer ' + token}))
            return 0
        reader = MetaReader(registry, token)
        reader.initialize()
        result = reader.rpc('tools/list', {}) if options.command == 'list-tools' else reader.call(options.tool, params)
        print(reader.redact(result))
        return 1 if result.get('isError') else 0
    except (ValueError, OSError, TypeError, KeyError):
        # Known errors contain no remote bodies or credential values.
        print('Meta read could not complete. Check the registry, tool arguments, account scope, credential and provider availability.', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
