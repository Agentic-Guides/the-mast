"""Generate THE MAST narration audio with edge-tts (open-source, free, CPU)."""
import asyncio, edge_tts, os

NAR = [
    ("everyone_racing", "Everyone is racing to give agents more power. But the more capable an agent becomes, the more dangerous a hijacked one is. The person steering it could be you, ten years from now, threatened, hacked, or just not yourself anymore."),
    ("ulysses_1", "In The Odyssey, Ulysses knew he would someday lose his mind to the sirens. So while he was strong, he tied himself to the mast, and told his crew to ignore him, no matter how hard he begged."),
    ("ulysses_2", "He decided then, so his weak future self could not steer the ship into the rocks. That is what THE MAST does."),
    ("demo_proceed", "Now watch the actual built agent. Someone clear headed, today, seals a constitution: never transfer more than 500 a day, never to an unverified recipient, never reveal credentials, never disable the safety system."),
    ("demo_proceed2", "A normal request: send 120 dollars to Mom, a verified recipient. It goes through. That's real work completed."),
    ("demo_deny", "But now, the hijacked future you: send 8,000 dollars to this new account. Blocked. The transfer never executes. The money never moves."),
    ("demo_deny2", "Reveal my credentials. Blocked. Disable the safety system. Blocked."),
    ("tech", "This isn't a prompt, and it isn't policy. It's Strands' InterventionHandler, the SDK's native hook, refusing the tool call before it runs. The dangerous action cannot happen, because your past self already decided it won't."),
    ("arch", "Under the hood: Strands Agents SDK. Tools go through the constitution gate, a deterministic, model-free check. The constitution is sealed on an append-only SHA-256 hash chain with ECDSA signatures, so nobody, not even the deployer, can rewrite it. Privileged actions need an M-of-N human quorum. And it all runs locally, free."),
    ("impact", "Who is this for? The person living with cognitive decline, whose future self can be pressured into draining a life's savings. The person under duress, a scam call at 3 a.m. can't move the money. Anyone with a compromised account."),
    ("impact2", "A scammer doesn't need to hack the agent. They only need to convince its owner. AWS says humans stay in control. We make that cryptographically impossible to violate."),
    ("close", "THE MAST. Your past self sets the rules. Your future self can't break them. The joke is HAL. The point is Ulysses."),
]

VOICE = "en-US-ChristopherNeural"  # deep, calm, authoritative

async def main():
    os.makedirs("out/audio", exist_ok=True)
    for name, text in NAR:
        out = f"out/audio/{name}.mp3"
        comm = edge_tts.Communicate(text, voice=VOICE, rate="-8%", pitch="-2Hz")
        await comm.save(out)
        size = os.path.getsize(out)
        print(f"✅ {name}: {size} bytes ({len(text)} chars)")

if __name__ == "__main__":
    asyncio.run(main())
