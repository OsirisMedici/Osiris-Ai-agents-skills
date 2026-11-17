# Connect another account

## Reuse before creating

Inspect the existing registered connection and identify its authenticated user, app, accessible business and selected ad account. Confirm account name and numeric ID, MCP eligibility/queryability and currency through available account reads. Active account status does not prove that an ad is delivering.

Use the current Meta connection flow in the in-app Browser. Prefer the host's supported OAuth route when it works. Use Meta's bearer-token route when OAuth cannot complete and that route is supported by the current official flow. Avoid substituting an unrelated connector or paid intermediary when the user chose Meta's official server.

Inspect permissions before approval. `ads_read` supplies ads read access; `ads_mcp_management` enables MCP access in the validated bearer route. Meta's advertised scope list includes write permissions too. The advertised list is not proof that every scope is required. Request the smallest supported grant for the job and verify the granted scopes. Do not describe a broad OAuth grant as technically read-only because instructions say to avoid writes.

App creation, accepting platform terms, granting access and extending credential duration need the applicable user approval. Reuse valid authorization already supplied for that exact action. The user handles passwords, MFA, CAPTCHA and recovery directly in the official UI. Keep credentials out of chat, screenshots, exports, command arguments and Git. On token/debugger screens avoid automatic full-page snapshots; use a safe observation or hand off to the user.

## Local registry

Create a separate record for each client, starting from this fictional example. Replace every identity with the selected account's verified values. No credential belongs in this JSON.

```json
{
  "version": 1,
  "provider": "Meta official Ads MCP",
  "endpoint": "https://mcp.facebook.com/ads",
  "approved_ad_account_id": "900000000001",
  "approved_ad_account_name": "Example Training Ads",
  "app_id": "900000000002",
  "keychain_service": "com.example.meta-ads.training-readonly",
  "keychain_account": "900000000002:900000000001",
  "scopes": ["ads_mcp_management", "ads_read"],
  "account_scope_enforced_by_credential": false,
  "write_helper": null
}
```

Store an approved bearer credential in macOS Keychain using an existing secure enrollment route or the user's direct Keychain entry. The bundled helper only reads an existing generic-password entry. It cannot enroll or renew a credential. Record the actual expiry, granted scopes and renewal route in the local registry. An approximately 60-day extension was available in the observed Meta flow; inspect the current expiry and available action instead of promising a fixed duration or automatic renewal.

## Use the bundled reader

Run from the installed skill directory, with paths to the selected client's registry and task-local arguments:

```bash
python3 scripts/meta_ads_read.py --registry /absolute/private/meta-ads-example.json list-tools > /absolute/task/work/meta-tools.json
python3 scripts/meta_ads_read.py --registry /absolute/private/meta-ads-example.json call ads_get_ad_entities --args /absolute/task/work/query.json > /absolute/task/work/result.json
```

The `headers` command exists solely for a host's supported credential-header helper. It prints an Authorization header containing the secret. Never execute it in a logged agent tool call, copy its output, or place its output in a config file. Configure a host to execute it privately only after checking that host's current header-helper support and preserving unrelated configuration. Restrict exposed native tools to the reader's nine read tools. Native calls still need explicit account scoping; the token may cover several accounts.

Verify a real campaign read after setup. An MCP entry can be saved before its tools become available to the current chat. Use the direct official reader for verification when appropriate; do not restart unrelated work merely to refresh tools. Report the distinction between saved configuration, live direct access and native tool availability.

## Recover without widening access

On authentication failure, inspect expiry, app identity, granted scopes and account role. A business portfolio's app-claim restriction does not by itself prove the selected ad account is unusable. Verify the actual account read.

For an OAuth callback failure, inspect the exact callback, DNS and current official route. Preserve browser security blocks. Do not switch to the user's personal Chrome, bypass an interstitial or expose a callback publicly. Remove only task-created temporary listeners/routes when no longer needed, preserving existing service configuration. If the supported route remains blocked, state the failed step and required user action.

Primary metadata checked on 2026-10-28: [Meta's protected-resource metadata](https://mcp.facebook.com/.well-known/oauth-protected-resource/ads). It identifies the official resource, authorization server, supported scopes and header bearer method. Tool availability and authentication UI can change; discover the current schemas and flow.
