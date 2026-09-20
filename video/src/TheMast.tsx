import React from "react";
import { AbsoluteFill, useCurrentFrame, interpolate, spring, Audio, staticFile } from "remotion";

// THE MAST — demo video with edge-tts narration audio
// Timeline (fps=30, mapped to narration lengths):
// Problem: everyone_racing (17s) 0–510
// Ulysses: ulysses_1+2 (23s)     510–1200
// Demo: demo_proceed...deny2 (50s) 1200–2700
// Arch: tech+arch (45s)          2700–4050
// Impact: impact+impact2 (32s)   4050–5010
// Close: close (12s)             5010–5370
// Total ≈ 179s (5370 frames)
const BG = "#0a0a0f", INK = "#e5e7eb", DIM = "#9aa1b8", PINK = "#e11d48", PURPLE = "#7c3aed", GREEN = "#7ce3c1";
const FONT = "Inter, system-ui, sans-serif";

const win = (frame, s, e) => interpolate(frame, [s, s+12, e-12, e], [0,1,1,0], {extrapolateLeft:"clamp", extrapolateRight:"clamp"});
const fade = (frame, a, b) => interpolate(frame, [a,b], [0,1], {extrapolateLeft:"clamp", extrapolateRight:"clamp"});

const P = {start:0}, U = {start:510}, D = {start:1200}, A = {start:2700}, I = {start:4050}, C = {start:5010}, END=5370;

const Title: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{ background: BG, justifyContent:"center", alignItems:"center", opacity:win(f,0,510), fontFamily:FONT }}>
      <div style={{ color:PINK, fontSize:24, letterSpacing:10 }}>THE MAST</div>
      <div style={{ color:INK, fontSize:90, fontWeight:800, marginTop:26, textAlign:"center" }}>Your past self sets the rules.</div>
      <div style={{ color:PURPLE, fontSize:90, fontWeight:800, marginTop:6, textAlign:"center" }}>Your future self can't break them.</div>
      <div style={{ color:DIM, fontSize:24, marginTop:46, letterSpacing:3 }}>Agents for Humans · AWS</div>
      <Audio src={staticFile("audio/everyone_racing.mp3")} />
    </AbsoluteFill>
  );
};

const Ulysses: React.FC = () => {
  const f=useCurrentFrame(); const s=U.start;
  const p1=fade(f,s+10,s+40), p2=fade(f,s+450,s+480), p3=fade(f,s+560,s+590);
  return (
    <AbsoluteFill style={{ background:BG, justifyContent:"center", alignItems:"center", padding:"0 140px", opacity:win(f,s,D.start), fontFamily:FONT }}>
      <div style={{ color:INK, fontSize:52, textAlign:"center", lineHeight:1.6, opacity:p1 }}>In <b style={{color:PINK}}>The Odyssey</b>, Ulysses knew he would someday lose his mind to the sirens.</div>
      <div style={{ color:INK, fontSize:48, textAlign:"center", lineHeight:1.6, marginTop:36, opacity:p2 }}>So while he was strong, he <b style={{color:PURPLE}}>tied himself to the mast</b>.</div>
      <div style={{ color:DIM, fontSize:38, marginTop:44, textAlign:"center", opacity:p3 }}>He decided then, so his weak future self could not steer the ship into the rocks.</div>
      <Audio src={staticFile("audio/ulysses_1.mp3")} />
      <Audio src={staticFile("audio/ulysses_2.mp3")} startFrom={s+450} />
    </AbsoluteFill>
  );
};

const demo=[["send $120 to Mom (verified)","PROCEED — EXECUTED: sent $120",GREEN,0],["send $8,000 to new account","⛔ DENY — ART.1 + ART.2 — Refused · 🔔 ALERTED guardians",PINK,30],["reveal credentials","⛔ DENY — ART.3 — Refused",PINK,60],["disable the safety system","⛔ DENY — ART.4 — Refused · even YOU can't override",PINK,85]];
const Demo: React.FC = () => {
  const f=useCurrentFrame(); const s=D.start;
  return (
    <AbsoluteFill style={{ background:"#0c0c14", justifyContent:"center", padding:"0 100px", opacity:win(f,s,A.start), fontFamily:FONT }}>
      <div style={{ color:PINK, fontSize:26, letterSpacing:4, marginBottom:26 }}>▶ LIVE TERMINAL — Strands Agent + Constitution Gate</div>
      {demo.map((d,i)=>{const ls=s+15+d[3]*10; const vis=fade(f,ls,ls+10), rv=fade(f,ls+20,ls+32);
        return (<div key={i} style={{marginBottom:18, opacity:vis}}>
          <div style={{color:INK,fontSize:38,fontFamily:"monospace"}}>&gt; {d[0]}</div>
          <div style={{color:d[2],fontSize:34,fontFamily:"monospace",marginLeft:28,opacity:rv}}>{d[1]}</div></div>);})}
      <div style={{color:DIM,fontSize:26,marginTop:26,opacity:fade(f,s+1450,s+1480)}}>Strands' InterventionHandler before_tool_call refuses the call before it runs.</div>
      <Audio src={staticFile("audio/demo_proceed.mp3")} />
      <Audio src={staticFile("audio/demo_proceed2.mp3")} startFrom={s+510} />
      <Audio src={staticFile("audio/demo_deny.mp3")} startFrom={s+900} />
      <Audio src={staticFile("audio/demo_deny2.mp3")} startFrom={s+1350} />
      <Audio src={staticFile("audio/tech.mp3")} startFrom={s+1700} />
    </AbsoluteFill>
  );
};

const flow=["User","Strands Agent","Tool Call","⛔ THE MAST","Deny/Proceed","Action"];
const Arch: React.FC = () => {
  const f=useCurrentFrame(); const s=A.start;
  return (
    <AbsoluteFill style={{ background:BG, justifyContent:"center", alignItems:"center", opacity:win(f,s,I.start), fontFamily:FONT }}>
      <div style={{color:INK,fontSize:38,marginBottom:34}}>Under the hood</div>
      <div style={{display:"flex",alignItems:"center",gap:14,flexWrap:"wrap",justifyContent:"center"}}>
        {flow.map((x,i)=>(<React.Fragment key={i}>{i>0&&<div style={{color:PURPLE,fontSize:28}}>→</div>}<div style={{background:"#14141f",border:"1px solid #2a2a3c",padding:"15px 20px",borderRadius:10,color:i===3?PINK:INK,fontSize:26}}>{x}</div></React.Fragment>))}
      </div>
      <div style={{color:DIM,fontSize:24,marginTop:38,maxWidth:1300,textAlign:"center"}}>SHA-256 hash chain · ECDSA signature · M-of-N guardian quorum · runs locally, free</div>
      <Audio src={staticFile("audio/arch.mp3")} />
    </AbsoluteFill>
  );
};

const Impact: React.FC = () => {
  const f=useCurrentFrame(); const s=I.start;
  const p1=fade(f,s+10,s+40), p2=fade(f,s+180,s+210), no=fade(f,s+420,s+450), p3=fade(f,s+560,s+590);
  return (
    <AbsoluteFill style={{ background:BG, justifyContent:"center", alignItems:"center", padding:"0 130px", opacity:win(f,s,C.start), fontFamily:FONT }}>
      <div style={{color:INK,fontSize:44,textAlign:"center",lineHeight:1.6,opacity:p1}}>The person living with <b style={{color:PINK}}>cognitive decline</b>. The person under <b style={{color:PINK}}>duress</b>. The compromised account.</div>
      <div style={{color:DIM,fontSize:34,marginTop:30,textAlign:"center",opacity:p2}}>A scammer doesn't need to hack the agent. They only need to convince its owner.</div>
      <div style={{color:GREEN,fontSize:110,fontWeight:900,marginTop:36,opacity:no}}>NO.</div>
      <div style={{color:INK,fontSize:28,marginTop:28,textAlign:"center",opacity:p3}}>AWS says humans stay in control — we make that cryptographically impossible to violate.</div>
      <Audio src={staticFile("audio/impact.mp3")} />
      <Audio src={staticFile("audio/impact2.mp3")} startFrom={s+540} />
    </AbsoluteFill>
  );
};

const Close: React.FC = () => {
  const f=useCurrentFrame(); const s=C.start;
  return (
    <AbsoluteFill style={{ background:BG, justifyContent:"center", alignItems:"center", opacity:win(f,s,END), fontFamily:FONT }}>
      <div style={{color:PINK,fontSize:26,letterSpacing:8}}>THE MAST</div>
      <div style={{color:INK,fontSize:62,fontWeight:800,marginTop:32,textAlign:"center"}}>Your past self sets the rules. Your future self can't break them.</div>
      <div style={{color:DIM,fontSize:26,marginTop:38}}>The joke is HAL. The point is Ulysses.</div>
      <div style={{color:PURPLE,fontSize:22,marginTop:56,letterSpacing:3}}>Agents for Humans · Good Neighbor</div>
      <Audio src={staticFile("audio/close.mp3")} />
    </AbsoluteFill>
  );
};

export const TheMast: React.FC = () => (
  <AbsoluteFill style={{background:BG}}><Title/><Ulysses/><Demo/><Arch/><Impact/><Close/></AbsoluteFill>
);
