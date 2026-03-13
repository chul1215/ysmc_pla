# 유성선병원 성형외과 홍보 웹사이트

유성선병원 성형외과 신설 부서 홍보용 정적 웹사이트

## 프로젝트 개요

대학병원의 안전함에 섬세함을 더한 유성선병원 성형외과의 온라인 홍보 페이지입니다.

### 주요 진료 분야
- **눈 성형** (eye.html)
- **리프팅** (lifting.html)
- **쁘띠/스킨** (petit.html)
- **외상** (trauma.html)
- **재건·종괴** (reconstruction.html)

## 기술 스택

- **Frontend**: 순수 HTML5, CSS3, Vanilla JavaScript
- **빌드 시스템**: 없음 (정적 파일 직접 배포)
- **스타일**: CSS Variables + 반응형 디자인
- **애니메이션**: Intersection Observer API

## 프로젝트 구조

```
ysmc_pla/
├── index.html          # 메인 랜딩 페이지 (시안 1 — 그라디언트 히어로형)
├── index2.html         # 메인 랜딩 페이지 (시안 2 — 전체화면 스플릿 패널형)
├── eye.html            # 눈 센터
├── lifting.html        # 리프팅
├── petit.html          # 쁘띠/스킨
├── trauma.html         # 외상
├── reconstruction.html # 재건·종괴
├── dashboard.html      # 기획안 대시보드
├── images/             # 이미지 리소스
├── briefing/           # 브리핑 자료 (마케팅 기획안, 경쟁사 분석 등)
├── plan/               # 기획서 및 마케팅 전략 문서
└── reference/          # 참고 자료
```

## 디자인 시스템

### 색상 팔레트
```css
--primary: #cd4631;       /* 테라코타 레드 */
--primary-light: #d96858;
--primary-dark: #a33828;
--accent: #f8f2dc;        /* 웜 크림 */
--accent-light: #faf6e8;
--bg-light: #fdf8f0;
--bg-warm: #faf5e6;
```

### 레이아웃
- 최대 너비: 1280px
- 섹션 패딩: 상하 100px, 좌우 40px
- 반응형 브레이크포인트: 1024px, 768px

## 로컬 미리보기

빌드 없이 브라우저에서 직접 열거나, 상대경로 이슈 방지를 위해 로컬 서버 사용:

```bash
python3 -m http.server 8080
# → http://localhost:8080
```

## 배포

GitHub Pages를 통해 자동 배포됩니다:

- **배포 URL**: `https://chul1215.github.io/ysmc_pla/`
- **설정**: GitHub 저장소 Settings → Pages → Source: `main` branch, `/ (root)` folder
- `main` 브랜치에 푸시하면 자동 배포됩니다.

## 담당 의료진

**신정환 과장**
- 가톨릭중앙의료원 출신
- 36대·37대 대한공중보건의사협의회 회장 역임
- 보건복지부 장관 표창 (2023·2024)
- 전문 분야: 성형외과 전반 (미용·재건·외상)

## 문의

- 전화 문의
- 카카오톡 상담
- 온라인 예약

## 라이선스

Copyright © 2026 유성선병원 성형외과. All rights reserved.
