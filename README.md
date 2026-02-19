# 유성선병원 성형외과 홍보 웹사이트

유성선병원 성형외과 신설 부서 홍보용 정적 웹사이트

## 🏥 프로젝트 개요

대학병원의 안전함에 섬세함을 더한 유성선병원 성형외과의 온라인 홍보 페이지입니다.

### 주요 진료 분야
- 👁️ **눈 성형** (eye.html)
- 🎯 **리프팅** (lifting.html)
- 💉 **쁘띠/스킨** (petit.html)
- 🏥 **외상** (trauma.html)
- 🔬 **재건·종괴** (reconstruction.html)

## 🛠️ 기술 스택

- **Frontend**: 순수 HTML5, CSS3, Vanilla JavaScript
- **빌드 시스템**: 없음 (정적 파일 직접 배포)
- **스타일**: CSS Variables + 반응형 디자인
- **애니메이션**: Intersection Observer API

## 📁 프로젝트 구조

```
ysmc_pla/
├── index.html          # 메인 랜딩 페이지
├── eye.html            # 눈 센터
├── lifting.html        # 리프팅
├── petit.html          # 쁘띠/스킨
├── trauma.html         # 외상
├── reconstruction.html # 재건·종괴
├── dashboard.html      # 관리자 대시보드
├── deploy/             # 배포용 파일 (루트 HTML과 동기화)
├── images/             # 이미지 리소스
└── plan/               # 기획서 및 마케팅 전략 문서
```

## 🎨 디자인 시스템

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

## 🚀 배포 방법

1. 루트 HTML 파일 수정
2. deploy 폴더에 동기화:
```bash
cp index.html eye.html lifting.html petit.html trauma.html reconstruction.html dashboard.html deploy/
```
3. 정적 파일 서버에 업로드

## 👨‍⚕️ 담당 의료진

**신정환 과장**
- 가톨릭중앙의료원 출신
- 전문 분야: 성형외과 전반

## 📞 문의

- 📞 전화 문의
- 💬 카카오톡 상담
- 📋 온라인 예약

## 📄 라이선스

Copyright © 2025 유성선병원 성형외과. All rights reserved.
