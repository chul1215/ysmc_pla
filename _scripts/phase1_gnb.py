#!/usr/bin/env python3
"""Phase 1: 모든 HTML의 GNB와 모바일 nav를 신규 카테고리 구조로 일괄 치환.

대상:
  - Cosmetic 17개: about, booking, breast, community, consultation, cosmetic,
    doctor, eye, fat, lifting, male, notice, nose, other, petit, reviews, tour
  - Medical 5개: burn, medical, reconstruction, trauma, pediatric (pediatric은 Phase5에서 삭제 예정)
  - index.html은 별도 처리 (1줄 토바 구조)
"""
import re
import os
import sys

ROOT = '/Users/chul/Documents/WORK/ysmc_pla/'

ABOUT_CURRENT_PAGES = {'about', 'doctor', 'tour', 'notice', 'events', 'hours'}


def cur(current, name):
    return ' class="current"' if current == name else ''


def cosmetic_gnb(current=None):
    about_cur = ' class="current"' if current in ABOUT_CURRENT_PAGES else ''
    return (
'''<nav class="gnb" aria-label="주 메뉴">
        <div class="gnb-item"><a href="about.html"''' + about_cur + '''>병원소개 <span class="gnb-arrow">&#9662;</span></a><div class="gnb-dropdown"><a href="notice.html"''' + cur(current, 'notice') + '''>공지사항</a><a href="tour.html"''' + cur(current, 'tour') + '''>병원둘러보기</a><a href="doctor.html"''' + cur(current, 'doctor') + '''>의료진소개</a><a href="about.html"''' + cur(current, 'about') + '''>오시는 길</a><a href="events.html"''' + cur(current, 'events') + '''>이벤트</a><a href="hours.html"''' + cur(current, 'hours') + '''>진료시간표</a></div></div>
        <div class="gnb-item">
          <a href="eye.html"''' + cur(current, 'eye') + '''>눈성형 <span class="gnb-arrow">&#9662;</span></a>
          <div class="gnb-dropdown dd-wide dd-wide-4">
            <div class="dd-col"><div class="dd-col-label">쌍꺼풀 성형술</div><a href="eye.html#double-eyelid">매몰법</a><a href="eye.html#double-eyelid">부분절개법</a><a href="eye.html#double-eyelid">절개법</a></div>
            <div class="dd-col"><div class="dd-col-label">중년 눈 성형술</div><a href="eye.html#middle-eye">상안검성형술</a><a href="eye.html#middle-eye">눈썹하거상술</a><a href="eye.html#middle-eye">하안검성형술</a></div>
            <div class="dd-col"><div class="dd-col-label">트임술</div><a href="eye.html#trim">앞트임</a><a href="eye.html#trim">뒷트임</a><a href="eye.html#trim">밑트임</a><a href="eye.html#trim">듀얼트임</a><a href="eye.html#trim">윗트임</a></div>
            <div class="dd-col"><div class="dd-col-label">눈밑 성형술</div><a href="eye.html#under-eye">눈밑지방재배치</a><a href="eye.html#under-eye">하안검성형술</a></div>
          </div>
        </div>
        <div class="gnb-item"><a href="nose.html"''' + cur(current, 'nose') + '''>코성형 <span class="gnb-arrow">&#9662;</span></a><div class="gnb-dropdown"><a href="nose.html">콧대성형</a><a href="nose.html">코끝성형</a><a href="nose.html">콧볼축소</a><a href="nose.html">코 재수술</a><a href="nose.html">기능성 코성형</a></div></div>
        <div class="gnb-item"><a href="breast.html"''' + cur(current, 'breast') + '''>가슴성형 <span class="gnb-arrow">&#9662;</span></a><div class="gnb-dropdown"><a href="breast.html">가슴확대술</a><a href="breast.html">가슴축소술</a><a href="breast.html">유두축소술</a><a href="breast.html">함몰유두</a><a href="breast.html">여유증</a></div></div>
        <div class="gnb-item"><a href="lifting.html"''' + cur(current, 'lifting') + '''>동안성형 <span class="gnb-arrow">&#9662;</span></a><div class="gnb-dropdown"><a href="lifting.html">안면거상술</a><a href="lifting.html">반거상술</a><a href="lifting.html">미니거상술</a><a href="lifting.html">목 거상술</a></div></div>
        <div class="gnb-item"><a href="fat.html"''' + cur(current, 'fat') + '''>바디성형 <span class="gnb-arrow">&#9662;</span></a><div class="gnb-dropdown"><a href="fat.html">얼굴지방흡입술</a><a href="fat.html">복부지방흡입술</a><a href="fat.html">허벅지 지방흡입술</a></div></div>
        <div class="gnb-item"><a href="petit.html"''' + cur(current, 'petit') + '''>쁘띠 <span class="gnb-arrow">&#9662;</span></a><div class="gnb-dropdown"><a href="petit.html">울쎄라</a><a href="petit.html">써마지</a><a href="petit.html">보톡스</a><a href="petit.html">필러</a><a href="petit.html">레이저</a></div></div>
      </nav>''')


def medical_gnb(current=None):
    about_cur = ' class="current"' if current in ABOUT_CURRENT_PAGES else ''
    return (
'''<nav class="gnb" aria-label="주 메뉴">
        <div class="gnb-item"><a href="about.html"''' + about_cur + '''>병원소개 <span class="gnb-arrow">&#9662;</span></a><div class="gnb-dropdown"><a href="notice.html"''' + cur(current, 'notice') + '''>공지사항</a><a href="tour.html"''' + cur(current, 'tour') + '''>병원둘러보기</a><a href="doctor.html"''' + cur(current, 'doctor') + '''>의료진소개</a><a href="about.html"''' + cur(current, 'about') + '''>오시는 길</a><a href="events.html"''' + cur(current, 'events') + '''>이벤트</a><a href="hours.html"''' + cur(current, 'hours') + '''>진료시간표</a></div></div>
        <div class="gnb-item"><a href="trauma.html"''' + cur(current, 'trauma') + '''>상처/외상 <span class="gnb-arrow">&#9662;</span></a><div class="gnb-dropdown"><a href="trauma.html">열상</a><a href="trauma.html">찰과상</a><a href="trauma.html">소아열상</a></div></div>
        <div class="gnb-item"><a href="burn.html"''' + cur(current, 'burn') + '''>화상 <span class="gnb-arrow">&#9662;</span></a><div class="gnb-dropdown"><a href="burn.html">소아화상</a><a href="burn.html">구축성형술</a><a href="burn.html">화상흉터재건</a></div></div>
        <div class="gnb-item"><a href="scar.html"''' + cur(current, 'scar') + '''>흉터 <span class="gnb-arrow">&#9662;</span></a><div class="gnb-dropdown"><a href="scar.html">흉터성형술</a><a href="scar.html">흉터치료</a></div></div>
        <div class="gnb-item"><a href="reconstruction.html"''' + cur(current, 'reconstruction') + '''>피부종양 <span class="gnb-arrow">&#9662;</span></a><div class="gnb-dropdown"><a href="reconstruction.html">모반</a><a href="reconstruction.html">피지낭종</a><a href="reconstruction.html">황색종</a></div></div>
        <div class="gnb-item"><a href="fracture.html"''' + cur(current, 'fracture') + '''>안면부골절 <span class="gnb-arrow">&#9662;</span></a><div class="gnb-dropdown"><a href="fracture.html">안와골절</a><a href="fracture.html">비골골절</a><a href="fracture.html">관골골절</a><a href="fracture.html">하악골 골절</a></div></div>
      </nav>''')


def cosmetic_mobile_nav(current=None):
    """cosmetic pages의 mob-nav-section 내부 (mob-switch-tab + sub grids)"""
    about_cur = ' class="current"' if current in ABOUT_CURRENT_PAGES else ''
    return (
'''<div class="mob-nav-section">
      <div class="mob-center-switcher">
        <a href="cosmetic.html" class="mob-switch-tab active">미용성형센터</a>
        <a href="medical.html" class="mob-switch-tab">외상·재건센터</a>
      </div>
      <div class="mob-sub-title">병원소개</div>
      <div class="mob-sub-grid">
        <a href="notice.html"''' + cur(current, 'notice') + '''>공지사항</a>
        <a href="tour.html"''' + cur(current, 'tour') + '''>병원둘러보기</a>
        <a href="doctor.html"''' + cur(current, 'doctor') + '''>의료진소개</a>
        <a href="about.html"''' + cur(current, 'about') + '''>오시는 길</a>
        <a href="events.html"''' + cur(current, 'events') + '''>이벤트</a>
        <a href="hours.html"''' + cur(current, 'hours') + '''>진료시간표</a>
      </div>
      <div class="mob-sub-title">미용성형</div>
      <div class="mob-sub-grid">
        <a href="eye.html"''' + cur(current, 'eye') + '''>눈성형</a>
        <a href="nose.html"''' + cur(current, 'nose') + '''>코성형</a>
        <a href="breast.html"''' + cur(current, 'breast') + '''>가슴성형</a>
        <a href="lifting.html"''' + cur(current, 'lifting') + '''>동안성형</a>
        <a href="fat.html"''' + cur(current, 'fat') + '''>바디성형</a>
        <a href="petit.html"''' + cur(current, 'petit') + '''>쁘띠</a>
      </div>
    </div>''')


def medical_mobile_nav(current=None):
    return (
'''<div class="mob-nav-section">
      <div class="mob-center-switcher">
        <a href="cosmetic.html" class="mob-switch-tab">미용성형센터</a>
        <a href="medical.html" class="mob-switch-tab active">외상·재건센터</a>
      </div>
      <div class="mob-sub-title">병원소개</div>
      <div class="mob-sub-grid">
        <a href="notice.html"''' + cur(current, 'notice') + '''>공지사항</a>
        <a href="tour.html"''' + cur(current, 'tour') + '''>병원둘러보기</a>
        <a href="doctor.html"''' + cur(current, 'doctor') + '''>의료진소개</a>
        <a href="about.html"''' + cur(current, 'about') + '''>오시는 길</a>
        <a href="events.html"''' + cur(current, 'events') + '''>이벤트</a>
        <a href="hours.html"''' + cur(current, 'hours') + '''>진료시간표</a>
      </div>
      <div class="mob-sub-title">외상·재건</div>
      <div class="mob-sub-grid">
        <a href="trauma.html"''' + cur(current, 'trauma') + '''>상처/외상</a>
        <a href="burn.html"''' + cur(current, 'burn') + '''>화상</a>
        <a href="scar.html"''' + cur(current, 'scar') + '''>흉터</a>
        <a href="reconstruction.html"''' + cur(current, 'reconstruction') + '''>피부종양</a>
        <a href="fracture.html"''' + cur(current, 'fracture') + '''>안면부골절</a>
      </div>
    </div>''')


# 파일별 current 마커
COSMETIC_FILES = {
    'about': 'about', 'doctor': 'doctor', 'tour': 'tour', 'notice': 'notice',
    'eye': 'eye', 'nose': 'nose', 'breast': 'breast', 'lifting': 'lifting',
    'fat': 'fat', 'petit': 'petit',
    'male': None, 'other': None, 'booking': None, 'community': None,
    'consultation': None, 'reviews': None, 'cosmetic': None,
}

MEDICAL_FILES = {
    'trauma': 'trauma', 'burn': 'burn', 'reconstruction': 'reconstruction',
    'medical': None, 'pediatric': None,
}

# 정규식 패턴
GNB_RE = re.compile(r'<nav class="gnb" aria-label="주 메뉴">.*?</nav>', re.DOTALL)
# mob-nav-section 내부 switcher+subs 블록. 시작: <div class="mob-nav-section">  끝: </div>(nav-section 종료) + 공백
MOB_RE = re.compile(
    r'<div class="mob-nav-section">.*?</div>\s*</div>(?=\s*<div class="mobile-nav-divider">)',
    re.DOTALL,
)
# 위 패턴 불안정할 수 있으니 더 보수적으로: mob-nav-section 열고 닫기
MOB_RE_ALT = re.compile(
    r'<div class="mob-nav-section">.*?(?=<div class="mobile-nav-divider">)',
    re.DOTALL,
)


def process(name, kind):
    path = os.path.join(ROOT, name + '.html')
    if not os.path.exists(path):
        return f'SKIP (missing): {name}.html'
    with open(path, 'r', encoding='utf-8') as f:
        src = f.read()
    orig = src

    if kind == 'cosmetic':
        current = COSMETIC_FILES.get(name)
        new_gnb = cosmetic_gnb(current)
        new_mob = cosmetic_mobile_nav(current)
    else:
        current = MEDICAL_FILES.get(name)
        new_gnb = medical_gnb(current)
        new_mob = medical_mobile_nav(current)

    # GNB 치환
    m = GNB_RE.search(src)
    if m:
        src = src[:m.start()] + new_gnb + src[m.end():]
    else:
        return f'FAIL (no gnb block): {name}.html'

    # Mobile nav 치환 — 정확한 boundary 찾기
    # mob-nav-section 열기 → 이어지는 첫 `</div>\n    <div class="mobile-nav-divider"` 매칭
    mob_start = src.find('<div class="mob-nav-section">')
    if mob_start == -1:
        return f'WARN (no mob-nav-section): {name}.html [gnb replaced]'
    # 찾아야 하는 종료 지점: mobile-nav-divider 바로 이전의 </div> (닫는 mob-nav-section)
    div_idx = src.find('<div class="mobile-nav-divider"', mob_start)
    if div_idx == -1:
        return f'WARN (no divider): {name}.html [gnb replaced]'
    # divider 앞으로 거슬러 올라가 가장 가까운 `</div>\n    ` 있는 위치
    # 간단하게 divider 시작 직전까지 일단 삭제 → 새 블록 삽입 → 뒤에 공백+divider 붙임
    # 하지만 스페이스/개행 구조를 깨뜨리지 않기 위해 line-based 처리
    # div_idx 이전의 공백은 유지. 즉 div_idx 직전의 공백까지 포함해 new_mob로 교체
    # new_mob은 `</div>` (mob-nav-section 닫음)로 끝나야 함 → block 내부에 </div> 이미 포함됨
    # 따라서 mob_start..div_idx (exclusive)를 new_mob + "\n    "로 교체
    replacement = new_mob + '\n    '
    src = src[:mob_start] + replacement + src[div_idx:]

    if src != orig:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(src)
        return f'OK: {name}.html'
    return f'NOOP: {name}.html'


def main():
    results = []
    for name in COSMETIC_FILES:
        results.append(process(name, 'cosmetic'))
    for name in MEDICAL_FILES:
        results.append(process(name, 'medical'))
    for r in results:
        print(r)


if __name__ == '__main__':
    main()
