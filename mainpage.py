import streamlit as st

st.set_page_config(page_title="MBTI 취미 추천 홈 🎉", page_icon="🌟")

# 화면 중앙 정렬
st.markdown("<h1 style='text-align: center;'>🌈 MBTI 취미 추천기 🎧</h1>", unsafe_allow_html=True)

st.write("")
st.write("")

st.markdown("""
<div style='text-align: center; font-size:18px;'>
안녕! 반가워 👋  
여기는 너의 **MBTI 성향에 딱 맞는 취미**를 추천해주는 귀여운 공간이야 🎀  
<br>
각 MBTI별로 <b>취미 2가지 + 준비물 + 참여할 수 있는 동호회</b>까지 알려줄게!  
재미있고 부담없이 즐길 수 있는 취미들만 골라놨어 😎  
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

st.markdown("### ✨ 이런 친구들에게 추천해!")
st.markdown("""
- 뭘 좋아하는지 아직 잘 모르겠는 사람 🤔  
- 해야 할 건 많은데 막상 취미는 없는 사람 🧸  
- 새로 무언가를 시작해보고 싶은 사람 🌱  
""")

st.write("")
st.write("")

st.markdown("<h3 style='text-align:center;'>👇 시작하려면 아래 버튼을 눌러줘!</h3>", unsafe_allow_html=True)

# 버튼 → main.py 페이지로 이동
if st.button("🎮 취미 추천 받으러 가기!"):
    st.switch_page("main.py")   # ✅ Streamlit 1.27 이상에서 지원
