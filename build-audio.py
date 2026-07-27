#!/usr/bin/env python3
"""Build meditation.mp3 from meditation-script.md.

Parses the numbered segments and [silence Ns] gaps from the script,
synthesizes each segment with Google Cloud TTS (Chirp 3 HD), joins them
with real silence, and encodes with lame.

Usage: python3 build-audio.py
Requires: gcloud auth (billed project below), lame on PATH.
"""
import base64
import json
import re
import subprocess
import wave

VOICE = "en-AU-Chirp3-HD-Enceladus"
SPEAKING_RATE = 0.85
RATE = 24000
BILLING_PROJECT = "nanager-f8c08"
LEAD_IN_S = 1.5
TAIL_S = 4.0

def parse_script(path):
    text = open(path).read()
    body = text.split("---\n", 1)[1].split("\n---", 1)[0]
    segments = []
    pattern = re.compile(r"^\d+\.\s(.*?)(?=\n\s*\[silence|\n\d+\.|\Z)", re.M | re.S)
    silences = re.findall(r"\[silence (\d+)s\]", body)
    blocks = pattern.findall(body)
    for i, block in enumerate(blocks):
        spoken = " ".join(line.strip() for line in block.strip().splitlines() if line.strip())
        gap = int(silences[i]) if i < len(silences) else 0
        segments.append((spoken, gap))
    return segments

def synth(token, text):
    body = json.dumps({
        "input": {"text": text},
        "voice": {"languageCode": "en-AU", "name": VOICE},
        "audioConfig": {"audioEncoding": "LINEAR16", "sampleRateHertz": RATE,
                        "speakingRate": SPEAKING_RATE},
    })
    out = subprocess.run(
        ["curl", "-s", "-X", "POST",
         "https://texttospeech.googleapis.com/v1/text:synthesize",
         "-H", f"Authorization: Bearer {token}",
         "-H", f"x-goog-user-project: {BILLING_PROJECT}",
         "-H", "Content-Type: application/json", "-d", body],
        capture_output=True, text=True).stdout
    resp = json.loads(out)
    if "audioContent" not in resp:
        raise SystemExit(f"TTS error: {out[:300]}")
    raw = base64.b64decode(resp["audioContent"])
    return raw[44:] if raw[:4] == b"RIFF" else raw

def main():
    token = subprocess.run(["gcloud", "auth", "print-access-token"],
                           capture_output=True, text=True).stdout.strip()
    segments = parse_script("meditation-script.md")
    print(f"{len(segments)} segments")
    pcm = b"\x00" * int(RATE * LEAD_IN_S * 2)
    for i, (text, gap) in enumerate(segments, 1):
        pcm += synth(token, text)
        pcm += b"\x00" * int(RATE * gap * 2)
        print(f"  [{i:2}] {text[:60]}…  +{gap}s")
    pcm += b"\x00" * int(RATE * TAIL_S * 2)
    with wave.open("/tmp/meditation.wav", "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(RATE)
        w.writeframes(pcm)
    subprocess.run(["lame", "--quiet", "-m", "m", "-b", "96", "/tmp/meditation.wav", "meditation.mp3"], check=True)
    seconds = len(pcm) / (RATE * 2)
    print(f"\nduration: {seconds:.1f}s  ->  MEDITATION_MS = {int(seconds * 1000) + 500}")

if __name__ == "__main__":
    main()
