#!/usr/bin/env python3
"""Restore 네이버 예약 alongside 카카오 케어챗 예약 across all HTML."""
import os, re, glob

ROOT = "/Users/chul/Documents/WORK/ysmc_pla"

# A. Append 네이버 예약 after 카카오 케어챗 예약 in the floating CTA block
FLOAT_BLOCK_RE = re.compile(
    r'(<a href="#" class="float-cta-btn float-btn-carechat">\s*'
    r'카카오 케어챗 예약\s*'
    r'</a>)(?!\s*<a href="#naver-booking")'
)
FLOAT_APPEND = (
    r'\1\n'
    '      <a href="#naver-booking" class="float-cta-btn float-btn-naver">\n'
    '        <span class="float-cta-icon">N</span>네이버 예약\n'
    '      </a>'
)

# B. Append Naver CSS rules right after the carechat rule
CSS_CARECHAT_ONLY = ".float-btn-carechat { background: #3C1E1E; color: #FEE500; }"
CSS_CARECHAT_WITH_NAVER = (
    ".float-btn-carechat { background: #3C1E1E; color: #FEE500; }\n"
    "    .float-btn-naver { background: #03C75A; color: #fff; }\n"
    "    .float-btn-naver .float-cta-icon { background: rgba(255,255,255,0.20); }"
)

changes = []
for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    orig = src

    src, n_block = FLOAT_BLOCK_RE.subn(FLOAT_APPEND, src)

    n_css = 0
    if CSS_CARECHAT_ONLY in src and ".float-btn-naver {" not in src:
        src = src.replace(CSS_CARECHAT_ONLY, CSS_CARECHAT_WITH_NAVER, 1)
        n_css = 1

    if src != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(src)
        changes.append((os.path.basename(path), n_block, n_css))

print(f"{'FILE':<30} {'BLOCK':>6} {'CSS':>5}")
for fn, b, c in changes:
    print(f"{fn:<30} {b:>6} {c:>5}")
print(f"\ntotal files changed: {len(changes)}")
