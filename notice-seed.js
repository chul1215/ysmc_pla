/* =============================================================
 * 공지사항 시드 데이터
 * - 최초 방문 시 localStorage('ysmc_notices')에 주입됨
 * - 'ysmc_notices_seeded' 플래그로 1회성 주입 보장
 * - admin.html에서 시드 공지를 삭제하면 복원되지 않음
 * - 관리자가 작성한 신규 공지는 영향받지 않음 (id 충돌 체크)
 * ============================================================= */
(function(global) {
  'use strict';

  var SEED_NOTICES = [
    {
      id: 'seed-10',
      category: '공지',
      title: '선메디컬센터 유성선병원 성형외과 홈페이지 오픈 안내',
      body: '<p>안녕하세요, 선메디컬센터 유성선병원 성형외과입니다.</p>' +
            '<p>2024년 12월, 선메디컬센터 유성선병원 성형외과 공식 홈페이지가 오픈되었습니다. 본 홈페이지를 통해 진료 정보, 의료진 소개, 온라인 상담 및 예약 서비스를 편리하게 이용하실 수 있습니다.</p>' +
            '<h3>제공 서비스</h3>' +
            '<ul>' +
              '<li>미용성형 및 치료재건 진료 안내</li>' +
              '<li>신정환 과장 프로필 및 진료 예약</li>' +
              '<li>온라인 상담 신청 (24시간 접수)</li>' +
              '<li>병원 둘러보기 및 오시는 길 안내</li>' +
            '</ul>' +
            '<p>더 나은 서비스 제공을 위해 지속적으로 개선해 나가겠습니다.</p>' +
            '<p><strong>문의: 042-609-1190</strong></p>',
      author: '관리자',
      date: '2024-12-01',
      updatedAt: '2024-12-01',
      views: 1045,
      pinned: false,
      visible: true,
      attachments: []
    },
    {
      id: 'seed-9',
      category: '공지',
      title: '개인정보처리방침 개정 안내 (2024년 12월 시행)',
      body: '<p>선메디컬센터 유성선병원 성형외과 개인정보처리방침이 개정되어 2024년 12월부터 시행됩니다.</p>' +
            '<h3>주요 개정 내용</h3>' +
            '<ul>' +
              '<li>온라인 상담 및 예약 서비스 관련 수집 항목 명시</li>' +
              '<li>개인정보 보관 기간 세부 조정 (상담 기록 3년, 진료 예약 5년)</li>' +
              '<li>제3자 제공 및 위탁 처리 내용 보완</li>' +
            '</ul>' +
            '<p>자세한 내용은 홈페이지 하단 <strong>개인정보처리방침</strong>에서 확인하실 수 있습니다.</p>' +
            '<p>개정 내용에 관한 문의는 병원 원무과로 연락 부탁드립니다.</p>' +
            '<p><strong>문의: 042-609-1190</strong></p>',
      author: '관리자',
      date: '2024-12-10',
      updatedAt: '2024-12-10',
      views: 228,
      pinned: false,
      visible: true,
      attachments: []
    },
    {
      id: 'seed-8',
      category: '공지',
      title: '온라인 예약 시스템 오픈 안내',
      body: '<p>선메디컬센터 유성선병원 성형외과 온라인 예약 시스템이 오픈되었습니다. 병원 방문 전 온라인으로 원하는 날짜와 시간을 예약하실 수 있습니다.</p>' +
            '<h3>예약 가능 채널</h3>' +
            '<ul>' +
              '<li>홈페이지 <strong>진료예약</strong> 메뉴</li>' +
              '<li>네이버 예약 (24시간 접수)</li>' +
              '<li>카카오 케어챗</li>' +
              '<li>전화 예약: <strong>042-609-1190</strong></li>' +
            '</ul>' +
            '<blockquote>성형외과 상담은 충분한 시간이 필요하여 사전 예약제로 운영됩니다.</blockquote>',
      author: '관리자',
      date: '2024-12-20',
      updatedAt: '2024-12-20',
      views: 395,
      pinned: false,
      visible: true,
      attachments: []
    },
    {
      id: 'seed-7',
      category: '공지',
      title: '카카오톡 상담 채널 개설 안내 (@유성선병원성형외과)',
      body: '<p>선메디컬센터 유성선병원 성형외과 카카오톡 채널이 개설되었습니다.</p>' +
            '<p>진료 문의, 수술 후 경과 관리, 예약 변경 등 다양한 상담을 카카오톡으로 편리하게 받으실 수 있습니다.</p>' +
            '<h3>채널 정보</h3>' +
            '<ul>' +
              '<li><strong>채널명</strong>: 유성선병원성형외과</li>' +
              '<li><strong>응대 시간</strong>: 평일 09:00 – 18:00, 토요일 09:00 – 13:00</li>' +
              '<li>주말·공휴일 문의는 다음 영업일에 순차 답변드립니다.</li>' +
            '</ul>' +
            '<p>카카오톡 검색창에서 <strong>유성선병원성형외과</strong>를 검색해 주세요.</p>',
      author: '관리자',
      date: '2025-01-05',
      updatedAt: '2025-01-05',
      views: 712,
      pinned: false,
      visible: true,
      attachments: []
    },
    {
      id: 'seed-6',
      category: '공지',
      title: '실손보험 청구 서류 발급 서비스 안내',
      body: '<p>실손보험 청구를 위한 서류 발급 서비스를 안내드립니다.</p>' +
            '<h3>발급 가능 서류</h3>' +
            '<ul>' +
              '<li>진료비 영수증 및 세부내역서</li>' +
              '<li>진단서 (보험용)</li>' +
              '<li>입·퇴원 확인서</li>' +
              '<li>수술 확인서</li>' +
            '</ul>' +
            '<h3>발급 방법</h3>' +
            '<ul>' +
              '<li>병원 원무과 직접 방문</li>' +
              '<li>전화 신청 후 우편 발송 (042-609-1190)</li>' +
            '</ul>' +
            '<blockquote>미용 목적 시술은 실손보험 적용 대상이 아닙니다. 치료 목적(외상·재건·기능 개선) 수술은 보험 적용 여부를 담당 과장과 상담하신 후 안내드립니다.</blockquote>',
      author: '관리자',
      date: '2025-01-10',
      updatedAt: '2025-01-10',
      views: 488,
      pinned: false,
      visible: true,
      attachments: []
    },
    {
      id: 'seed-5',
      category: '공지',
      title: '2025년 설날 연휴 진료 일정 안내 (1/28 ~ 1/30 휴진)',
      body: '<p>2025년 설날 연휴 진료 일정을 안내드립니다.</p>' +
            '<h3>휴진 기간</h3>' +
            '<ul>' +
              '<li><strong>2025년 1월 28일(화) ~ 1월 30일(목)</strong></li>' +
            '</ul>' +
            '<h3>정상 진료 재개</h3>' +
            '<ul>' +
              '<li>2025년 1월 31일(금) 09:00부터</li>' +
            '</ul>' +
            '<h3>응급 진료</h3>' +
            '<p>연휴 기간에도 유성선병원 응급실은 24시간 운영되며, 외상·화상 등 응급 상황은 언제든 내원 가능합니다.</p>' +
            '<p><strong>문의: 042-609-1190</strong> (연휴 중 응급실로 자동 연결)</p>',
      author: '관리자',
      date: '2025-01-20',
      updatedAt: '2025-01-20',
      views: 623,
      pinned: false,
      visible: true,
      attachments: []
    },
    {
      id: 'seed-4',
      category: '공지',
      title: '신정환 과장 MBC 대전 뉴스 출연 안내 (2025.02.20)',
      body: '<p>신정환 과장이 MBC 대전 뉴스에 출연하여 안면부 골절 및 외상 재건 수술에 관한 인터뷰를 진행합니다.</p>' +
            '<h3>방송 정보</h3>' +
            '<ul>' +
              '<li><strong>방송일</strong>: 2025년 2월 20일(목)</li>' +
              '<li><strong>방송사</strong>: MBC 대전</li>' +
              '<li><strong>프로그램</strong>: MBC 대전 뉴스데스크</li>' +
              '<li><strong>주제</strong>: 안면부 골절 환자의 기능·심미 동시 회복</li>' +
            '</ul>' +
            '<p>성형외과 전문의가 종합병원 환경에서 외상 재건 수술을 집도하는 특성과 다학제 협진 시스템을 소개할 예정입니다. 많은 관심 부탁드립니다.</p>',
      author: '관리자',
      date: '2025-02-18',
      updatedAt: '2025-02-18',
      views: 541,
      pinned: false,
      visible: true,
      attachments: []
    },
    {
      id: 'seed-3',
      category: '공지',
      title: '2025년 3월 진료시간 변경 안내 — 토요일 오후 진료 추가',
      body: '<p>2025년 3월부터 토요일 오후 진료가 추가됩니다.</p>' +
            '<h3>변경 후 진료시간</h3>' +
            '<ul>' +
              '<li><strong>평일</strong>: 09:00 – 18:00</li>' +
              '<li><strong>토요일</strong>: 09:00 – 17:00 (점심시간 13:00 – 14:00)</li>' +
            '</ul>' +
            '<p>기존 토요일 오전 진료(09:00 – 13:00)에서 오후 시간대가 추가되었습니다. 직장인·학생분들의 편의를 고려한 조치이며, 토요일 수술 스케줄도 일부 운영됩니다.</p>' +
            '<p><strong>예약 문의: 042-609-1190</strong></p>',
      author: '관리자',
      date: '2025-03-10',
      updatedAt: '2025-03-10',
      views: 312,
      pinned: false,
      visible: true,
      attachments: []
    },
    {
      id: 'seed-2',
      category: '공지',
      title: '외상 응급 환자 24시간 접수 시스템 도입 안내',
      body: '<p>선메디컬센터 유성선병원 성형외과는 종합병원 내 응급실과 연계하여 외상 응급 환자 24시간 접수 시스템을 도입하였습니다.</p>' +
            '<h3>적용 대상</h3>' +
            '<ul>' +
              '<li>안면부 열상·찢김 상처</li>' +
              '<li>안면부 골절 (코·광대·턱 등)</li>' +
              '<li>화상 (모든 범위)</li>' +
              '<li>손 외상 및 절단 사고</li>' +
            '</ul>' +
            '<h3>이용 방법</h3>' +
            '<ol>' +
              '<li>응급실 내원 → 응급의학과 초진 → 성형외과 협진</li>' +
              '<li>야간·주말·공휴일 24시간 동일하게 운영</li>' +
              '<li>응급 수술이 필요한 경우 즉시 수술실 연계</li>' +
            '</ol>' +
            '<blockquote>골든타임 내 봉합과 재건이 필요한 외상은 응급실로 바로 내원해 주십시오.</blockquote>' +
            '<p><strong>대표 전화: 042-609-1190</strong></p>',
      author: '관리자',
      date: '2025-02-15',
      updatedAt: '2025-02-15',
      views: 876,
      pinned: true,
      visible: true,
      attachments: []
    },
    {
      id: 'seed-1',
      category: '공지',
      title: '선메디컬센터 유성선병원 성형외과 신규 개설 및 진료 안내 (필독)',
      body: '<p>선메디컬센터 유성선병원 성형외과가 신규 개설되었습니다.</p>' +
            '<h3>개설 배경</h3>' +
            '<p>종합병원의 안전한 진료 환경에 섬세한 미용·재건 술기를 결합하여, 대전·충청 지역 주민분들께 한 단계 높은 수준의 성형외과 진료를 제공하고자 합니다.</p>' +
            '<h3>진료 영역</h3>' +
            '<ul>' +
              '<li><strong>미용성형</strong>: 눈·코·가슴·동안·바디·쁘띠</li>' +
              '<li><strong>치료재건</strong>: 외상·화상·흉터·피부종양·안면부골절</li>' +
            '</ul>' +
            '<h3>담당 의료진</h3>' +
            '<ul>' +
              '<li>신정환 과장 (성형외과 전문의, 가톨릭중앙의료원 출신)</li>' +
            '</ul>' +
            '<h3>종합병원 성형외과의 차별점</h3>' +
            '<ul>' +
              '<li>마취통증의학과·응급의학과·내과 전문의 상시 협진</li>' +
              '<li>24시간 응급 대응 시스템</li>' +
              '<li>수술 후 입원·회복 관리 일원화</li>' +
            '</ul>' +
            '<p><strong>예약 및 상담: 042-609-1190</strong></p>' +
            '<p>진료시간: 평일 09:00 – 18:00, 토요일 09:00 – 17:00</p>',
      author: '관리자',
      date: '2025-02-28',
      updatedAt: '2025-02-28',
      views: 1284,
      pinned: true,
      visible: true,
      attachments: []
    }
  ];

  function seedIfNeeded() {
    if (typeof localStorage === 'undefined') return;
    if (localStorage.getItem('ysmc_notices_seeded') === '1') return;
    var existing = [];
    try { existing = JSON.parse(localStorage.getItem('ysmc_notices') || '[]'); } catch(e) {}
    if (!Array.isArray(existing)) existing = [];
    var existingIds = {};
    existing.forEach(function(n) { if (n && n.id) existingIds[n.id] = true; });
    var merged = existing.slice();
    SEED_NOTICES.forEach(function(seed) {
      if (!existingIds[seed.id]) merged.push(seed);
    });
    localStorage.setItem('ysmc_notices', JSON.stringify(merged));
    localStorage.setItem('ysmc_notices_seeded', '1');
  }

  global.NoticeSeed = {
    data: SEED_NOTICES,
    seedIfNeeded: seedIfNeeded
  };
})(typeof window !== 'undefined' ? window : this);
