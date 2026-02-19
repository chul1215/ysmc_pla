# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

유성선병원 성형외과 신설 부서 홍보용 정적 웹사이트. 빌드 시스템이 없으며 순수 HTML/CSS/JS로 구성된다.

- **언어**: 한국어 (lang="ko")
- **스택**: 순수 HTML5 + CSS3 + Vanilla JS (프레임워크/패키지 없음)
- **서버**: 정적 파일 서버 직접 업로드 (빌드 불필요)

## 파일 구조

```
ysmc_pla/
├── index.html          ← 메인 랜딩 페이지
├── eye.html            ← 눈 센터
├── lifting.html        ← 리프팅
├── petit.html          ← 쁘띠/스킨
├── trauma.html         ← 외상
├── reconstruction.html ← 재건·종괴
├── dashboard.html      ← 관리자 대시보드 (Tailwind CSS)
├── images/             ← 이미지 파일
├── plan/               ← 기획서 및 마케팅 전략 문서
└── reference/          ← 참고 자료 및 기획 문서
```

## 배포 워크플로우

GitHub Pages를 통해 자동 배포된다:

- **배포 URL**: `https://chul1215.github.io/ysmc_pla/`
- **설정**: GitHub 저장소의 Settings → Pages → Source: `main` branch, `/ (root)` folder
- 변경사항을 `main` 브랜치에 푸시하면 자동으로 배포됨

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
}
```

RGB 변환값 (rgba 하드코딩 시 사용):
- `#cd4631` → `205, 70, 49`
- `#f8f2dc` → `248, 242, 220`

색상 변경 시 CSS 변수 외에 파일 내 하드코딩된 `rgba(...)` 값도 별도로 확인해야 한다 (grep으로 검색 필요).

## dashboard.html 특이사항

다른 페이지와 달리 Tailwind CSS를 사용하며, 색상은 Tailwind config와 `hsla()` 메시 그라디언트로 정의된다. CSS 변수 블록이 없으므로 색상 변경 시 별도로 처리해야 한다.

## 레이아웃 패턴

- 최대 너비: `1280px` (모든 섹션 공통)
- 섹션 패딩: 상하 `100px`, 좌우 `40px`
- 반응형 브레이크포인트: `1024px`, `768px`
- 폰트: `'Pretendard'`, `'Apple SD Gothic Neo'`, `'Malgun Gothic'`
- 스크롤 애니메이션: `Intersection Observer API` + `.fade-up` 클래스

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

## 브랜드 포지셔닝

- 핵심 메시지: "대학병원의 안전함에 섬세함을 더하다"
- 주요 진료축: 눈, 리프팅, 쁘띠/스킨, 외상, 재건·종괴
- 담당의: 신정환 과장 (가톨릭중앙의료원 출신)
- CTA 3종: 상담 예약하기 / 전화 문의 / 카카오톡 문의
