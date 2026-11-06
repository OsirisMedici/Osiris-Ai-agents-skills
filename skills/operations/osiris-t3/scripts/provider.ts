import { execFileSync, spawn } from "node:child_process";
import { readFileSync } from "node:fs";
import { homedir } from "node:os";

const [target = "mac", action = "status"] = Bun.argv.slice(2);
if (!["mac", "vps"].includes(target) || !["status", "configure"].includes(action)) {
  throw new Error("Usage: bun scripts/provider.ts <mac|vps> <status|configure>");
}
if (process.platform === "linux" && target === "mac") throw new Error("Check the Mac from the Mac host.");
const remote = target === "vps" && process.platform !== "linux";
const sshHost = Bun.env.T3_SSH_HOST ?? "";
const claudeBinary = Bun.env.T3_CLAUDE_BIN ?? "";
if (remote && !/^[a-zA-Z0-9_][a-zA-Z0-9_.@-]*$/.test(sshHost)) {
  throw new Error("Set T3_SSH_HOST to the configured SSH host for the VPS.");
}
if (action === "configure" && !claudeBinary.startsWith("/")) {
  throw new Error("Set T3_CLAUDE_BIN to the absolute Claude CLI path on the target host.");
}
const quote = (s: string) => `'${s.replaceAll("'", "'\"'\"'")}'`;
const lookup = 'import json,pathlib; p=pathlib.Path.home()/".t3/runtime"; print(p/"versions"/json.loads((p/"service-state.json").read_text())["activeVersion"]/"t3")';
const cli = remote
  ? execFileSync("ssh", ["-o", "BatchMode=yes", "-o", "ConnectTimeout=15", sshHost, "python3 -c " + quote(lookup)], { encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] }).trim()
  : process.platform === "linux"
    ? `${homedir()}/.t3/runtime/versions/${JSON.parse(readFileSync(`${homedir()}/.t3/runtime/service-state.json`, "utf8")).activeVersion}/t3`
    : `${homedir()}/.t3/bin/t3`;
function run(args: string[]) {
  try {
    return remote
      ? execFileSync("ssh", ["-o", "BatchMode=yes", "-o", "ConnectTimeout=15", sshHost, [cli, ...args].map(quote).join(" ")], { encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] })
      : execFileSync(cli, args, { encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] });
  } catch {
    throw new Error("T3 CLI request failed; check the host, active runtime and access.");
  }
}

let tunnel: ReturnType<typeof spawn> | undefined;
let issued: { sessionId: string; token: string } | undefined;
let socket: WebSocket | undefined;
let sequence = 0;
const pending = new Map<string, { resolve: (v: any) => void; reject: (e: Error) => void; timer: ReturnType<typeof setTimeout> }>();

function rpc(tag: string, payload: unknown): Promise<any> {
  const id = String(++sequence);
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => { pending.delete(id); reject(new Error(`${tag} timed out`)); }, 45000);
    pending.set(id, { resolve, reject, timer });
    socket!.send(JSON.stringify({ _tag: "Request", id, tag, payload, headers: [] }));
  });
}

function summary(config: any) {
  const list = Array.isArray(config.providers) ? config.providers : Object.values(config.providers ?? {});
  return {
    target,
    providers: list.filter((p: any) => JSON.stringify([p.id, p.instanceId, p.driverKind, p.driver]).includes("claude")).map((p: any) => ({
      id: p.id ?? p.instanceId, driver: p.driverKind ?? p.driver,
      displayName: p.displayName, enabled: p.enabled, installed: p.installed,
      version: p.version, status: p.status,
      auth: { status: p.auth?.status, accountEmail: p.auth?.accountEmail, accountLabel: p.auth?.accountLabel, planType: p.auth?.planType },
      message: p.message,
    })),
    configuredInstance: config.settings?.providerInstances?.claudeAgent,
  };
}

try {
  const scopes = ["orchestration:read", "providers:manage", ...(action === "configure" ? ["settings:write"] : [])];
  issued = JSON.parse(run(["auth", "session", "issue", "--json", "--ttl", "5m", "--label", "T3 Claude setup", ...scopes.flatMap(s => ["--scope", s])]));
  if (remote) {
    tunnel = spawn("ssh", ["-N", "-v", "-o", "BatchMode=yes", "-o", "ConnectTimeout=15", "-o", "ExitOnForwardFailure=yes", "-L", "127.0.0.1:43773:127.0.0.1:3773", sshHost], { stdio: ["ignore", "ignore", "pipe"] });
    await new Promise<void>((resolve, reject) => {
      const timer = setTimeout(() => reject(new Error("SSH forwarding timed out")), 20000);
      tunnel!.stderr!.on("data", data => {
        if (String(data).includes("Local forwarding listening on")) { clearTimeout(timer); resolve(); }
      });
      tunnel!.on("error", () => { clearTimeout(timer); reject(new Error("SSH forwarding failed")); });
      tunnel!.on("exit", code => { clearTimeout(timer); reject(new Error(`SSH forwarding exited ${code}`)); });
    });
  }
  socket = new WebSocket(`ws://127.0.0.1:${remote ? 43773 : 3773}/ws?orchestrationProtocol=2`, { headers: { Authorization: `Bearer ${issued!.token}` } });
  socket.addEventListener("message", event => {
    const raw = JSON.parse(String(event.data));
    for (const m of Array.isArray(raw) ? raw : [raw]) {
      const p = pending.get(String(m.requestId));
      if (m._tag !== "Exit" || !p) continue;
      clearTimeout(p.timer); pending.delete(String(m.requestId));
      if (m.exit?._tag === "Success") p.resolve(m.exit.value);
      else p.reject(new Error(`RPC failed: ${(m.exit?.cause ?? []).map((c: any) => c.error?._tag ?? c._tag).join(", ")}`));
    }
  });
  await new Promise<void>((resolve, reject) => {
    const timer = setTimeout(() => reject(new Error("T3 connection timed out")), 15000);
    socket!.addEventListener("open", () => { clearTimeout(timer); resolve(); }, { once: true });
    socket!.addEventListener("error", () => { clearTimeout(timer); reject(new Error("T3 connection failed")); }, { once: true });
  });
  if (action === "configure") {
    const current = await rpc("server.getConfig", {});
    const existing = current.settings?.providerInstances?.claudeAgent ?? {};
    await rpc("server.updateSettings", {
      patch: {},
      providerInstanceMutation: {
        operation: "upsert", instanceId: "claudeAgent",
        instance: {
          ...existing, driver: "claudeAgent", displayName: existing.displayName ?? "Claude Code", enabled: true,
          config: { ...(existing.config ?? {}), binaryPath: claudeBinary },
        },
      },
    });
  }
  await rpc("server.refreshProviders", { instanceId: "claudeAgent", fresh: true });
  const result = summary(await rpc("server.getConfig", {}));
  if (result.configuredInstance) {
    const x = result.configuredInstance;
    result.configuredInstance = { driver: x.driver, displayName: x.displayName, enabled: x.enabled, config: { binaryPath: x.config?.binaryPath, homePath: x.config?.homePath } };
  }
  console.log(JSON.stringify(result, null, 2));
} catch (error) {
  console.error(error instanceof Error ? error.message : "T3 setup failed");
  process.exitCode = 1;
} finally {
  for (const p of pending.values()) clearTimeout(p.timer);
  socket?.close();
  if (issued) {
    try { run(["auth", "session", "revoke", issued.sessionId]); }
    catch { console.error("Temporary T3 setup session could not be revoked; it expires within five minutes."); }
  }
  tunnel?.kill();
}
