# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

선메디컬센터 유성선병원 성형외과 신설 부서 홍보용 정적 웹사이트. 빌드 시스템이 없으며 순수 HTML/CSS/JS로 구성된다.

- **브랜드명**: 선메디컬센터 유성선병원 성형외과
- **언어**: 한국어 (lang="ko")
- **스택**: 순수 HTML5 + CSS3 + Vanilla JS (프레임워크/패키지 없음)
- **배포**: GitHub Pages (`https://chul1215.github.io/ysmc_pla/`) — main 브랜치 푸시 시 자동 배포
- **로컬 서버**: `python3 -m http.server 8080`
- **개발 환경**: cmux (tmux 기반 통합 개발환경) — 내장 브라우저 사용

## 테스트 및 확인 절차 (cmux 환경)

마이크로페이지(HTML 파일) 관련 작업 시 **반드시 cmux 내장 브라우저로 직접 확인**한다.

1. 로컬 서버가 실행 중인지 확인: `python3 -m http.server 8080`
2. cmux 내장 브라우저에서 `http://localhost:8080/<파일명>.html` 접속
3. 수정 후 브라우저 새로고침으로 변경사항 즉시 검증
4. 모바일 레이아웃 확인: 브라우저 창 크기를 768px 이하로 조정

> **Playwright MCP**도 사용 가능하나, cmux 내장 브라우저가 이미 열려 있을 경우 그쪽을 우선 활용할 것.

## 파일 구성

- `index.html` — 메인 홈 (스플릿 히어로)
- `admin.html` — 운영 관리 페이지 "유성선병원 성형외과 MASTER PAGE" (Tailwind CSS, **별도 아키텍처**, GNB 없음)
- `dashboard.html` — 마케팅 대시보드 (Tailwind CSS, **별도 아키텍처**)
- `cosmetic.html` / `medical.html` — 진료 허브 페이지 (각 카테고리 진입점)
- 미용·성형 상세 7개 (+1 비활성): `eye`, `nose`, `lifting`, `fat`, `breast`, `other`, `petit` / `male` (GNB 미노출, 직접 접근만 가능)
- 치료·재건 상세 5개: `trauma`, `burn`, `scar`, `reconstruction`, `fracture` (소아진료 `pediatric.html`은 2026-04-17 삭제, 내용은 trauma/burn으로 분산)
- 기관 소개: `about`, `doctor`, `tour`
- 커뮤니티: `community`, `consultation`, `booking`, `notice`, `reviews`
  - `reviews.html` — 수술후기 목록 페이지. `localStorage: ysmc_reviews`에서 공개 후기(`visible !== false`)를 동적 로딩. 카테고리 필터 탭, 카드 그리드(3→2→1열), 클릭 시 상세 모달. admin에서 등록한 후기가 자동 반영됨.
  - `news.html` — 파일은 존재하나 **모든 GNB/모바일 nav에서 링크 제거됨** (언론보도 게시판 비활성화)
- `_archive/` — 미사용 보관
- `delivery/` — 퍼블리싱 전달용 스냅샷. 커밋된 하위 폴더는 누적 이력으로 유지:
  - `20260417_3rd/` (3차, 최신) — 공개 HTML 24 + `변경사항_20260417_3rd.md` + **신규/변경 이미지만** 상대경로 그대로 동봉(`images/medical-hero.jpg`, `images/images2/medical/scar/`, `images/images2/medical/fracture/`)
  - `20260417/` (2차)·`20260417_ysmc_update2.zip` (2차 zip)은 **git untracked** 로컬 보관 — 사용자 지시로 커밋 제외
  - 신규 폴더 만들 때 이전 폴더 전체 복제하지 말고, 이전 배포 이후 변경·신규된 파일만 복사 + 변경사항 md 작성. PNG도 포함되도록 `.gitignore`에 `!delivery/**/*.png` 예외 이미 적용됨

### 사용 가능한 이미지 (`images/` 폴더)

루트: `medical-hero.jpg` (치료재건 대표 히어로 — index·fracture·scar·reconstruction 4개 페이지가 공유. Gemini 2.5 Flash Image 생성), `lifting.jpg`, `shin_profile.jpg`, `eye-correction.png`, `petit-skin.png`, `doctor_shin.png` (의료진 실제 사진). `surgery-room.jpg`는 2026-04-17 `medical-hero.jpg`로 교체되어 **현재 미참조** (로컬엔 보존).

눈성형 시술 이미지 (eye.html 전용): `매몰법_den.png`, `절개법_dei.png`, `부분절개법_dep.png`, `앞트임_epi.png`, `눈매교정.png`, `눈_나노지방_nano.png`, `위트임.png`, `듀얼트임.png`, `하안검.jpg`, `지방재배치.jpg`, `눈썹밑거상_SB.png`, `기능코.jpg`, `콧볼_인중축소.jpg`, `무보형물_귀연골.jpg`, `무보형물_비중격.jpg`

`images/mc-image/미용성형/` — 카테고리 카드용 실사진 8종 + 메인/세컨페이지 이미지:
- `미용성형 메인.jpg`, `미용성형 세컨페이지.jpg`
- `1. 아이 센터.png`, `2. 라이노플래스티.jpg`, `3. 리프팅 안티에이징.jpg`, `4. 메일 코스매틱.png`, `5. 팻 컨투어링.jpg`, `6. 브레스트 써저리.jpg`, `7. 아더 써저리.jpg`, `8. 쁘띠스킨.jpg`

`images/mc-image/치료재건/` — 카테고리 카드용 실사진 4종 + 메인/세컨페이지 이미지:
- `치료재건 메인.png`, `치료재건 세컨페이드.png`
- `1. 트라우마.png`, `2. 번 트리트먼트.png`, `3. 스킨 튜머.png`, `4. 피디애트릭.jpg`

`images/card-image/` — 섹션 카드용 실사진 (URL-safe 경로):
- `values/` → `safety-first.jpg`, `precise-surgery.jpg`, `patient-care.jpg`
- `safety-main/` → `emergency-24h.jpg`, `anesthesia.jpg`, `multidisciplinary.jpg`
- `safety-medical/` → `emergency-system.jpg`, `surgical-anesthesia.jpg`, `rehabilitation.jpg`
- `sns/` → `blepharoptosis.png`, `face-lump.png`, `hospital-plastic.jpg`

`images/images2/cosmetic/{page}/` — 미용성형 상세 페이지용 시술·특징 카드 이미지 (URL-safe):
- `breast/` → `safety-design`, `breast-augmentation`, `breast-reduction`, `inverted-nipple`, `nipple-surgery`, `anesthesia-specialist`, `body-ratio`, `hospitalization`
- `other/` → `careful-planning`, `earlobe-repair`, `keloid-treatment`, `ear-correction`, `scar-surgery`, `earlobe-augmentation`, `piercing-repair`, `specialist-surgeon`, `keloid-protocol`, `hospital-test`
- `male/` → `male-approach`, `male-eye`, `male-nose`, `gynecomastia`, `male-liposuction`, `male-contour`, `male-petit`, `male-aesthetic`, `quick-recovery`, `hospital-anesthesia`
- `lifting/` → `safe-lifting`, `ulthera`, `thermage`, `facelift`, `complex-lifting`, `skin-analysis`, `custom-lifting`, `natural-recovery`
- `petit/` → `honest-consultation`, `botox`, `filler`, `skin-booster`, `laser`, `specialist-procedure`, `genuine-product`, `natural-result`
- `fat/` → `volume-balance`, `face-fat-graft`, `face-liposuction`, `body-liposuction`, `nano-fat`, `fat-relocation`, `lipo-combo`, `precise-volume`, `hospital-anesthesia`, `realistic-goal`
- `nose/` → `nose-design`, `nose-bridge`, `nose-tip`, `nostril-philtrum`, `nose-revision`, `functional-nose`, `hump-nose`, `hospital-safety`, `autologous-cartilage`, `face-ratio`
- `eye/` → `hospital-safety`, `specialist-surgeon`, `custom-design`, `under-eye-fat`

`images/images2/medical/{page}/` — 치료재건 상세 페이지용 시술·특징 카드 이미지 (URL-safe):
- `trauma/` → `emergency-consult`, `specialist-suture`, `scar-laser`
- `pediatric/` → `pediatric-approach`, `pediatric-suture`, `pediatric-mole`, `pediatric-burn`, `pediatric-vascular`, `pediatric-ear`, `pediatric-scar`, `pediatric-anesthesia`, `growth-plan`, `guardian-care` (pediatric.html은 삭제됐지만 일부 이미지는 trauma/burn에서 재활용 가능)
- `reconstruction/` → `accurate-diagnosis`, `diagnosis-system`, `specialist-surgery`, `minimal-scar`
- `scar/` → `accurate-diagnosis`, `diagnosis-system`, `specialist-surgery`, `minimal-scar` (2026-04-17 Gemini 신규 생성 — 기존 reconstruction 이미지 공유 상태에서 전용으로 분리)
- `fracture/` → `accurate-diagnosis`, `diagnosis-system`, `specialist-surgery`, `minimal-scar` (2026-04-17 Gemini 신규 생성)
- `burn/` → `burn-stages`, `acute-burn`, `skin-graft`, `burn-scar-recon`, `contracture`, `burn-scar-nonsurgical`, `pediatric-burn`, `emergency-system`, `inpatient-care`, `long-term-scar`

**이 목록에 없는 이미지 경로는 사용 금지** — 없는 이미지는 CSS 그라디언트로 처리.

> `.gitignore`에 `*.png` 전역 무시 규칙이 있고 `!images/**/*.png` 예외가 적용되어 있다. `images/` 밖의 PNG는 git에 추가되지 않는다. 이미지 경로는 반드시 공백·한글·괄호 없는 URL-safe 형식으로 유지할 것 (GitHub Pages에서 인코딩 오류 발생).

## 코드 아키텍처: 파일 완전 자급자족 구조

**공유 CSS/JS 파일이 없다.** 모든 스타일, GNB, 스크립트는 각 HTML 파일 내 `<style>`, `<script>` 블록에 인라인으로 존재한다.

공통 요소(GNB, 색상 변수, 푸터 등)를 수정할 때는 **영향받는 모든 파일을 각각 수정**해야 한다. 다수 파일을 한 번에 고칠 때는 `grep -rl | xargs sed` 방식을 사용한다 (멀티라인 for 루프는 이 환경에서 동작하지 않음):

```bash
# 특정 문자열이 있는 파일만 대상으로 일괄 치환
grep -rl 'OLD' /Users/chul/Documents/WORK/ysmc_pla/*.html | xargs sed -i '' 's/OLD/NEW/g'
```

GNB나 모바일 nav 블록 전체를 일괄 재구성할 때는 `_scripts/phase1_gnb.py` 참조. 해당 스크립트는 22개 HTML에 대해 정규식으로 `<nav class="gnb">...</nav>` 블록과 `<div class="mob-nav-section">` 블록을 찾아 신규 템플릿으로 치환하며, 파일별 `current` 마커는 `COSMETIC_FILES`/`MEDICAL_FILES` 매핑으로 유지. 멀티라인 문자열 치환은 `perl -0 -i`, 단일라인은 `sed`로 처리한다.

### `_scripts/` 디렉터리 도구 인벤토리

전 페이지 일괄 치환은 `sed`로 안 되는(멀티라인/복합) 경우 이 스크립트들을 참고·재활용한다:

- `phase1_gnb.py` — GNB/모바일 nav 블록 템플릿 치환기
- `naver_to_carechat.py` / `restore_naver.py` — 플로팅 CTA 블록 치환·복원 템플릿. 정규식 `subn` + 단일 CSS 문자열 replace 구조라, 다른 다중 파일 블록 작업에 복제하기 좋은 레퍼런스
- `gen_images.py` / `gen_index_medical.py` — Gemini 2.5 Flash Image 생성기. 자세한 워크플로는 아래 "Gemini 이미지 생성" 섹션

### 헤더 구조

**index.html만** 1줄 토바 (`.header-topbar`, 48px):

```
[선메디컬센터 유성선병원 성형외과]    병원소개 | 미용성형센터 | 외상·재건센터 | 커뮤니티  [≡]
```
- 헤더 높이: PC 48px / 모바일 44px. hero는 `height: 100svh` (margin-top 없음)

**나머지 모든 페이지** — 2단 헤더 (탭바 40px + GNB 64px = 104px):

```
         [미용성형센터 | 외상·재건센터]              ← 탭바 (.header-topbar, 중앙 정렬)
[로고]  병원소개▼ 눈성형▼ 코성형▼ ... 쁘띠▼  [진료예약] [상담예약]  [≡]  ← GNB (.header-gnb-row)
```

- **탭바**: 미용성형센터 / 외상·재건센터 전환. `.topbar-tab.active`로 현재 섹션 표시
- **GNB**: 전 페이지가 동일한 구조 (병원소개 + 7개 카테고리). 2026-04-17 재구성
  - Cosmetic (7 items): 병원소개 / 눈성형 / 코성형 / 가슴성형 / 동안성형 / 바디성형 / 쁘띠
  - Medical (6 items): 병원소개 / 상처·외상 / 화상 / 흉터 / 피부종양 / 안면부골절
  - **드롭다운이 정답이고 상세 페이지 내부 카드·태그가 여기에 맞춰져야 한다** — 드롭다운 변경 시 반드시 해당 페이지 `treatment-types`·`principle-tags`·FAQ까지 정합화. 현재 스냅샷:
    - `burn.html` treatment-types 3종: 화상 흉터 재건 / 구축 교정 / 소아 화상 치료 (드롭다운 "소아화상/구축 교정/화상흉터재건"과 일치). "구축성형술"은 2026-04-17 "구축 교정"으로 전역 치환됨
    - `reconstruction.html` treatment-types 3종: 모반 / 피지낭종 / 황색종 (본문 카드까지 질환별로 재작성)
    - `scar.html` treatment-types 2종: 흉터성형술 / 흉터 레이저 치료 (켈로이드·귀 켈로이드 카드·태그·원리 문구 전부 삭제됨)
    - `lifting.html`에서 **나노마이크로지방이식**, `petit.html`에서 **스킨부스터** 카드·태그·FAQ 문구 삭제됨. 실수로 복원하지 말 것
  - 병원소개 드롭다운: 공지사항·병원둘러보기·의료진소개·오시는 길
  - 눈성형 드롭다운: 쌍꺼풀 성형술(매몰/부분절개/절개) / 중년 눈 성형술(상안검/눈썹하거상/하안검) / 트임술(앞/뒷/밑/듀얼/윗) / 눈밑 성형술(눈밑지방재배치/하안검성형술)
- **드롭다운**: `.gnb-dropdown` (hover 시 표시), 눈성형은 `.dd-wide.dd-wide-4` 4컬럼 (min-width 700px)
- **현재 메뉴 표시**: `.gnb-item > a.current` 클래스
- **CTA 버튼**: `.header-cta` 안에 `.btn-outline-w`(진료예약) + `.btn-solid-w`(상담 예약)
- **모바일** (768px 이하): `.gnb, .header-cta { display: none }`, 햄버거만 표시 → 풀스크린 오버레이
- **헤더 높이**: PC 104px(탭바 40 + GNB 64) / 모바일 96px(탭바 36 + GNB 60) → `.page-hero { margin-top: 104px }`, 모바일 `96px`. 모바일 축소 수치는 `@media (max-width: 768px)` 안에서 재정의됨
- **예외**: `burn.html`은 `emergency-banner`가 헤더 바로 아래에 오므로 margin-top이 banner에 적용됨

### JS 패턴

- **진료 상세 페이지**: 플로팅 CTA 토글용 standalone `<script>` IIFE만 존재. FAQ 아코디언은 `onclick="this.parentElement.classList.toggle('active')"` 방식
- **index.html**: IIFE — 헤더 스크롤, 모바일 메뉴, Intersection Observer fade-up, 스플릿 히어로 터치 (`height: 100svh`, `.sp-seam::before` 구분선은 `display: none` 상태 유지)
- **cosmetic.html / medical.html**: IIFE — 자동 슬라이드쇼(3초 전환), 카테고리 스크롤 drag-to-scroll, 플로팅 CTA 토글
- **about.html**: IIFE — 카드 stagger 애니메이션. 오시는 길 섹션에 Google Maps iframe 내장 (`https://www.google.com/maps?q=...&output=embed`), API 키 불필요
- **tour.html**: 터치 스와이프 슬라이더 (화살표 + dot 인디케이터)
- **reviews.html**: IIFE — `localStorage: ysmc_reviews` 로딩 후 카드 렌더링, 카테고리 필터(`data-cat` 속성), 클릭 시 상세 모달 (`modal-overlay.open` 토글 + `document.body.style.overflow` 제어)

### 허브 페이지 섹션 구성 (cosmetic.html / medical.html)

**cosmetic.html:** 히어로 슬라이드쇼(눈/코/리프팅/지방/가슴/기타/쁘띠 — 7종) → 카테고리 스크롤 7종 → Why Choose Us → 의료진 소개 → CTA

**medical.html:** 프로모션 배너(응급/조직검사/안면부골절) → 히어로 슬라이드쇼(외상/화상/흉터/피부종양/안면부골절 — 5종) → 카테고리 스크롤 5종 → 안전 시스템 → 의료진 소개 → CTA

### eye.html 본문 5블록 구조 (2026-04-17 재편)

`surgery-types` 섹션을 5개 하위 섹션으로 분리하여 각각 `id`로 앵커링:
1. `#double-eyelid` 쌍꺼풀 성형술 — 매몰법·부분절개법·절개법 3 카드
2. `#upper-blepharoplasty` 상안검 성형술 — 1 카드 (surgery-types.alt 배경)
3. `#brow-lift` 눈썹하 거상술 — 1 카드
4. `#trim` 트임술 — 앞/뒷/밑/듀얼/윗 5 카드 (surgery-types.alt 배경)
5. `#under-eye` 눈밑 성형술 — 눈밑지방재배치 + `#lower-blepharoplasty` 하안검성형술 2 카드

GNB 드롭다운 중 "중년 눈 성형술" 라벨(상안검+눈썹하거상+하안검)은 본문에서는 #upper-blepharoplasty / #brow-lift / #lower-blepharoplasty 3군데로 분산 노출. 하안검성형술은 GNB 중년 눈 성형술과 본문 눈밑 성형술 **양쪽 모두에** 표시 (사용자 지시).

`.surgery-types.alt { background: var(--surface) }` 스타일로 섹션이 교차 배경되도록 처리.

### 좌우 스크롤 트랙 정렬 패턴 (중요)

Chrome에서 `scroll-snap-type`을 가진 flex 컨테이너에 `padding-left`를 주면 첫 카드로 스냅되어 padding이 무효화된다. `::before` 가상 요소를 좌측 스페이서로 사용:

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
  /* gap(16px)만큼 뺀 값 */
  width: max(16px, calc((100vw - 1360px) / 2 + 16px));
}
```

- `gap` 값이 spacer와 첫 카드 사이에도 적용되므로 `::before` width에서 gap을 차감해야 정렬이 맞음
- drag-to-scroll JS는 `document` 레벨 이벤트 리스너 사용 (트랙 밖에서 마우스를 놓아도 작동)

> **[롤백 참고] cosmetic.html 전후변화 섹션**: 2026-03-26 삭제. 실제 케이스 사진 확보 시 복원 방법:
> 1. CSS: `.before-after-section`, `.ba-*` 관련 스타일 블록을 카테고리 스크롤 CSS 뒤에 추가 (gap: 20px, spacer: `max(12px, calc((100vw - 1360px) / 2 + 12px))`)
> 2. HTML: `<!-- ===== TRUST SECTION -->` 바로 앞에 `<section class="before-after-section">` 블록 삽입 (ba-scroll-wrapper → 4장 ba-card → ba-notice 구조)
> 3. JS: `catTrack` 드래그 스크롤 블록 뒤에 `baScrollTrack` 변수 선언 + 버튼 이벤트 + 드래그 스크롤 IIFE 추가
> 4. 모바일 @media: `.before-after-section { padding: 60px 0; }` 외 ba-* 오버라이드 추가
> 5. 실제 사진은 `images/` 폴더에 넣고 `ba-half` 배경 이미지로 교체 (`background-image: url(...)`, `background-size: cover`)

### booking.html 구조 (현행)

커스텀 예약 폼 없음. 3채널 카드로만 구성:
- **온라인 예약** → 본원 예약시스템 외부 링크 (`href="#"`, `<!-- TODO -->` 주석으로 URL 교체 위치 표시)
- **전화 예약** → 성형외과 직통 (`href="tel:042-609-1190"`)
- **카카오톡 예약** → 카카오 케어챗 링크 (`href="#"`, `<!-- TODO -->` 주석으로 URL 교체 위치 표시)

### 모바일 주의사항

- **CSS 캐스케이드 순서**: `.mobile-cta { display: none }` 기본 정의는 반드시 `@media` 블록보다 **앞에** 선언. 기존 파일 중 순서가 뒤바뀐 경우 `@media` 안에 `!important`가 붙어 있음
- **하단 고정 CTA 바** (`class="mobile-cta"`): `padding-bottom: calc(10px + env(safe-area-inset-bottom))`으로 아이폰 노치 대응
- **브레이크포인트**: `1024px` (태블릿), `768px` (모바일)

## CSS 색상 시스템

페이지 그룹별로 색상 팔레트가 다르다. 수정 전 해당 파일의 `:root`를 반드시 확인할 것.

**전 페이지 공통** (index, cosmetic, medical, about, doctor, tour, 상세 페이지 등) — 로즈/와인 계열:
```css
:root {
  --primary: #9E6B7B;
  --primary-light: #D4A5B5;
  --primary-dark: #8A5568;
  --accent: #D4A5B5;
  --bg-off: #F3E8E4;
  --text-dark: #2D1F24;
  --text-mid: #6B5258;
  --surface: #FBF5F3;
}
```

**미용·성형 상세 페이지** (eye, nose, lifting 등)는 `--wine`, `--navy`, `--navy-mid`, `--bg-off`를 정의하지 않는다.

## admin.html 특이사항 (유성선병원 성형외과 MASTER PAGE)

공개 사이트와 완전히 분리된 운영 관리 페이지. GNB 없음, 공개 페이지에서 링크되지 않음.

- **CDN 의존**: Tailwind CSS (커스텀 teal/surface 컬러 확장), Google Fonts (Noto Sans KR) — 인터넷 필수
- **인증**: `sessionStorage('ysmc_admin')` — 비밀번호는 JS 내 `ADMIN_PW` 상수 (정적 사이트 한계, 실 운영 시 서버 사이드 인증 필요)
- **테마**: `<html class="dark">` 고정 (라이트 모드 없음)
- **3개 관리 메뉴**: 팝업 관리 / 공지사항 관리 / 온라인 상담 (수술후기 관리는 2026-04-17 제거됨)
- **이미지 업로드**: 팝업의 이미지 필드는 `<input type="file">` → `FileReader.readAsDataURL()` → Base64 Data URL로 localStorage에 저장. 선택 즉시 썸네일 미리보기 표시, × 버튼으로 삭제. 고해상도 원본 업로드 시 localStorage 5MB 한도 주의.
- **localStorage 데이터 계약** — 공개 페이지 연동 현황:
  - `ysmc_popup` → `index.html` 팝업 오버레이 표시 (날짜 범위 + "오늘 하루 보지 않기" 지원) ✅
  - `ysmc_reviews` → `reviews.html` 수술후기 (admin에서 제거됨, 공개 페이지는 잔존하나 비활성 상태)
  - `ysmc_notices` → `notice.html` 공지사항 동적 로딩 (기존 하드코딩 목록 위에 prepend, 클릭 시 본문 모달) ✅
  - `ysmc_consultations` → `consultation.html` 폼 submit → admin에서 미확인/확인/답변완료 관리 ✅
- **미확인 상담 뱃지**: 사이드바에 `pending` 상태 건수 표시, 상담 클릭 시 `pending→read` 자동 전환

## dashboard.html 특이사항

- **CDN 의존**: Tailwind CSS, Google Fonts — 인터넷 필수
- **테마**: `<html class="dark">` 기본값, `html.light-mode` 토글, `localStorage('dashboardTheme')` 저장

## 레이아웃 패턴

- 최대 너비: `1280px` / 섹션 패딩: 상하 `100px`, 좌우 `40px`
- 폰트: Pretendard (CDN) → `'Apple SD Gothic Neo'` → `'Malgun Gothic'`
  - 예외: `community.html`, `reviews.html`은 Manrope(Google Fonts)를 1순위로 사용 (`'Manrope', 'Pretendard', ...`)

## OG / SNS 공유 메타태그

`index.html`에 OG 및 Twitter Card 메타태그가 설정되어 있다. 썸네일 이미지는 **절대 URL**이어야 하며, 한글·공백이 포함된 경로는 사용 불가.

```html
<meta property="og:image" content="https://chul1215.github.io/ysmc_pla/images/lifting.jpg">
```

- 카카오톡 캐시 초기화: https://developers.kakao.com/tool/clear/og

## 브랜드 & 콘텐츠 규칙

- **핵심 메시지**: "종합병원의 안전함에 섬세함을 더하다"
- **의료진 호칭**: "전문의" 또는 "과장" 사용. **"원장" 사용 금지** (종합병원 진료과 형태)
- **담당의**: 신정환 과장 (성형외과 전문의, 가톨릭중앙의료원 출신)
- **대표전화**: `042-609-1190` (전 페이지 적용됨)
- **CTA 4종 (순서 고정)**: 전화 상담(`tel:042-609-1190`) → 진료 예약(`booking.html`) → 카카오 상담 → 네이버 예약. 네이버 예약은 기능 여부 확인 중이라 병행 유지(확정 시 제거 여부 재결정).
- **플로팅 CTA** (데스크탑 우측, 전 페이지): 전화 상담 / 카톡 상담 / 카카오 케어챗 예약 / 네이버 예약 — `.float-cta` + 토글 JS, 태블릿/모바일에서 `display: none`. 케어챗 버튼은 `.float-btn-carechat`(배경 `#3C1E1E` + 텍스트 `#FEE500`), 네이버 버튼은 `.float-btn-naver`(`#03C75A`), 둘 다 `href="#"` 상태로 URL 주입 대기
- **남성성형**: `male.html` 파일은 존재하나 GNB/모바일nav/cosmetic 슬라이드에서 **링크 제거됨** (직접 URL 접근만 가능)
- **미용성형 컬러**: `--primary` / **치료재건 컬러**: `--navy-mid`
- **의료법 준수**: "최고", "완벽한", "100% 만족" 등 과장 표현 금지

### 이미지 카드 구조 패턴

`about.html` `.mission-card`, `index.html`/`medical.html` `.safety-card`는 이미지+텍스트 조합 구조를 사용한다:

```html
<div class="safety-card">
  <div class="safety-img">
    <img src="images/card-image/safety-main/emergency-24h.jpg" alt="..." loading="lazy">
  </div>
  <div class="safety-card-body">
    <span class="safety-icon">...</span>
    <h3>...</h3>
    <p>...</p>
  </div>
</div>
```

- 이미지 높이: PC `190px` / 태블릿 `260px` / 모바일 `220px`
- 호버 시 이미지 `scale(1.06)` 줌인 (`transition: transform 0.5s ease`)
- `index.html` `.drlog-card`의 `.drlog-thumb`도 동일 패턴 — `position: absolute` img + `::after` 어두운 그라디언트 오버레이 + `z-index: 2` 뱃지/아이콘

## Stitch MCP (AI UI 디자인)

Google Stitch MCP가 연결되어 있어 대화 중 UI 디자인 생성을 직접 요청할 수 있다.

- **MCP 서버**: `stitch-mcp` (npx stitch-mcp)
- **Google Cloud 프로젝트**: `gen-lang-client-0995891471` (Default Gemini Project)
- **인증 방식**: Application Default Credentials (`~/.config/gcloud/application_default_credentials.json`)
- **MCP 재연결**: `claude mcp restart stitch`
- **인증 만료 시**: `gcloud auth application-default login` 재실행

Stitch로 생성한 HTML/CSS 결과물을 이 프로젝트에 통합할 때는 인라인 스타일 구조를 유지하고, CSS 변수를 프로젝트 색상 시스템으로 교체해야 한다.

## Gemini 이미지 생성 (장면 실사진 합성)

"우리 병원 분위기" 컷을 만들어낼 때 `nano-banana` MCP 또는 직접 REST 호출을 사용한다. `_scripts/gen_images.py`·`gen_index_medical.py`가 레퍼런스.

- **모델**: `gemini-2.5-flash-image` — **`-preview` 접미사 안 붙은 쪽**. preview 모델명은 일부 프로젝트에서 404로 거절됨. `nano-banana-mcp` npm 패키지는 기본적으로 preview를 호출하므로 필요 시 `~/.npm/_npx/<hash>/node_modules/nano-banana-mcp/dist/index.js`에서 모델명 패치 후 `pkill -f nano-banana-mcp`로 프로세스 재시작
- **결제 조건**: 이 모델은 **무료 티어 quota 0**. `AIza...` API 키 프로젝트에 Billing 활성화 필수. 비용은 장당 약 $0.04. Imagen 4 계열도 유료 전용
- **키 주입**: 스크립트는 `os.environ["GEMINI_API_KEY"]`로 받음. 절대 소스에 하드코딩하지 말 것. MCP 등록은 `claude mcp add -s user -e GEMINI_API_KEY=... nano-banana -- npx -y nano-banana-mcp`
- **출력 포맷**: 1024×1024 정사각 PNG/JPG. 세로/가로 비율이 필요해도 출력은 정사각으로 나오므로 프롬프트에서 "vertical 3:4 portrait composition" 같은 힌트만 가능. 최종 표시는 CSS `background-size: cover + position: center`로 대응
- **프롬프트 지침**: "Korean plastic surgeon", "Korean university hospital OR", "dusty rose palette (#9E6B7B)" 같은 맥락 키워드 + "No text, no logo, no watermark" 필수. 의료 사이트라 Unsplash 등 스톡은 한국 의료진 부재로 대체재가 되지 못함

## 콘텐츠 전략 참고

`reference/content_strategy.md` — 경쟁사 벤치마킹, 페이지별 카피 브리프, 차별화 포지셔닝. **카피 수정 시 반드시 참고.**

`reference/3rd_feedback.md`, `reference/second_feedback.md` — 피드백 이력. 이전 수정 맥락 파악 시 참고.

`reference/microsite_cf.md` — 마이크로사이트 콘텐츠 방향 참고.

## 기획·전략 문서

`plan/` — 전체 프로젝트 실행 기획안. 페이지 구조, 오픈 일정, 예산 등 상위 기획 참고 시 우선 열람.

`briefing/` — SNS·마케팅 전략 보고서 모음. 아래 파일이 핵심이다:

- `briefing/sns_strategy_integrated.md` — **SNS 운영 전략 최종안** (harada 벤치마크 + 대전 경쟁 분석 통합). SNS 관련 카피·전략 수정 시 반드시 참고.
- `briefing/dashboard_briefing.md` — 마케팅 기획 전체 요약 대시보드.
- `briefing/competitor_analysis_daejeon.md` — 대전 지역 성형외과 경쟁 분석.
- `briefing/sns_benchmark_harada.md` — @days_harada 일본 계정 심층 분석.
- `briefing/instagram_benchmark_daejeon.md` — 대전 경쟁사 인스타그램 계정 분석.
