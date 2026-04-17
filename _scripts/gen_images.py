#!/usr/bin/env python3
"""Generate page-specific images with Gemini 2.5 Flash Image via REST."""
import base64, json, os, sys, time, urllib.request, urllib.error

API_KEY = os.environ.get("GEMINI_API_KEY", "")
if not API_KEY:
    sys.exit("error: set GEMINI_API_KEY env var before running")
MODEL = "gemini-2.5-flash-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"

ROOT = "/Users/chul/Documents/WORK/ysmc_pla/images/images2/medical"

JOBS = [
    # fracture.html — facial bone fracture
    ("fracture/accurate-diagnosis.png",
     "Professional medical editorial photograph. A Korean male plastic surgeon in dark navy scrubs stands in a modern Korean university hospital imaging room, pointing with his finger at a large wall-mounted monitor showing a photorealistic 3D CT reconstruction of a human facial skull with a visible orbital floor fracture and nasal bone fracture. Cool clinical teal and navy lighting, very realistic medical equipment, photo taken at 50mm, shallow depth of field. No text, no logo, no watermark on image. 4:3 aspect ratio."),

    ("fracture/diagnosis-system.jpg",
     "Close-up professional medical photograph of a modern radiology workstation. A large dark monitor displays a detailed 3D CT reconstruction of a fractured facial skeleton (orbital floor depression visible) with small measurement callouts. A Korean surgeon's hand in a white coat holds a medical stylus near the monitor. Cool teal-navy ambient lighting of a hospital reading room. Photorealistic, sharp focus, DSLR medical editorial style. No text, no logo, no watermark. 4:3 aspect ratio."),

    ("fracture/specialist-surgery.png",
     "Professional medical editorial photograph. Four Korean doctors — a plastic surgeon, a dental surgeon, an ENT specialist, an ophthalmologist — wearing a mix of navy scrubs and white coats, standing together around a backlit radiology lightbox in a bright modern Korean university hospital conference room. They are discussing facial CT films clipped to the lightbox. Collaborative, professional body language. Photorealistic, shallow depth of field, DSLR look. No text, no logo, no watermark. 4:3 aspect ratio."),

    ("fracture/minimal-scar.jpg",
     "Close-up professional surgical photograph. Gloved hands of a Korean plastic surgeon (blue nitrile gloves) making a careful intraoral incision inside the upper gum of a patient lying on an operating table, using fine stainless-steel forceps and a small scalpel. Sterile surgical field with blue drapes around the patient's mouth, bright overhead OR light. Photorealistic, clean medical editorial style, macro detail. No text, no logo, no watermark. 4:3 aspect ratio."),

    # scar.html — scar revision / laser
    ("scar/accurate-diagnosis.png",
     "Professional medical editorial photograph. A Korean male plastic surgeon in soft rose-beige scrubs carefully examines a faded surgical scar on the inner forearm of a Korean female patient seated in a bright consultation room. He is holding a small silver dermatoscope close to her skin. Warm natural window light mixed with soft overhead light. Dusty rose and beige color palette (hex #9E6B7B accent), calm empathetic mood. Photorealistic skin texture, 50mm lens, shallow depth of field, editorial DSLR look. No text, no logo, no watermark. 4:3 aspect ratio."),

    ("scar/diagnosis-system.jpg",
     "Close-up macro medical photograph: the gloved hand of a Korean plastic surgeon measures a healed linear surgical scar on a patient's forearm using a small clear plastic ruler and a dermatoscope. Clean bright hospital consultation room background, soft blur. Warm rose-beige color palette, very realistic skin texture, editorial medical style. DSLR, sharp focus. No text, no logo, no watermark. 4:3 aspect ratio."),

    ("scar/specialist-surgery.png",
     "Professional medical photograph. A Korean plastic surgeon in navy scrubs wearing surgical loupes performs meticulous scar revision surgery on a patient's forearm, using fine microsurgical forceps and a delicate suture needle. Sterile blue operative drape surrounds the surgical field, bright overhead OR light illuminates the skin. Photorealistic, detailed skin and instruments, shallow depth of field, medical editorial DSLR look. No text, no logo, no watermark. 4:3 aspect ratio."),

    ("scar/minimal-scar.jpg",
     "Close-up professional medical photograph. A Korean female patient's forearm resting on a clean white surface, showing a fine, neatly sutured cosmetic scar line after scar revision; a gloved finger of a surgeon gently inspects it. Bright, clean hospital follow-up room, warm rose-beige palette. Photorealistic skin detail, soft warm lighting, editorial medical style. No text, no logo, no watermark. 4:3 aspect ratio."),
]


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
            print(f"  HTTP {e.code}: {err[:200]}", file=sys.stderr)
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
    parts = data["candidates"][0]["content"]["parts"]
    for p in parts:
        if "inlineData" in p and p["inlineData"].get("data"):
            return base64.b64decode(p["inlineData"]["data"])
    raise RuntimeError(f"No image in response: {json.dumps(data)[:300]}")


def main():
    for rel, prompt in JOBS:
        out = os.path.join(ROOT, rel)
        if os.path.exists(out) and os.path.getsize(out) > 1024:
            print(f"SKIP {rel} (exists, {os.path.getsize(out)} bytes)")
            continue
        print(f"GEN  {rel} ...", flush=True)
        img = generate(prompt)
        with open(out, "wb") as f:
            f.write(img)
        print(f"OK   {rel} ({len(img)} bytes)")
        time.sleep(1)


if __name__ == "__main__":
    main()
