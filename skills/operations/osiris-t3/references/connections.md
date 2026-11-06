# Connect to the right machine

## T3 Connect

Use the same T3 Connect account for host registration and the browser client. Its identity is independent of the paid Claude account; discover or confirm the existing T3 identity rather than assuming the addresses must match.

On a verified CLI, `t3 connect status --json` reports setup. Discover the active executable from runtime state: an old service launcher path does not establish the running version. Check `--help` for the installed host. Some builds offer `t3 connect link --headless` or `t3 up`. Setup can require the managed cloudflared relay client, user device approval and a controlled server restart. Prepare everything before arranging a restart; preserve active agents.

Teach the user: open https://app.t3.codes, sign into the same T3 Connect account, choose the VPS and continue an existing thread. A missing environment is a host/link/reachability problem, not a reason to create a second workspace. The Mac may sleep for VPS work. Accessing local Writer remotely requires the Mac to be awake, online and itself reachable.

The hosted app.t3.codes client is the official client. Unmerged fork changes in desktop or web UI are not automatically included. Where the custom web UI is required, verify a supported private endpoint serving the fork's bundled web client and distinguish it from the official hosted client.

T3 client connections and agent-to-agent peer links are different. Do not create broad peer grants solely to teach browser access.

## Claude subscription

Resolve the intended paid Claude account from the authorized setup record or ask the user to identify it. Verify the CLI binary, provider instance, and configuration directory on the target host. Service PATH may differ from the interactive shell.

Run `claude auth status` with the configured executable and directory. Use `claude auth login --claudeai` with the intended identity if the user authorized login and the installed CLI supports it. Each machine authenticates locally. Keep OAuth files, cookies and keychains on the host that created them. Use subscription mode for the paid plan. The CLI's `--console` flow uses separate API billing.

Use the native flow or T3's supported provider authentication interface. Have the user approve the correct account themselves if authorization requires a browser. A remote flow may require a callback route or a code in the remote terminal; inspect the actual prompt before giving instructions. Keep codes out of chat and logs.

After login, verify the CLI reports the expected email and loggedIn true. Refresh that provider in T3 and verify authenticated/ready. A minimal successful Claude turn proves runtime use; CLI status alone proves only login. Avoid changing the current conversation's provider or creating paid test turns without considering existing authorization and shared usage.

The bundled Bun helper queries the provider snapshot through T3 RPC with a five-minute scoped session and revokes that session afterward. Run `bun <skill>/scripts/provider.ts mac status` on the Mac or `bun <skill>/scripts/provider.ts vps status` on the VPS. For a VPS check from the Mac, set `T3_SSH_HOST` to the verified SSH host. The helper targets the `claudeAgent` instance and assumes T3 is listening on loopback port 3773.

The `configure` action writes provider settings. Use it only for an authorized setup, and set `T3_CLAUDE_BIN` to the absolute Claude CLI path on the target machine.
