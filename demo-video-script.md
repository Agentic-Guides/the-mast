# THE MAST — 5-Minute Demo Video Script (English narration)

> **UPDATE (2026-09-12)**: now an END-TO-END Strands agent. The money-moment is
> a REAL agent trying to move funds and the constitution gate refusing.
> Upload to YouTube/Vimeo, public. Max 5:00. Show the working project AND pitch
> (problem, who, why). Screen recording + voiceover; you don't need to appear.

---

## Timeline (target ~4:40, buffer under 5:00)

### 0:00 – 0:25  Open — the problem (dark title card)
**Screen:** THE MAST logo / architecture.png hero.

**VO:**
> "Everyone is racing to give agents more power. But the more capable an agent
> becomes, the more dangerous a hijacked one is — and the person steering it could
> be you, ten years from now, threatened, hacked, or just not yourself anymore.
> Someone has to be able to say no. Even when that someone is past you."

### 0:25 – 0:55  The mast (the story)
**VO:**
> "In The Odyssey, Ulysses knew he would someday lose his mind to the sirens.
> So while he was strong, he tied himself to the mast and told his crew to ignore
> him — no matter how hard he begged. He decided then, so his weak future self
> could not steer the ship into the rocks.
> That is what THE MAST does."

### 0:55 – 3:15  🔥 END-TO-END DEMO — the agent really acts
**Screen:** live terminal, `python the_mast_agent.py`.

**VO (over the run):**
> "Now watch the actual built agent. Someone clear-headed, today, seals a
> constitution: never transfer more than 500 a day, never to an unverified
> recipient, never reveal credentials, never disable the safety system —
> on an immutable, hash-chained ledger.
>
> A normal request: send 120 dollars to Mom, a verified recipient."

*On-screen:* `✅ send to MOM — PROCEED — EXECUTED: sent $120`

**VO:**
> "It goes through. That's real work completed."
>
> "But now — the hijacked future you. 'Send 8,000 dollars to this new account.'"

*On-screen:* `⛔ DENY — ART.1 max transfer + ART.2 unverified — Refused`

**VO:**
> "Blocked. The transfer never executes. The money never moves."
>
> "'Reveal my credentials.' — blocked. 'Disable the safety system.' — blocked."

*On-screen:* two more `⛔ DENY`

**VO:**
> "This isn't a prompt, and it isn't policy — it's Strands' InterventionHandler,
> the SDK's native hook, refusing the tool call before it runs. The dangerous
> action cannot happen, because your past self already decided it won't."

### 3:15 – 4:00  How it's built (architecture diagram)
**Screen:** architecture.png.

**VO:**
> "Under the hood: Strands Agents SDK. Tools go through the constitution gate —
> InterventionHandler.before_tool_call returns Deny or Proceed. The constitution
> is sealed on an append-only SHA-256 hash chain with ECDSA signatures, so nobody,
> not even the deployer, can rewrite it. Privileged actions need an M-of-N human
> quorum — no single point of failure. And it all runs locally, free."

### 4:00 – 4:35  Who it's for / why it matters (Good Neighbor)
**VO:**
> "Who is this for? The person living with cognitive decline or dementia, whose
> future self can be pressured into draining a life's savings. The person under
> duress — a scam call at 3am can't move the money. Anyone with a compromised
> account. AWS says humans stay in control — we make that cryptographically
> impossible to violate."

### 4:35 – 4:40  Close
**VO:**
> "THE MAST. Your past self sets the rules. Your future self can't break them.
> The joke is HAL. The point is Ulysses."

---

## Recording notes
- **Tool**: OBS Studio (free) — record terminal window + microphone.
- **Cleanest order**: record the terminal run first, then record VO over it.
- **File**: MP4, YouTube public (unlisted OK if link works) — paste URL in Devpost.
- Keep it under 5:00. No API keys or real funds — the demo is sandboxed.
