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
