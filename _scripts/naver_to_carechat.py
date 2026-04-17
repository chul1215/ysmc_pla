#!/usr/bin/env python3
"""Replace floating CTA '네이버 예약' with '카카오 케어챗 예약' across HTML."""
import os, re, glob, sys

ROOT = "/Users/chul/Documents/WORK/ysmc_pla"

# Pattern 1: floating CTA HTML block (multiline)
FLOAT_HTML_RE = re.compile(
    r'<a href="#naver-booking" class="float-cta-btn float-btn-naver">\s*'
    r'<span class="float-cta-icon">N</span>네이버 예약\s*'
    r'</a>'
)
FLOAT_HTML_NEW = (
    '<a href="#" class="float-cta-btn float-btn-carechat">\n'
    '        카카오 케어챗 예약\n'
    '      </a>'
)

# Pattern 2: CSS color rule (single line)
CSS_BG_OLD = ".float-btn-naver { background: #03C75A; color: #fff; }"
CSS_BG_NEW = ".float-btn-carechat { background: #3C1E1E; color: #FEE500; }"

# Pattern 3: CSS icon rule (single line, to delete)
CSS_ICON_RE = re.compile(
    r'^\s*\.float-btn-naver \.float-cta-icon \{ background: rgba\(255,255,255,0\.20\); \}\s*\n',
    re.MULTILINE,
)

changes = []
for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
    with open(path, "r", encoding="utf-8") as f:
        src = f.read()
    orig = src

    # HTML block replace (keep original leading whitespace by not anchoring)
    src, n_html = FLOAT_HTML_RE.subn(FLOAT_HTML_NEW, src)
    # CSS main rule
    n_css = src.count(CSS_BG_OLD)
    src = src.replace(CSS_BG_OLD, CSS_BG_NEW)
    # CSS icon rule delete
    src, n_icon = CSS_ICON_RE.subn("", src)

    if src != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(src)
        changes.append((os.path.basename(path), n_html, n_css, n_icon))

print(f"{'FILE':<30} {'HTML':>5} {'CSS':>5} {'ICON':>5}")
for fn, h, c, i in changes:
    print(f"{fn:<30} {h:>5} {c:>5} {i:>5}")
print(f"\ntotal files changed: {len(changes)}")
