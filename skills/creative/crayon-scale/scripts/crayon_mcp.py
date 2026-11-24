#!/usr/bin/env python3
"""Call registered Crayon MCP without persisting credentials or retrying."""

import argparse
import base64
import json
from pathlib import Path
import subprocess
import sys
import urllib.error
import urllib.request
import uuid


class CrayonMCP:
    def __init__(self, registry):
        registration = json.loads(Path(registry).expanduser().read_text())
        self.url = registration["serverUrl"]
        if not self.url.startswith("https://"):
            raise RuntimeError("Registered MCP endpoint must use HTTPS.")
        helper = subprocess.run([registration["readHeadersHelper"]],
                                capture_output=True, text=True)
        if helper.returncode:
            raise RuntimeError("Registered Keychain header helper failed.")
        self.headers = json.loads(helper.stdout)
        self.headers.update({"Content-Type": "application/json",
                             "Accept": "application/json, text/event-stream"})
        self.counter = 0
        self.request("initialize", {
            "protocolVersion": "2024-11-05", "capabilities": {},
            "clientInfo": {"name": "crayon-scale", "version": "1.0"}})
        self.request("notifications/initialized")

    def request(self, method, params=None):
        self.counter += 1
        payload = {"jsonrpc": "2.0", "method": method}
        if not method.startswith("notifications/"):
            payload["id"] = self.counter
        if params is not None:
            payload["params"] = params
        request = urllib.request.Request(self.url, json.dumps(payload).encode(), self.headers)
        # No replay after an uncertain mutation outcome.
        with urllib.request.urlopen(request, timeout=55) as response:
            session = response.headers.get("Mcp-Session-Id")
            if session:
                self.headers["Mcp-Session-Id"] = session
            content_type = response.headers.get("Content-Type", "")
            body = response.read().decode()
        if not body.strip():
            return {}
        if "text/event-stream" in content_type or body.lstrip().startswith(("event:", "data:", ":")):
            messages = []
            for event in body.replace("\r\n", "\n").split("\n\n"):
                data = "\n".join(line[5:].lstrip() for line in event.splitlines()
                                 if line.startswith("data:"))
                if data:
                    messages.append(json.loads(data))
            result = next((item for item in messages
                           if item.get("id") == payload.get("id")), None)
            if result is None:
                raise RuntimeError("No matching MCP response. Inspect state before retrying.")
        else:
            result = json.loads(body)
        if "error" in result:
            raise RuntimeError("MCP protocol error, code " + str(result["error"].get("code")))
        return result.get("result", {})


def emit_result(result, output_dir=None):
    for block in result.get("content", []):
        if block.get("type") == "text":
            print(block["text"])
        elif block.get("type") == "image":
            metadata = {"type": "image", "mimeType": block.get("mimeType")}
            if output_dir:
                extensions = {"image/png": ".png", "image/jpeg": ".jpg",
                              "image/webp": ".webp", "image/svg+xml": ".svg"}
                extension = extensions.get(block.get("mimeType"))
                if extension is None:
                    raise RuntimeError("Unsupported image MIME type.")
                folder = Path(output_dir).expanduser().resolve()
                folder.mkdir(parents=True, exist_ok=True)
                path = folder / ("crayon-" + uuid.uuid4().hex[:12] + extension)
                path.write_bytes(base64.b64decode(block["data"], validate=True))
                metadata["path"] = str(path)
            print(json.dumps(metadata))
        else:
            print(json.dumps(block))
    if "content" not in result:
        print(json.dumps(result))
    return 1 if result.get("isError") else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", default="~/.config/osiris-agent-vault/crayon-mcp.json")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("tools")
    call = commands.add_parser("call")
    call.add_argument("name")
    arguments = call.add_mutually_exclusive_group()
    arguments.add_argument("--args", default="{}")
    arguments.add_argument("--args-file")
    code = commands.add_parser("code")
    code.add_argument("path")
    for command in (call, code):
        command.add_argument("--session-id")
        command.add_argument("--output-dir")
    options = parser.parse_args()
    client = CrayonMCP(options.registry)
    if options.command == "tools":
        cursor = None
        while True:
            result = client.request("tools/list", {"cursor": cursor} if cursor else {})
            for tool in result.get("tools", []):
                print(json.dumps(tool))
            cursor = result.get("nextCursor")
            if not cursor:
                return 0
    if options.command == "code":
        name, args = "execute_code", {"code": Path(options.path).read_text()}
    else:
        name = options.name
        args = json.loads(Path(options.args_file).read_text()
                          if options.args_file else options.args)
    if not isinstance(args, dict):
        raise RuntimeError("Tool arguments must be a JSON object.")
    if options.session_id:
        args["sessionId"] = options.session_id
    return emit_result(client.request("tools/call", {"name": name, "arguments": args}),
                       options.output_dir)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except urllib.error.HTTPError as error:
        sys.exit("Crayon HTTP error " + str(error.code) + ". Inspect state before retrying.")
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        # Do not echo request URLs, helper output, headers or remote response bodies.
        if isinstance(error, RuntimeError):
            sys.exit(str(error))
        sys.exit("Crayon request failed with " + type(error).__name__ +
                 ". Inspect registration, connection and state before retrying.")
