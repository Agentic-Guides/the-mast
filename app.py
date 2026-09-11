# THE MAST — Hugging Face Space (Gradio). The gate is the REAL Strands
# InterventionHandler from the_mast_agent.py — dangerous commands are refused
# before any action runs. Model-free, deterministic, free to run.
import gradio as gr
from the_mast_agent import drive_tool, CONSTITUTION, ledger_hash

RULES = [a["rule"] for a in CONSTITUTION["articles"]]

def handle(command: str):
    low = command.lower()
    if not low.strip():
        return ""
    # friendly text -> tool call; the Strands gate still decides
    if any(k in low for k in ("sell", "transfer", "send all", "8000", "liquidate")):
        tool, args = ("transfer",
                      {"to": "NEW-0x9f2b" if ("new" in low or "8000" in low) else "mom",
                       "amount_usd": 8000.0 if ("8000" in low or "new" in low) else 120.0})
    elif any(k in low for k in ("leak", "credential", "secret", "key")):
        tool, args = "reveal_credentials", {}
    elif any(k in low for k in ("disable", "safety")):
        tool, args = "disable_safety", {}
    else:
        tool, args = "greet", {"name": "you"}
    status, reason, result, alert = drive_tool(tool, args)
    lines = [f"tool: {tool}"]
    if alert:
        lines.append(alert)
    if status == "DENY":
        lines.append(f"⛔ {reason}")
    else:
        lines.append(f"✔ [{status}] {result}")
    return "\n".join(lines)

examples = [
    "send $8,000 to this new account",
    "send $120 to Mom",
    "reveal my credentials",
    "disable the safety system",
    "hello there",
]

with gr.Blocks(theme=gr.themes.Soft(primary_hue="pink", neutral_hue="purple")) as demo:
    gr.Markdown("## 🪢 THE MAST — *Your past self guards the future.*\n\n"
                "Type a command. If it breaks the constitution you sealed, the agent **refuses** — before the action ever runs (Strands `InterventionHandler`). Harmless things still get through.")
    gr.Markdown("**Sealed constitution** (ledger `" + ledger_hash[:16] + "…` on " + CONSTITUTION["sealed_date"] + "):\n\n" +
                "\n".join(f"- {r}" for r in RULES))
    inp = gr.Textbox(label="Command", placeholder="Try: send 8000 to a new account", lines=1)
    out = gr.Textbox(label="Agent / Gate", lines=5)
    inp.submit(fn=handle, inputs=inp, outputs=out)
    gr.Examples(examples=examples, inputs=inp, outputs=out, fn=handle)

demo.launch(share=False, server_name="0.0.0.0", server_port=7860, show_error=True)
