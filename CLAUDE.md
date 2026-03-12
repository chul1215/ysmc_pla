# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

유성선병원 성형외과 신설 부서 홍보용 정적 웹사이트. 빌드 시스템이 없으며 순수 HTML/CSS/JS로 구성된다.

- **언어**: 한국어 (lang="ko")
- **스택**: 순수 HTML5 + CSS3 + Vanilla JS (프레임워크/패키지 없음)
- **서버**: 정적 파일 서버 직접 업로드 (빌드 불필요)

## 로컬 미리보기

빌드 없이 브라우저에서 직접 열거나, 상대경로 이슈 방지를 위해 로컬 서버 사용:

```bash
python3 -m http.server 8080
# → http://localhost:8080
```

## 파일 구조

```
ysmc_pla/
├── index.html          ← 메인 랜딩 페이지 (시안 1, 시안 스위처 포함)
├── index2.html         ← 메인 랜딩 페이지 (시안 2, 스플릿 히어로 디자인)
├── eye.html            ← 눈 센터
├── lifting.html        ← 리프팅
├── petit.html          ← 쁘띠/스킨
├── trauma.html         ← 외상
├── reconstruction.html ← 재건·종괴
├── dashboard.html      ← 관리자 대시보드 (Tailwind CSS)
├── images/             ← 이미지 파일 (상대경로로 참조)
├── briefing/           ← 브리핑 자료
├── plan/               ← 기획서 및 마케팅 전략 문서
└── reference/          ← 참고 자료
```

## 배포 워크플로우

GitHub Pages를 통해 자동 배포된다:

- **배포 URL**: `https://chul1215.github.io/ysmc_pla/`
- **설정**: GitHub 저장소 Settings → Pages → Source: `main` branch, `/ (root)` folder
- `main` 브랜치에 푸시하면 자동 배포됨
- README에 언급된 `deploy/` 폴더는 현재 미사용 (루트에서 직접 배포)

## 코드 아키텍처: 파일 완전 자급자족 구조

**공유 CSS/JS 파일이 없다.** 모든 스타일과 스크립트는 각 HTML 파일 내 `<style>`, `<script>` 블록에 인라인으로 존재한다.

따라서 공통 요소(헤더, 네비게이션, 색상 변수 등)를 수정할 때는 **영향받는 모든 파일을 각각 수정**해야 한다.

### 상세 페이지 (eye, lifting, petit, trauma, reconstruction)

- `<script>` 블록 없음 — 모든 인터랙션은 CSS + inline `onclick` 처리
- FAQ 아코디언: `onclick="this.parentElement.classList.toggle('active')"` 방식
- 스크롤 fade-up 애니메이션 없음
- sticky mobile CTA 바 없음

### index.html (시안 1) 추가 기능

- **mobile-cta**: 모바일 전용 하단 고정 CTA 바 (전화/카카오톡 버튼)
- **Intersection Observer + `.fade-up`**: 스크롤 진입 시 애니메이션
- **draft-switcher**: 하단 고정 시안 전환 버튼 (index.html ↔ index2.html)
- `<script>` 블록으로 헤더 스크롤 축소, 모바일 메뉴, FAQ, 스크롤 애니메이션 구현

## CSS 색상 시스템

모든 페이지(dashboard.html 제외)는 동일한 CSS 변수 블록을 사용한다:

```css
:root {
  --primary: #cd4631;       /* 메인 컬러 (테라코타 레드) */
  --primary-light: #d96858;
  --primary-dark: #a33828;
  --accent: #f8f2dc;        /* 서브 컬러 (웜 크림) */
  --accent-light: #faf6e8;
  --bg-light: #fdf8f0;
  --bg-warm: #faf5e6;
  --text-dark: #1A1A1A;
  --text-mid: #555;
  --text-light: #888;
  --shadow: 0 4px 24px rgba(0,0,0,0.08);
  --shadow-lg: 0 8px 40px rgba(0,0,0,0.12);
}
```

RGB 변환값 (rgba 하드코딩 시 사용):
- `#cd4631` → `205, 70, 49`
- `#f8f2dc` → `248, 242, 220`

색상 변경 시 CSS 변수 외에 파일 내 하드코딩된 `rgba(...)` 값도 grep으로 확인해야 한다.

## dashboard.html 특이사항

다른 페이지와 달리 Tailwind CSS (CDN)를 사용하며, 색상은 Tailwind config와 `hsla()` 메시 그라디언트로 정의된다. CSS 변수 블록이 없으므로 색상 변경 시 별도로 처리해야 한다.

- **테마 토글**: `<html class="dark">` 기본값. 헤더 버튼이 `html.light-mode` 클래스를 토글하며 `localStorage('dashboardTheme')`에 저장한다.
- **라이트 모드 CSS**: `<style>` 내 `html.light-mode ...` 셀렉터로 `.mesh-gradient`, `.glass-panel`, `text-white/XX`, `bg-white/XX`, `border-white/XX` 등을 일괄 오버라이드. Tailwind utility 클래스명에 `/`가 포함되어 CSS 셀렉터에서 백슬래시 이스케이프(`text-white\/60`) 필요.
- **커스텀 클래스**: `.glass-panel` / `.mesh-gradient` — Tailwind 유틸리티가 아닌 인라인 `<style>` 정의
- **레이아웃**: `overflow-hidden h-screen` 고정 높이 앱 레이아웃. 모바일에서는 햄버거 드로어 사이드바 사용.

## 레이아웃 패턴 (상세 페이지)

- 최대 너비: `1280px` (모든 섹션 공통)
- 섹션 패딩: 상하 `100px`, 좌우 `40px`
- 반응형 브레이크포인트: `1024px`, `768px`
- 폰트: `'Pretendard'`, `'Apple SD Gothic Neo'`, `'Malgun Gothic'`

## 페이지 공통 구조 (상세 페이지)

각 상세 페이지는 동일한 섹션 순서를 따른다:
1. 고정 헤더/GNB 네비게이션
2. 히어로 섹션
3. 수술 원칙 섹션
4. 특장점 카드 섹션
5. 수술 유형 그리드
6. FAQ 아코디언
7. CTA 섹션
8. 푸터

## index2.html 특이사항 (시안 2)

스플릿 히어로 패널 방식으로, index.html과 구조가 다르다:

- **스플릿 패널**: `flex` 비율 transition으로 패널 확장 (`flex: 1` → `flex: 1.6`). `clip-path` 미사용.
- **대각선 심(seam)**: 0-width flex item + `::before { skewX(-6deg) }`으로 구현
- **iOS Safari 대응**: `height: 100svh` (svh 단위 필수)
- **모바일 column 전환**: `flex-direction: column` + 동일 flex transition 재사용
- **모바일 콘텐츠**: hover 없는 환경에서 `opacity: 1 !important` 오버라이드 필요
- **JS**: IIFE 패턴. 모바일 터치 시 1차 탭→패널 확장, 2차 탭→링크 이동, 2.2초 자동 축소
- **시안 스위처**: 두 파일 모두 하단 고정 버튼(`draft-switcher`)으로 상호 전환 가능

## 브랜드 포지셔닝

- 핵심 메시지: "대학병원의 안전함에 섬세함을 더하다"
- 주요 진료축: 눈, 리프팅, 쁘띠/스킨, 외상, 재건·종괴
- 담당의: 신정환 과장 (가톨릭중앙의료원 출신)
- CTA 3종: 상담 예약하기 / 전화 문의 / 카카오톡 문의
