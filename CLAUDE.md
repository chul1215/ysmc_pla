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

공통 요소(GNB, 색상 변수, 푸터 등)를 수정할 때는 **영향받는 모든 파일을 각각 수정**해야 한다.

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
- **cosmetic.html, medical.html, about.html**: IIFE — 카드 stagger 애니메이션
- **tour.html**: 터치 스와이프 슬라이더 (화살표 + dot 인디케이터)

### 모바일 주의사항

**CSS 캐스케이드 순서**: `.mobile-cta { display: none }` 기본 정의는 반드시 `@media (max-width: 768px) { .mobile-cta { display: block } }` 오버라이드보다 **앞에** 선언해야 한다. 순서가 뒤바뀌면 모바일에서도 CTA가 표시되지 않음.

- **하단 고정 CTA 바** (`class="mobile-cta"`): 전화/카카오 버튼 2개. `padding-bottom: calc(10px + env(safe-area-inset-bottom))`으로 아이폰 노치 대응
- **푸터 퀵링크**: 오시는 길 / 진료 시간 / 카카오톡 상담 3개. **네이버 예약 없음**
- **브레이크포인트**: `1024px` (태블릿), `768px` (모바일)

### index.html 스플릿 히어로

- **모바일 터치**: 1차 탭 → 패널 확장, 2차 탭 → 링크 이동, 2.2초 자동 축소
- **iOS Safari**: `height: 100svh`
- **패널 링크**: 좌측 → `cosmetic.html`, 우측 → `medical.html`

### cosmetic.html 히어로 레이아웃 주의

`.hero-banner-inner`에 `width: 100%` 필수 — 없으면 flex child가 content 너비로 수축해 텍스트가 좌측에 고정되지 않음. `font-size: clamp(36px, 4.2vw, 54px)` — 더 큰 값은 컨테이너 내에서 3줄 깨짐 발생.

## CSS 색상 시스템

모든 페이지(dashboard.html 제외)에서 동일한 CSS 변수:

```css
:root {
  --primary: #6abea7;       /* 메인 컬러 (민트/틸) */
  --primary-light: #7cffc4;
  --primary-dark: #4d9e8a;
  --wine: #1a3d38;          /* 딥 틸 (미용성형 히어로 배경) */
  --navy: #0a1828;          /* 다크 네이비 (치료재건 배경) */
  --navy-mid: #1a3a5c;
  --accent: #c0e8e4;        /* 서브 컬러 (라이트 민트) */
  --accent-light: #daf2f0;
  --bg-off: #f0f8f7;        /* 섹션 배경 (민트 오프화이트) */
  --text-dark: #1A1A1A;
  --text-mid: #555;
  --text-light: #888;
  --white: #FFFFFF;
}
```

색상 변경 시 CSS 변수 외에 파일 내 하드코딩된 `rgba(...)` 값도 grep으로 확인 필요.

## dashboard.html 특이사항

- **CDN 의존**: Tailwind CSS, Google Fonts — 인터넷 필수
- **테마**: `<html class="dark">` 기본값, `html.light-mode` 토글, `localStorage('dashboardTheme')` 저장
- Tailwind 클래스명의 `/`는 CSS 셀렉터에서 백슬래시 이스케이프 필요 (`text-white\/60`)

## 레이아웃 패턴

- 최대 너비: `1280px` / 섹션 패딩: 상하 `100px`, 좌우 `40px`
- 폰트: Pretendard (CDN) → `'Apple SD Gothic Neo'` → `'Malgun Gothic'`

## 브랜드 & 콘텐츠 규칙

- **핵심 메시지**: "대학병원의 안전함에 섬세함을 더하다"
- **의료진 호칭**: "전문의" 또는 "과장" 사용. **"원장" 사용 금지** (종합병원 진료과 형태)
- **담당의**: 신정환 과장 (성형외과 전문의, 가톨릭중앙의료원 출신)
- **CTA 3종**: 상담 예약(`booking.html`) / 전화(`tel:042-000-0000`) / 카카오톡
- **미용성형 컬러**: `--primary` / **치료재건 컬러**: `--navy-mid`
- **의료법 준수**: "최고", "완벽한", "100% 만족" 등 과장 표현 금지

## 콘텐츠 전략 참고

`reference/content_strategy.md` — 경쟁사 벤치마킹, 페이지별 카피 브리프, 차별화 포지셔닝. 카피 수정 시 반드시 참고.
