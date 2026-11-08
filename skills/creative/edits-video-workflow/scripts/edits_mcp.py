#!/usr/bin/env python3
"""Call the local Instagram Edits Automation Server without exposing its token."""
import argparse
import base64
import json
import os
import re
import shlex
import subprocess
import urllib.error
import urllib.request
from pathlib import Path

READ_TOOLS = {
    "appState", "getCapabilities", "projects", "elements", "tracks", "mediaBin",
    "mediaStatus", "getElement", "getTransform", "getTransformKeyframes",
    "getMediaPanelItems", "captions", "captureFrame", "exportStatus",
    "projectDynamicRange", "listTextPresets", "listCaptionStyles",
}


def token_from_clipboard(endpoint, variable):
    snippet = subprocess.run(["pbpaste"], capture_output=True, text=True, check=True).stdout
    try:
        declaration, registration = [shlex.split(line) for line in snippet.strip().splitlines()]
        env_flag = registration.index("--bearer-token-env-var")
        if (len(declaration) != 2 or declaration[0] != "export"
                or not declaration[1].startswith(variable + "=")
                or registration[:3] != ["codex", "mcp", "add"]
                or endpoint not in registration or registration[env_flag + 1] != variable):
            raise ValueError
        return declaration[1].split("=", 1)[1]
    except (IndexError, ValueError):
        raise ValueError("Copy Edits' Codex setup snippet from Settings → Automation") from None


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


class Edits:
    def __init__(self, port, token):
        self.url = f"http://127.0.0.1:{port}/mcp"
        self.token = token
        self.opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
        self.headers = {
            "Authorization": "Bearer " + token,
            "Content-Type": "application/json",
            "Accept": "application/json, text/event-stream",
        }
        self.number = 0
        initialized = self.rpc("initialize", {
            "protocolVersion": "2025-03-26",
            "capabilities": {},
            "clientInfo": {"name": "edits-video-workflow", "version": "1.0"},
        })
        self.headers["MCP-Protocol-Version"] = initialized["protocolVersion"]
        self.rpc("notifications/initialized", notification=True)

    def rpc(self, method, params=None, *, notification=False):
        payload = {"jsonrpc": "2.0", "method": method}
        if params is not None:
            payload["params"] = params
        if not notification:
            self.number += 1
            payload["id"] = self.number
        request = urllib.request.Request(
            self.url, data=json.dumps(payload).encode(), headers=self.headers,
        )
        try:
            with self.opener.open(request, timeout=30) as response:
                session = response.headers.get("Mcp-Session-Id")
                if session:
                    self.headers["Mcp-Session-Id"] = session
                if notification:
                    return None
                if response.headers.get_content_type() == "text/event-stream":
                    for line in response:
                        if line.startswith(b"data: "):
                            message = json.loads(line[6:])
                            if message.get("id") == payload["id"]:
                                break
                    else:
                        raise RuntimeError("Edits returned no matching SSE response")
                else:
                    message = json.load(response)
        except urllib.error.HTTPError as error:
            raise RuntimeError(f"Edits returned HTTP {error.code} for {method}") from None
        if "error" in message:
            safe_error = str(message["error"]).replace(self.token, "[redacted]")
            raise RuntimeError(safe_error)
        return message["result"]

    def tools(self):
        cursor = None
        seen = set()
        while True:
            result = self.rpc("tools/list", {"cursor": cursor} if cursor else {})
            yield from result["tools"]
            cursor = result.get("nextCursor")
            if not cursor:
                return
            if cursor in seen:
                raise RuntimeError("Edits repeated a tool catalog cursor")
            seen.add(cursor)


def call(client, options):
    params = json.loads(options.args)
    if not isinstance(params, dict):
        raise ValueError("--args must contain a JSON object")
    result = client.rpc("tools/call", {"name": options.tool, "arguments": params})
    values = []
    for block in result.get("content", []):
        if block["type"] == "text":
            safe_text = block["text"].replace(client.token, "[redacted]")
            try:
                values.append(json.loads(safe_text))
            except ValueError:
                values.append(safe_text)
        elif block["type"] == "image" and options.image_output:
            with options.image_output.open("xb") as output:
                output.write(base64.b64decode(block["data"], validate=True))
    print(json.dumps(values[0] if len(values) == 1 else values, ensure_ascii=False, indent=2))
    return int(bool(result.get("isError")))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=19501)
    parser.add_argument("--token-env", default="METAPILOT_TOKEN")
    parser.add_argument("--clipboard", action="store_true")
    actions = parser.add_subparsers(dest="action", required=True)
    catalog = actions.add_parser("tools")
    catalog.add_argument("--match", default=".", help="Regex to filter tool names")
    tool = actions.add_parser("call")
    tool.add_argument("tool")
    tool.add_argument("--args", default="{}")
    tool.add_argument("--write", action="store_true")
    tool.add_argument("--image-output", type=Path, help="Save one returned frame to a new path")
    options = parser.parse_args()
    if not 1 <= options.port <= 65535:
        parser.error("Port must be between 1 and 65535")
    if options.action == "call" and options.tool not in READ_TOOLS and not options.write:
        parser.error("This call needs an explicit --write flag")
    try:
        token = (
            token_from_clipboard(f"http://127.0.0.1:{options.port}/mcp", options.token_env)
            if options.clipboard else os.environ.get(options.token_env)
        )
        if not token or not re.fullmatch(r"[^\s\x00-\x1f\x7f]+", token):
            raise ValueError("No valid Edits bearer token in the chosen source")
        client = Edits(options.port, token)
        if options.action == "tools":
            query = re.compile(options.match, re.IGNORECASE)
            print(json.dumps([t for t in client.tools() if query.search(t["name"])], indent=2))
            return 0
        return call(client, options)
    except (ValueError, OSError, RuntimeError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    raise SystemExit(main())
