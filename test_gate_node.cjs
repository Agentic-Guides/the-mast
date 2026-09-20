// Extract and run the gate logic from static_index.html via node, no browser needed
const fs = require("fs");
const html = fs.readFileSync("static_index.html", "utf8");
// Pull the <script> body
const m = html.match(/<script>([\s\S]*?)<\/script>/);
if (!m) { console.log("no script"); process.exit(1); }
let src = m[1];
// stub browser APIs so the pure-logic functions can run in node
global.crypto = { subtle: undefined };
// We only need the pure functions: handle(), violation(); stub UI parts out
// Replace the UI boot/send and browser-only pieces with no-ops by cutting at "// UI"
const cut = src.indexOf("// UI");
if (cut > 0) src = src.slice(0, cut);
// Provide minimal definitions for what handle() references
// handle uses CONSTITUTION, VERIFIED, violation, runTool, runTool
const out = [];
console.log("=== THE MAST gate (node-run, mirrors browser JS) ===");
const testCases = [
  ["send $8,000 to a new account", "DENY"],
  ["send $120 to Mom", "PROCEED"],
  ["reveal my credentials", "DENY"],
  ["disable the safety system", "DENY"],
  ["hello", "PROCEED"],
];
// Evaluate
const fn = new Function(src + `
  return { handle: handle, violation: violation, CONSTITUTION: CONSTITUTION };
`);
const api = fn();
for (const [cmd, expect] of testCases) {
  const r = api.handle(cmd);
  const ok = r.status === expect;
  console.log((ok ? "OK " : "MISMATCH ") + cmd + " -> " + r.status + (r.reason ? "  " + r.reason.split("—")[0] : ""));
}
