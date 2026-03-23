# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

유성선병원 성형외과 신설 부서 홍보용 정적 웹사이트. 빌드 시스템이 없으며 순수 HTML/CSS/JS로 구성된다.

- **언어**: 한국어 (lang="ko")
- **스택**: 순수 HTML5 + CSS3 + Vanilla JS (프레임워크/패키지 없음)
- **배포**: GitHub Pages (`https://chul1215.github.io/ysmc_pla/`) — main 브랜치 푸시 시 자동 배포
- **로컬 서버**: `python3 -m http.server 8080`

## 파일 구성

- `index.html` — 메인 홈 (스플릿 히어로)
- `dashboard.html` — 관리자 대시보드 (Tailwind CSS, **별도 아키텍처**)
- `cosmetic.html` / `medical.html` — 진료 허브 페이지 (각 카테고리 진입점)
- 미용·성형 상세 8개: `eye`, `nose`, `lifting`, `male`, `fat`, `breast`, `other`, `petit`
- 치료·재건 상세 4개: `trauma`, `burn`, `reconstruction`, `pediatric`
- 기관 소개: `about`, `doctor`, `tour`
- 커뮤니티: `community`, `consultation`, `booking`, `news`, `notice`
- `_archive/` — 미사용 보관 (GNB에서 제거된 features.html, academic.html 등)

### 사용 가능한 이미지 (`images/` 폴더)

루트: `eye-correction.png`, `lifting.jpg`, `petit-skin.png`, `surgery-room.jpg`, `shin_profile.jpg` 및 눈성형 시술 이미지 다수 (`매몰법_den.png`, `절개법_dei.png`, `앞트임_epi.png` 등).

`images/mc-image/미용성형/` — 카테고리 카드용 실사진 8종 + 메인/세컨페이지 이미지:
- `미용성형 메인.jpg`, `미용성형 세컨페이지.jpg`
- `1. 아이 센터.png`, `2. 라이노플래스티.jpg`, `3. 리프팅 안티에이징.jpg`, `4. 메일 코스매틱.png`, `5. 팻 컨투어링.jpg`, `6. 브레스트 써저리.jpg`, `7. 아더 써저리.jpg`, `8. 쁘띠스킨.jpg`

`images/mc-image/치료재건/` — 카테고리 카드용 실사진 4종 + 메인/세컨페이지 이미지:
- `치료재건 메인.png`, `치료재건 세컨페이지.png`
- `1. 트라우마.png`, `2. 번 트리트먼트.png`, `3. 스킨 튜머.png`, `4. 피디애트릭.jpg`

**이 목록에 없는 이미지 경로는 사용 금지** — 없는 이미지는 CSS 그라디언트로 처리.

## 코드 아키텍처: 파일 완전 자급자족 구조

**공유 CSS/JS 파일이 없다.** 모든 스타일, GNB, 스크립트는 각 HTML 파일 내 `<style>`, `<script>` 블록에 인라인으로 존재한다.

공통 요소(GNB, 색상 변수, 푸터 등)를 수정할 때는 **영향받는 모든 파일을 각각 수정**해야 한다. 다수 파일을 한 번에 고칠 때는 `sed -i ''` 루프를 사용한다:

```bash
for f in about.html booking.html breast.html burn.html community.html consultation.html \
  cosmetic.html doctor.html eye.html fat.html index.html lifting.html male.html \
  medical.html news.html nose.html notice.html other.html pediatric.html petit.html \
  reconstruction.html tour.html trauma.html; do
  sed -i '' 's/OLD/NEW/g' "$f"
done
```

### GNB 구조 (모든 페이지 공통)

```
[로고] | 소개 | 의료진소개 | 병원둘러보기 | 진료안내▼ | 커뮤니티▼ | [상담예약]
```

- **드롭다운**: CSS hover로만 구현 (JS 없음)
- **모바일**: 햄버거 → 풀스크린 오버레이
- **현재 페이지 표시**: 해당 항목에 `.current` 클래스

### JS 패턴

- **진료 상세 페이지**: `<script>` 블록 없음. FAQ 아코디언은 `onclick="this.parentElement.classList.toggle('active')"` 방식
- **index.html**: IIFE — 헤더 스크롤, 모바일 메뉴, Intersection Observer fade-up, 스플릿 히어로 터치
- **cosmetic.html / medical.html**: IIFE — 자동 슬라이드쇼(3초 전환), 카테고리 스크롤 drag-to-scroll, 전후변화 스크롤, 플로팅 CTA 토글
- **about.html**: IIFE — 카드 stagger 애니메이션
- **tour.html**: 터치 스와이프 슬라이더 (화살표 + dot 인디케이터)

### 허브 페이지 섹션 구성 (cosmetic.html / medical.html)

**cosmetic.html 섹션 순서:**
1. 히어로 슬라이드쇼 — 눈/코/리프팅/가슴 4슬라이드 자동전환
2. 카테고리 스크롤 (`.categories-scroll-section`) — 8개 항목 좌우 스크롤
3. 전후변화 (`.before-after-section`) — 4카드 좌우 스크롤
4. Why Choose Us (`.trust-section`)
5. 의료진 소개
6. CTA 섹션

**medical.html 섹션 순서:**
1. 프로모션 배너 스트립 (응급/조직검사/소아진료 3개)
2. 히어로 슬라이드쇼 — 상처외상/화상/피부종양/소아진료 4슬라이드
3. 카테고리 스크롤 — 4개 항목 좌우 스크롤
4. 안전 시스템 섹션
5. 의료진 소개
6. CTA 섹션

### 좌우 스크롤 트랙 정렬 패턴 (중요)

Chrome에서 `scroll-snap-type`을 가진 flex 컨테이너에 `padding-left`를 주면 브라우저가 자동으로 첫 카드에 스냅하여 padding이 무효화되는 버그가 있다. 이를 회피하기 위해 `::before` 가상 요소를 좌측 스페이서로 사용:

```css
.categories-scroll-track {
  display: flex;
  gap: 16px;
  overflow-x: auto;
  padding: 8px 40px 16px 0;  /* padding-left 없음 */
}
.categories-scroll-track::before {
  content: '';
  flex-shrink: 0;
  /* gap(16px)만큼 뺀 값: 다른 섹션 콘텐츠 좌측과 정렬 */
  width: max(16px, calc((100vw - 1360px) / 2 + 16px));
}
```

- `gap` 값이 spacer와 첫 카드 사이에도 적용되므로 `::before` width에서 gap을 차감해야 다른 섹션과 정렬이 맞음
- `ba-scroll-track`(gap: 20px)의 spacer 상수는 12px: `max(12px, calc((100vw - 1360px) / 2 + 12px))`
- drag-to-scroll JS는 `e.clientX` + `document` 레벨 이벤트 리스너 사용 (트랙 밖에서 마우스를 놓아도 작동)

### 모바일 주의사항

**CSS 캐스케이드 순서**: `.mobile-cta { display: none }` 기본 정의는 반드시 `@media` 블록보다 **앞에** 선언해야 한다. 기존 페이지 중 순서가 뒤바뀐 파일은 `@media` 안에 `!important`가 붙어 있다. 새 페이지 작성 시 앞에 선언하면 `!important` 불필요.

- **하단 고정 CTA 바** (`class="mobile-cta"`): 전화/카카오/네이버예약 버튼 3개. `padding-bottom: calc(10px + env(safe-area-inset-bottom))`으로 아이폰 노치 대응
- **푸터 퀵링크**: 오시는 길 / 진료 시간 / 카카오톡 상담 3개
- **브레이크포인트**: `1024px` (태블릿), `768px` (모바일)

### index.html 스플릿 히어로

- **PC**: 마우스 hover 시 패널 1.6:0.4 비율로 확장, mouseleave 시 원위치
- **모바일 터치**: `touchstart`로 Y좌표 기록 → `touchend`에서 이동 거리 체크. dy/dx > 12px이면 스크롤로 판단해 패널 활성화 무시. 탭으로 판정되면 1차 탭 → 패널 확장, 2.2초 자동 축소. 2차 탭(이미 active) → 링크 이동.
- **iOS Safari**: `height: 100svh`
- **패널 링크**: 좌측(spLeft) → `cosmetic.html`, 우측(spRight) → `medical.html`
- **`.sp-seam::before`**: 패널 구분선 — `display: none` 처리됨 (제거 상태 유지)

### cosmetic.html 히어로 레이아웃 주의

`.hero-banner-inner`에 `width: 100%` 필수 — 없으면 flex child가 content 너비로 수축해 텍스트가 좌측에 고정되지 않음. `font-size: clamp(36px, 4.2vw, 54px)` — 더 큰 값은 컨테이너 내에서 3줄 깨짐 발생.

## CSS 색상 시스템

모든 페이지(dashboard.html 제외)에서 동일한 CSS 변수 (nanaprs.com 팔레트 기준):

```css
:root {
  --primary: #42c0bf;       /* 메인 컬러 (teal/cyan) */
  --primary-light: #63c3c2;
  --primary-dark: #2da8a7;
  --wine: #232942;          /* 딥 다크네이비 (미용성형 히어로 배경) */
  --navy: #0d1f2e;          /* 다크 네이비 (치료재건 배경) */
  --navy-mid: #303947;
  --accent: #b2e4e4;        /* 서브 컬러 (라이트 teal) */
  --accent-light: #d2f0f0;
  --bg-off: #f0fafa;        /* 섹션 배경 (teal 오프화이트) */
  --text-dark: #1A1A1A;
  --text-mid: #555;
  --text-light: #888;
  --white: #FFFFFF;
}
```

일부 페이지는 위 변수 외에 `--bg-light: #f0fafa`, `--bg-warm: #d2f0f0` 같은 로컬 변수를 추가로 정의한다.

색상 변경 시 CSS 변수 외에 파일 내 하드코딩된 `rgba(...)`, 인라인 `style=""` 값도 grep으로 확인 필요:

```bash
grep -rn "OLD_HEX\|rgba(OLD_R,OLD_G,OLD_B" *.html
```

## dashboard.html 특이사항

- **CDN 의존**: Tailwind CSS, Google Fonts — 인터넷 필수
- **테마**: `<html class="dark">` 기본값, `html.light-mode` 토글, `localStorage('dashboardTheme')` 저장
- Tailwind 클래스명의 `/`는 CSS 셀렉터에서 백슬래시 이스케이프 필요 (`text-white\/60`)
- 총 페이지 수는 **23페이지** (홈+허브 3, 기관소개 3, 미용성형 8, 치료재건 4, 커뮤니티 5)

## 레이아웃 패턴

- 최대 너비: `1280px` / 섹션 패딩: 상하 `100px`, 좌우 `40px`
- 폰트: Pretendard (CDN) → `'Apple SD Gothic Neo'` → `'Malgun Gothic'`

## 브랜드 & 콘텐츠 규칙

- **핵심 메시지**: "대학병원의 안전함에 섬세함을 더하다"
- **의료진 호칭**: "전문의" 또는 "과장" 사용. **"원장" 사용 금지** (종합병원 진료과 형태)
- **담당의**: 신정환 과장 (성형외과 전문의, 가톨릭중앙의료원 출신)
- **CTA 4종 (순서 고정)**: 전화 상담(`tel:042-000-0000`) → 진료 예약(`booking.html`) → 카카오 상담 → 네이버 예약
- **플로팅 CTA** (데스크탑 우측): 전화 상담 / 카톡 상담 / 네이버 예약
- **미용성형 컬러**: `--primary` / **치료재건 컬러**: `--navy-mid`
- **의료법 준수**: "최고", "완벽한", "100% 만족" 등 과장 표현 금지

## 콘텐츠 전략 참고

`reference/content_strategy.md` — 경쟁사 벤치마킹, 페이지별 카피 브리프, 차별화 포지셔닝. 카피 수정 시 반드시 참고.
