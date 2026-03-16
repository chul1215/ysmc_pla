# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

유성선병원 성형외과 신설 부서 홍보용 정적 웹사이트. 빌드 시스템이 없으며 순수 HTML/CSS/JS로 구성된다.

- **언어**: 한국어 (lang="ko")
- **스택**: 순수 HTML5 + CSS3 + Vanilla JS (프레임워크/패키지 없음)
- **배포**: GitHub Pages (`https://chul1215.github.io/ysmc_pla/`) — main 브랜치 푸시 시 자동 배포
- **로컬 실행**: 파일 더블클릭으로 직접 열기 가능 (Pretendard CDN, 상대경로 모두 정상 작동)

```bash
# 선택적 로컬 서버 (필요 시)
python3 -m http.server 8080
```

## 전체 파일 구조 (26개 HTML)

```
index.html              ← 메인 홈 (스플릿 히어로, 최종 확정)
index2.html             ← 구 시안2 보관용 (현재 미사용)
dashboard.html          ← 관리자 대시보드 (Tailwind CSS, 별도 아키텍처)

# 허브 페이지
cosmetic.html           ← 미용·성형 전체 허브 (8개 카테고리)
medical.html            ← 치료·재건 전체 허브 (4개 카테고리)

# 기관 소개
about.html / doctor.html / features.html / tour.html / academic.html

# 미용·성형 상세 (8개)
eye.html / nose.html / lifting.html / male.html
fat.html / breast.html / other.html / petit.html

# 치료·재건 상세 (4개)
trauma.html / burn.html / reconstruction.html / pediatric.html

# 커뮤니티 (5개)
community.html / consultation.html / booking.html / news.html / notice.html

images/         ← 실제 이미지 파일 (아래 목록 참조)
reference/      ← 마케팅 전략 문서 (content_strategy.md, microsite_cf.md)
briefing/       ← 브리핑 자료
plan/           ← 기획서
```

### 사용 가능한 이미지 (`images/` 폴더)
`eye-correction.png`, `lifting.jpg`, `petit-skin.png`, `surgery-room.jpg`, `shin_profile.jpg`
및 눈성형 관련 시술 이미지 다수 (매몰법, 절개법, 앞트임 등). **이 목록에 없는 이미지 경로는 사용 금지** — 없는 이미지는 CSS 그라디언트로 처리.

## 코드 아키텍처: 파일 완전 자급자족 구조

**공유 CSS/JS 파일이 없다.** 모든 스타일, GNB, 스크립트는 각 HTML 파일 내 `<style>`, `<script>` 블록에 인라인으로 존재한다.

공통 요소(GNB, 색상 변수, 푸터 등)를 수정할 때는 **영향받는 모든 파일을 각각 수정**해야 한다.

### GNB 구조 (모든 페이지 공통)

```
[로고] | 소개 | 의료진소개 | 성형외과특징 | 병원둘러보기 | 진료안내▼ | 학술활동 | 커뮤니티▼ | [상담예약]
```

- **진료안내 드롭다운**: 2컬럼 메가메뉴 (미용·성형 8개 / 치료·재건 4개)
- **커뮤니티 드롭다운**: 1컬럼 (온라인상담, 카카오톡상담, 진료예약, 언론보도, 공지사항)
- **드롭다운 방식**: CSS hover로만 구현 (JS 없음)
- **모바일**: 햄버거 → 풀스크린 오버레이, 계층 구조 유지
- **현재 페이지 표시**: 해당 항목에 `.current` 클래스

### 상세 페이지 JS 규칙

- **상세 페이지 (eye, lifting 등 진료 페이지)**: `<script>` 블록 없음 — 모든 인터랙션은 CSS + inline `onclick`
- **FAQ 아코디언**: `onclick="this.parentElement.classList.toggle('active')"` 방식
- **index.html**: IIFE 패턴 `<script>` 블록 — 헤더 스크롤, 모바일 메뉴, Intersection Observer fade-up 포함

### index.html 스플릿 히어로 특이사항

- **스플릿 패널**: `flex` 비율 transition (`flex: 1` → `flex: 1.6`), clip-path 미사용
- **대각선 심(seam)**: 0-width flex item + `::before { skewX(-6deg) }`
- **iOS Safari 대응**: `height: 100svh`
- **패널 클릭**: 좌측 → `cosmetic.html`, 우측 → `medical.html` 이동
- **모바일 터치**: 1차 탭 → 패널 확장, 2차 탭 → 링크 이동, 2.2초 자동 축소

## CSS 색상 시스템

모든 페이지(dashboard.html 제외)는 동일한 CSS 변수 블록을 사용한다:

```css
:root {
  --primary: #cd4631;       /* 메인 컬러 (테라코타 레드) */
  --primary-light: #d96858;
  --primary-dark: #a33828;
  --wine: #3d0f09;          /* 딥 와인 (미용성형 히어로 배경) */
  --navy: #0a1828;          /* 다크 네이비 (치료재건 배경, doctor 섹션) */
  --navy-mid: #1a3a5c;      /* 미드 네이비 */
  --accent: #f8f2dc;        /* 서브 컬러 (웜 크림) */
  --accent-light: #faf6e8;
  --bg-off: #f5f3ef;        /* 섹션 배경 (오프화이트) */
  --text-dark: #1A1A1A;
  --text-mid: #555;
  --text-light: #888;
}
```

- `--primary` (`#cd4631`) → rgba: `205, 70, 49`
- `--accent` (`#f8f2dc`) → rgba: `248, 242, 220`
- 색상 변경 시 CSS 변수 외에 파일 내 하드코딩된 `rgba(...)` 값도 grep으로 확인 필요

## dashboard.html 특이사항

다른 페이지와 완전히 별개의 아키텍처:

- **CDN 의존**: Tailwind CSS, Google Fonts (Inter, Noto Sans KR, Material Icons) — 인터넷 필수
- **테마 토글**: `<html class="dark">` 기본값. `html.light-mode` 클래스 토글, `localStorage('dashboardTheme')` 저장
- **라이트 모드 CSS**: `html.light-mode ...` 셀렉터. Tailwind 클래스명의 `/`는 CSS 셀렉터에서 백슬래시 이스케이프 필요 (`text-white\/60`)
- **커스텀 클래스**: `.glass-panel`, `.mesh-gradient` — `<style>` 블록 내 정의
- **레이아웃**: `overflow-hidden h-screen` 고정 높이. 모바일 햄버거 드로어

## 레이아웃 패턴

- 최대 너비: `1280px`
- 섹션 패딩: 상하 `100px`, 좌우 `40px`
- 반응형 브레이크포인트: `1024px`, `768px`
- 폰트: Pretendard (CDN 로드) → `'Apple SD Gothic Neo'` → `'Malgun Gothic'`

## 브랜드 & 콘텐츠 규칙

- **핵심 메시지**: "대학병원의 안전함에 섬세함을 더하다"
- **의료진 호칭**: 반드시 "전문의" 또는 "과장" 사용. **"원장"은 사용 금지** (종합병원 진료과 형태)
- **담당의**: 신정환 과장 (성형외과 전문의, 가톨릭중앙의료원 출신)
- **SNS 섹션 설명**: "유성선병원 성형외과가 직접 전하는 의료 정보와 상담 콘텐츠"
- **CTA 3종**: 상담 예약(`booking.html`) / 전화 문의(`tel:042-000-0000`) / 카카오톡 문의
- **미용성형 컬러 포인트**: `--primary` 테라코타 계열
- **치료재건 컬러 포인트**: `--navy-mid` 네이비 계열
- **의료법 준수**: "최고", "완벽한", "100% 만족" 등 과장 표현 사용 금지

## 콘텐츠 전략 참고

`reference/content_strategy.md` — 경쟁사(체리성형외과, 나나성형외과) 벤치마킹 분석, 각 페이지별 카피 브리프, 차별화 포지셔닝 5가지 포함. 카피 수정 시 반드시 참고.
