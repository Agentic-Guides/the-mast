#!/bin/bash
# Compose narration at correct offsets, then mux with the video track.
cd /c/Users/hohoh/Desktop/the-mast/video
set -e
A=out/audio

# [delay_ms, file]
spec=(17000 "$A/everyone_racing.mp3" 17000 "$A/ulysses_1.mp3" 30970 "$A/ulysses_2.mp3" 40000 "$A/demo_proceed.mp3" 57000 "$A/demo_proceed2.mp3" 68000 "$A/demo_deny.mp3" 81300 "$A/demo_deny2.mp3" 90000 "$A/tech.mp3" 107000 "$A/arch.mp3" 135000 "$A/impact.mp3" 153000 "$A/impact2.mp3" 167000 "$A/close.mp3")
N=$(( ${#spec[@]} / 2 ))

# build arg list starting with video
args="-y -i out/video_only.mp4"
for ((i=0;i<N;i++)); do args+=" -i ${spec[$((i*2+1))]}"; done

fc="[1:a]adelay=${spec[0]}|${spec[0]}[a0]"
for ((i=1;i<N;i++)); do
  d=${spec[$((i*2))]}
  fc+=",[$((i+1)):a]adelay=${d}|${d}[a${i}]"
done
fc+=",amix=inputs=${N}:normalize=0[aout]"

cmd="ffmpeg ${args} -filter_complex \"${fc}\" -map \"[aout]\" -map 0:v:0 -c:v copy -c:a aac -b:a 192k -shortest out/the-mast-final.mp4"
echo "FC:$fc"
echo "=== RUN ==="
eval "$cmd" 2>&1 | tail -4
echo "=== RESULT ==="
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 out/the-mast-final.mp4
ffprobe -v error -show_entries stream=codec_type -of csv=p=0 out/the-mast-final.mp4
