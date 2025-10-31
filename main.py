import streamlit as st

st.set_page_config(page_title="MBTI 취미 추천기 🎨", page_icon="🎧")

st.title("🎉 MBTI 기반 취미 추천기!")
st.write("안녕! 😄 너의 MBTI를 골라주면, 딱 맞는 취미 두 가지를 추천해줄게! "
         "설명도 쉽고 귀엽게 해줄게요 😎")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("👉 MBTI를 선택해주세요!", mbti_types)

hobby_data = {
    "ISTJ": [
        {
            "name": "📚 서점 탐방",
            "desc": "차분하게 혼자만의 시간 보내기 딱! 새로운 책 냄새는 감성 + 집중력 UP 😊",
            "items": "가벼운 가방, 노트, 펜",
            "club": "독서토론 동아리, 지역 도서관 독서 모임"
        },
        {
            "name": "⚽ 조용한 개인 운동 (런닝·사이클)",
            "desc": "규칙적인 루틴 좋아하는 ISTJ에게 찰떡! 꾸준하면 실력 + 건강 둘 다 챙김 💪",
            "items": "운동화, 물, 이어폰",
            "club": "학교 체력단련부, 지역 마라톤 커뮤니티"
        }
    ],
    "ISFJ": [
        {
            "name": "🌿 테라리움/미니 화분 키우기",
            "desc": "작은 생명을 돌보며 힐링하기 좋아하는 ISFJ에게 천천히 성장 보는 맛 🌱",
            "items": "작은 화분, 흙, 씨앗",
            "club": "식물 가꾸기 동호회, 반려식물 SNS 모임"
        },
        {
            "name": "📸 필름 감성 사진",
            "desc": "따뜻한 분위기 담는 감성 장인 ISFJ에게 찰떡 감성 📷",
            "items": "필름 카메라 or 감성 앱",
            "club": "사진 동아리, 감성사진 인스타 커뮤니티"
        }
    ],
    "INFJ": [
        {
            "name": "📝 감성 글쓰기",
            "desc": "마음 속 깊은 생각을 단어로 꺼내보는 시간 ✨ 마음 정리에도 최고!",
            "items": "노트, 펜, 조용한 공간",
            "club": "시·수필 동아리, 글쓰기 온라인 카페"
        },
        {
            "name": "🎧 나만의 플레이리스트 큐레이션",
            "desc": "INFJ는 음악으로 감정 여행하는 타입 🎶 플레이리스트 만들기 완전 잘함.",
            "items": "이어폰, 음악 스트리밍 앱",
            "club": "음악 감상 소모임, 플레이리스트 공유 SNS 모임"
        }
    ],
    "INTJ": [
        {
            "name": "♟️ 체스 / 전략 보드게임",
            "desc": "머리 쓰는 거 좋아하는 전략가 INTJ에게 딱! 승부욕 발동 ⚡",
            "items": "보드게임 앱 or 오프라인 체스판",
            "club": "보드게임 동아리, 지역 보드게임 카페 모임"
        },
        {
            "name": "💻 코딩 취미 시작",
            "desc": "논리력 갑인 INTJ에게 감각적 재미까지 챙길 수 있는 취미!",
            "items": "노트북, 구글링할 마음",
            "club": "학교 컴퓨터 동아리, GitHub 커뮤니티"
        }
    ],
    "ENFP": [
        {
            "name": "🎤 버스킹 감성 노래 / 노래방 놀기",
            "desc": "표현력 최고✨ 끼쟁이 ENFP는 함께 놀면서 에너지 충전!",
            "items": "물, 좋아하는 노래 리스트",
            "club": "밴드부, 지역 보컬 연습 모임"
        },
        {
            "name": "🎨 아트 토이 / 키링 만들기",
            "desc": "손으로 만드는 감성 작업 완전 잘 맞음! 개성 뿜뿜 🧸",
            "items": "UV 레진 키트 혹은 꾸미기 재료",
            "club": "핸드메이드 공방 체험, DIY 커뮤니티"
        }
    ],
    "ENTJ": [
        {
            "name": "🏋️‍♂️ PT/헬스 루틴 관리",
            "desc": "목표 세우고 달성하는 걸 좋아하는 ENTJ에게 헬스는 인생 RPG 🎮",
            "items": "운동화, 무선 이어폰, 운동 앱",
            "club": "헬스 커뮤니티, 학교 체력부"
        },
        {
            "name": "🗣️ 토론 / 발표 모임",
            "desc": "사고 말하고 정리하는 능력 최고! 리더력 발휘 가능 🧠",
            "items": "메모장, 자신감 10%",
            "club": "토론 동아리, 또래발표 소모임"
        }
    ],
  import streamlit as st

st.set_page_config(page_title="MBTI 취미 추천기 🎨", page_icon="🎧")

st.title("🎉 MBTI 기반 취미 추천기!")
st.write("안녕! 😄 너의 MBTI를 골라주면, 딱 맞는 취미 두 가지를 추천해줄게! "
         "설명도 쉽고 귀엽게 해줄게요 😎")

mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("👉 MBTI를 선택해주세요!", mbti_types)

hobby_data = {
    "ISTJ": [
        {
            "name": "📚 서점 탐방",
            "desc": "차분하게 혼자만의 시간 보내기 딱! 새로운 책 냄새는 감성 + 집중력 UP 😊",
            "items": "가벼운 가방, 노트, 펜",
            "club": "독서토론 동아리, 지역 도서관 독서 모임"
        },
        {
            "name": "⚽ 조용한 개인 운동 (런닝·사이클)",
            "desc": "규칙적인 루틴 좋아하는 ISTJ에게 찰떡! 꾸준하면 실력 + 건강 둘 다 챙김 💪",
            "items": "운동화, 물, 이어폰",
            "club": "학교 체력단련부, 지역 마라톤 커뮤니티"
        }
    ],
    "ISFJ": [
        {
            "name": "🌿 테라리움/미니 화분 키우기",
            "desc": "작은 생명을 돌보며 힐링하기 좋아하는 ISFJ에게 천천히 성장 보는 맛 🌱",
            "items": "작은 화분, 흙, 씨앗",
            "club": "식물 가꾸기 동호회, 반려식물 SNS 모임"
        },
        {
            "name": "📸 필름 감성 사진",
            "desc": "따뜻한 분위기 담는 감성 장인 ISFJ에게 찰떡 📷",
            "items": "필름 카메라 또는 감성 카메라 앱",
            "club": "사진 동아리, 감성 사진 공유 SNS"
        }
    ],
    "INFJ": [
        {
            "name": "📝 감성 글쓰기",
            "desc": "마음 속 생각을 단어로 꺼내보는 시간 ✨",
            "items": "노트, 펜",
            "club": "문예부, 글쓰기 커뮤니티"
        },
        {
            "name": "🎧 플레이리스트 큐레이팅",
            "desc": "음악으로 감정 여행하는 INFJ에게 찰떡 🎶",
            "items": "이어폰, 음악 앱",
            "club": "음악 공유 SNS 모임"
        }
    ],
    "INTJ": [
        {
            "name": "♟️ 체스 / 전략 게임",
            "desc": "두뇌 풀가동 전략 놀이 INTJ에게 완전 맞음 ⚡",
            "items": "보드게임 또는 앱",
            "club": "보드게임 모임"
        },
        {
            "name": "💻 코딩 취미",
            "desc": "분석 + 창조 동시에 만족 😎",
            "items": "노트북",
            "club": "코딩 스터디"
        }
    ],
    "ISTP": [
        {
            "name": "🛠️ DIY 조립/수리",
            "desc": "손으로 만지는 순간 집중력 MAX",
            "items": "조립 키트",
            "club": "메이커스 공방"
        },
        {
            "name": "🚴 자전거 라이딩",
            "desc": "혼자 떠나는 감성 미니 여행 🌬️",
            "items": "자전거, 물",
            "club": "지역 라이딩 모임"
        }
    ],
    "ISFP": [
        {
            "name": "🎨 수채화 / 드로잉",
            "desc": "조용한 감성 시간이 힐링 그 자체 💗",
            "items": "스케치북, 색연필",
            "club": "미술 동아리"
        },
        {
            "name": "🎧 카페 음악 감상",
            "desc": "분위기 = 힐링 🌙",
            "items": "이어폰",
            "club": "음악 감상 모임"
        }
    ],
    "INFP": [
        {
            "name": "📖 감성 소설/에세이",
            "desc": "상상력으로 우주 여행 가능 ✨",
            "items": "책 한 권",
            "club": "독서 모임"
        },
        {
            "name": "🎨 감정 다이어리",
            "desc": "내 마음을 예쁘게 저장하기 🧸",
            "items": "다이어리, 스티커",
            "club": "다꾸 커뮤니티"
        }
    ],
    "INTP": [
        {
            "name": "🧩 레고/퍼즐 조립",
            "desc": "몰입하면 시간 사라짐 😆",
            "items": "레고 or 퍼즐",
            "club": "메카닉 커뮤니티"
        },
        {
            "name": "🔍 지식 탐험 / 위키 탐험",
            "desc": "궁금하면 끝까지 파는 스타일 🔥",
            "items": "노트북",
            "club": "지식 토론 모임"
        }
    ],
    "ESTP": [
        {
            "name": "🏀 농구 / 풋살",
            "desc": "에너지 충전형 스포츠🔥",
            "items": "운동화",
            "club": "운동 동아리"
        },
        {
            "name": "🎮 경쟁 게임",
            "desc": "승부욕 뿜뿜 ⚡",
            "items": "게임 기기",
            "club": "e스포츠 팀"
        }
    ],
    "ESFP": [
        {
            "name": "💃 댄스 / K-POP 커버",
            "desc": "끼왕 ESFP 본진✨",
            "items": "운동화",
            "club": "댄스 동아리"
        },
        {
            "name": "📸 브이로그 촬영",
            "desc": "일상이 콘텐츠가 됨 🎥",
            "items": "휴대폰",
            "club": "영상 제작 모임"
        }
    ],
    "ENFP": [
        {
            "name": "🎤 노래방 / 버스킹 감성",
            "desc": "표현력 폭발 ENFP에 찰떡 💥",
            "items": "물, 노래리스트",
            "club": "밴드부, 보컬 크루"
        },
        {
            "name": "🧸 아트토이 / 키링 만들기",
            "desc": "창의력 = 무한대 ♾️",
            "items": "레진 키트",
            "club": "DIY 공방"
        }
    ],
    "ENTP": [
        {
            "name": "🎲 토론형 보드게임",
            "desc": "말+뇌 풀가동 🤓",
            "items": "보드게임",
            "club": "보드게임 카페"
        },
        {
            "name": "🎙️ 팟캐스트/의견 방송",
            "desc": "생각 말하는 게 걍 재밌는 타입 😎",
            "items": "마이크 or 폰",
            "club": "콘텐츠 제작 모임"
        }
    ],
    "ESTJ": [
        {
            "name": "⏱️ 루틴 챌린지",
            "desc": "계획 세우고 실천 = ESTJ의 진심",
            "items": "체크리스트",
            "club": "스터디 그룹"
        },
        {
            "name": "🏸 배드민턴",
            "desc": "깔끔 + 스피디 ✨",
            "items": "라켓",
            "club": "배드민턴 모임"
        }
    ],
    "ESFJ": [
        {
            "name": "🍰 베이킹",
            "desc": "누군가에게 나눠줄 수 있는 행복 💖",
            "items": "공방 or 오븐",
            "club": "베이킹 클래스"
        },
        {
            "name": "🎀 스크랩북 / 다꾸",
            "desc": "예쁜 거 좋아하면 무조건 만족 💗",
            "items": "스티커, 테이프",
            "club": "다꾸 SNS 모임"
        }
    ],
    "ENFJ": [
        {
            "name": "🌏 봉사 활동",
            "desc": "사람과 연결되는 ENFJ의 힐링 취미 ✨",
            "items": "물티슈, 편안한 복장",
            "club": "청소년 봉사단"
        },
        {
            "name": "🎬 연극 / 뮤지컬",
            "desc": "공감력+표현력 = 무대 체질 🎭",
            "items": "대본",
            "club": "연극부"
        }
    ],
    "ENTJ": [
        {
            "name": "🏋️‍♂️ 헬스 루틴 만들기",
            "desc": "목표 → 달성! ENTJ 모토 🔥",
            "items": "운동화",
            "club": "헬스 커뮤니티"
        },
        {
            "name": "🗣️ 토론/발표 모임",
            "desc": "리더력 발휘하는 자리 💡",
            "items": "메모장",
            "club": "토론 동아리"
        }
    ]
}


if mbti in hobby_data:
    st.subheader(f"✨ {mbti} 유형에게 추천하는 취미 활동은...")
    for hobby in hobby_data[mbti]:
        st.markdown(f"### {hobby['name']}")
        st.write(hobby["desc"])
        st.markdown(f"**🔧 준비물:** {hobby['items']}")
        st.markdown(f"**🤝 참여할 수 있는 동호회:** {hobby['club']}")
        st.divider()
else:
    st.info("해당 유형의 취미 정보는 업데이트 중이에요 😄 잠시만 기다려줘!")

st.write("💡 *참고로 MBTI는 참고용일 뿐! 진짜 중요한 건 ‘내가 재밌는지’야!* ✨")

}

if mbti in hobby_data:
    st.subheader(f"✨ {mbti} 유형에게 추천하는 취미 활동은...")
    for hobby in hobby_data[mbti]:
        st.markdown(f"### {hobby['name']}")
        st.write(hobby["desc"])
        st.markdown(f"**🔧 준비물:** {hobby['items']}")
        st.markdown(f"**🤝 참여할 수 있는 동호회:** {hobby['club']}")
        st.divider()
else:
    st.info("해당 유형의 취미 정보는 업데이트 중이에요 😄 잠시만 기다려줘!")

st.write("💡 *참고로 MBTI는 참고용일 뿐! 진짜 중요한 건 ‘내가 재밌는지’야!* ✨")
