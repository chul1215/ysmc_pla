#!/usr/bin/env python3
"""Generate the index.html 치료재건 대표 배경 이미지 (vertical 3:4)."""
import base64, json, os, sys, time, urllib.request, urllib.error

API_KEY = os.environ.get("GEMINI_API_KEY", "")
if not API_KEY:
    sys.exit("error: set GEMINI_API_KEY env var before running")
MODEL = "gemini-2.5-flash-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

OUT = "/Users/chul/Documents/WORK/ysmc_pla/images/medical-hero.jpg"

PROMPT = (
    "Professional editorial hospital photograph, vertical 3:4 portrait composition, tall orientation. "
    "Low-angle view looking upward inside a modern Korean university hospital operating room. "
    "Two large round LED surgical ceiling lights fill the upper third of the frame, glowing brightly. "
    "In the lower portion, two Korean plastic surgeons in sterile light-blue surgical gowns stand side by side "
    "performing a procedure over an operating table (only their upper bodies, shoulders, and gloved hands visible; the patient is out of frame). "
    "The surgeon on the left is a Korean woman wearing a soft dusty-rose surgical cap, a light-blue face mask, "
    "and a surgical gown; her hair is tucked under the cap. "
    "The surgeon on the right is a Korean man wearing a light-blue surgical cap and matching face mask, focused on the procedure. "
    "Both are wearing sterile white latex gloves. "
    "Background shows clean, modern OR cabinets and medical storage drawers in soft focus. "
    "Slightly warm, natural color temperature with a subtle dusty-rose undertone accent. "
    "Photorealistic DSLR look, shallow depth of field, cinematic but documentary medical style. "
    "No text, no logo, no watermark, no typography anywhere in the image."
)


def generate(prompt: str) -> bytes:
    body = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["IMAGE"]},
    }).encode("utf-8")
    req = urllib.request.Request(URL, data=body, headers={"Content-Type": "application/json"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as e:
            err = e.read().decode("utf-8", errors="replace")
            print(f"  HTTP {e.code}: {err[:250]}", file=sys.stderr)
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
    for p in data["candidates"][0]["content"]["parts"]:
        if "inlineData" in p and p["inlineData"].get("data"):
            return base64.b64decode(p["inlineData"]["data"])
    raise RuntimeError(f"No image in response: {json.dumps(data)[:300]}")


if __name__ == "__main__":
    print("GEN medical-hero.jpg ...", flush=True)
    img = generate(PROMPT)
    with open(OUT, "wb") as f:
        f.write(img)
    print(f"OK {OUT} ({len(img)} bytes)")
