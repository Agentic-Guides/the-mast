import React from "react";
import { Composition } from "remotion";
import { TheMast } from "./TheMast";
import { TheBulwark } from "./TheBulwark";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="TheMast"
        component={TheMast}
        durationInFrames={5370} // ~3 min, synced to edge-tts narration
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="TheBulwark"
        component={TheBulwark}
        durationInFrames={3600} // ~2 min, pure video (no <Audio>)
        fps={30}
        width={1920}
        height={1080}
      />
    </>
  );
};
