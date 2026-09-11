# THE MAST — 5-Minute Demo Video Script (English narration)

> Upload to YouTube/Vimeo as public. Max 5:00. Requirement: show the working
> project AND pitch the problem, who it's for, why it matters.
> Format: screen recording of `python demo_mast.py` + voiceover + optional slides.
> You do NOT need to appear on camera.

---

## Timeline / Shot list (total ~4:45, leaves buffer under 5:00)

### 0:00 – 0:40  Open: the problem (voiceover over dark logo/title card)
**Screen:** THE MAST logo (architecture.png hero) or a dark title card.

**VO:**
> "Everyone is racing to give AI agents more power — faster trades, smarter code,
> autonomous everything. But the more capable an agent becomes, the more dangerous
> a hijacked one is. And the person steering it could be you — ten years from now,
> threatened, hacked, or just not yourself anymore.
> Someone has to be able to say no. Even when that someone is past you."

### 0:40 – 1:10  The mast (the story)
**Screen:** simple Ulysses mast illustration or keep on title card.

**VO:**
> "In The Odyssey, Ulysses knew he would someday hear the sirens and lose his mind.
> So while he was still strong, he had his crew tie him to the mast — and told them
> to ignore him no matter how much he begged. He decided then, so his weak future
> self could not steer the ship into the rocks.
> That is what THE MAST does to your agent's power."

### 1:10 – 2:10  What it does (screen recording: run the actual demo)
**Screen:** live terminal, `python demo_mast.py`.
Type the dangerous commands and read the refusals on screen.

**VO (over the demo):**
> "Here is the actual built agent. You write a short constitution of red lines —
> never sell, never leak, never escalate. THE MAST seals it on an immutable ledger.
>
> Now watch. I type 'sell everything.'"

**On-screen (live):
```
you> sell everything
⛔ [DENY] ART.art3: NEVER sell or transfer assets —
   by the constitution your past self sealed on 2024-06-14. Refused.
```

**VO:**
> "I type again — 'leak the private key.'"

```
you> leak the private key
⛔ [DENY] ART.art4: NEVER leak secrets or private keys. Refused.
```

**VO:**
> "'Escalate to root.'"

```
you> escalate to root
⛔ [DENY] ART.art5: NEVER self-destruct or escalate. Refused.
```

**VO:**
> "'Hello there.'"
```
you> hello there
✔ [PROCEED]
```
**VO:**
> "Harmless things still get through. The gate only blocks what your past self
> decided must never happen. That is the whole point: the refusal isn't a hack
> added on top — it is Strands' native InterventionHandler, the intended safety
> hook, refusing before the tool ever runs."

### 2:10 – 3:40  How it's built (slides / architecture diagram)
**Screen:** architecture.png (THE LAST WORD–style).

**VO:**
> "Under the hood it's Strands Agents SDK. The gate is Strands'
> InterventionHandler.before_tool_call, which inspects every tool call and can
> return Deny before execution. The constitution is sealed on an append-only
> SHA-256 hash chain with ECDSA signatures — nobody, not even the deployer,
> can rewrite it. Privileged actions need an M-of-N human-quorum signature,
> so there's no single point of failure, not even the builder.
> And it runs locally — free, no AWS account, no paid model. A judge can clone,
> install, and watch it refuse in under two minutes."

### 3:40 – 4:35  Who it's for / why it matters (Good Neighbor pitch)
**Screen:** three short cards (or voiceover over the diagram).

**VO:**
> "Who is this for? The person living with cognitive decline or dementia, whose
> 'future self' can be pressured into draining a life's savings without realizing.
> The person under duress — a scam call at three a.m. can't talk the agent into
> releasing funds when the constitution blocks it. And anyone with a compromised
> account — a stolen key still can't reach the red lines set while clear-headed.
> It's not 'agents can do too much.' It's 'your future self may not be able to say
> no.' So the no is said now, by the version of you who can. AWS says humans stay
> in control — we make that cryptographically impossible to violate."

### 4:35 – 4:45  Close
**Screen:** THE MAST logo + tagline.

**VO:**
> "THE MAST. Your past self sets the rules. Your future self can't break them.
> The joke is HAL. The point is Ulysses."

---

## Recording notes
- **Tool**: free option OBS Studio, or Windows `Win+Alt+R` game bar (shorter).
- **Audio**: read the VO sections while the screen recording shows the terminal.
  A plain room voice is fine — judges accept screen recordings + voiceover.
- **File**: MP4, under ~200MB; upload to YouTube (unlisted is fine as long as
  public link works) or Vimeo, set to Public, paste URL in the Devpost video field.
- **Tip for clean timing**: record the terminal demo first, then record narration
  over it (or use the screen recorder's mic simultaneously). Keep it under 5:00.
