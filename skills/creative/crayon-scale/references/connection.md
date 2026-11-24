# Crayon connection and API use

Prefer a suitable exposed Crayon connector. Read its overview and current schemas. The namespace alone is not product identity. An overview describing native walls, rooms and centimetres belongs to Chalk.

On Osiris's Mac, `~/.config/osiris-agent-vault/crayon-mcp.json` is the non-secret registration naming the Crayon endpoint and Keychain header helper. The bundled `scripts/crayon_mcp.py` uses it, keeps credentials and session headers in memory and never retries requests automatically. It does not alter harness configuration. On another host, discover that host's registered connection rather than copying credentials.

Commands are relative to this skill directory:

```bash
python3 scripts/crayon_mcp.py tools
python3 scripts/crayon_mcp.py call high_level_overview
python3 scripts/crayon_mcp.py call list_sessions
python3 scripts/crayon_mcp.py call crayon_api_info --args '{"type":"Crayon"}'
python3 scripts/crayon_mcp.py code /absolute/path/to/inspect-design.js
```

Use `--args-file /absolute/path/args.json` for complex arguments. `code` reads JavaScript from a file to avoid shell expansion. Pass `--session-id` after `call` or `code` for multiple sessions. `tools` returns current names, descriptions and schemas. Inspect only relevant entries.

For image responses supply `--output-dir /absolute/path/to/evidence`. The helper writes image blocks and prints paths for visual inspection. Without that option it prints image metadata, never base64. It leaves remote links remote rather than downloading them to bypass presentation restrictions.

The registered endpoint was verified as the UI design server during skill creation. Availability and editor connections can change. With no suitable session, open the intended Crayon file and enable its MCP connection. Keep the in-app Browser visible. Verify workspace and file before editing.

## API details

- `execute_code` runs with `crayon`, `crayonUtils` and persistent `storage`. Use documented utilities for search/structure. Objects in `storage` belong to the current editor session.
- Shape dimensions use `resize`; parent-relative coordinates are computed properties. Flex/grid controls child positions. Query docs for creation, prototypes, tokens and components.
- Text resizing differs from font size. Check rendered `textBounds` after layout settles. Replace entire fills/strokes arrays when changing them.
- Use `export_shape` for visual inspection, then the documented `wait_for_save` for the active file after edits settle. Exports and save-status reads alone do not establish persistence.
- Tool errors return nonzero exit status. A transport failure can happen after a mutation commits. Inspect actual state/receipt before recovery instead of resending automatically.
- Repair authentication through the registered account route. Keep headers, keys and transport sessions out of logs, screenshots and project records.
