import streamlit as st
import random

# 🌸 페이지 기본 설정
st.set_page_config(page_title="Girl's Vibe Music Picker ", page_icon="🎧", layout="centered")

# 🎀 CSS 꾸미기
st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #ffe6f0 0%, #ffd1dc 100%);
    color: #ff69b4;
    font-family: 'Comic Sans MS', cursive;
}
h1, h2, h3, p, select, button, label {
    text-align: center;
}
div.stButton > button {
    background-color: #ff85a2;
    color: white;
    border: none;
    border-radius: 20px;
    font-size: 20px;
    padding: 10px 25px;
    box-shadow: 0px 4px 10px rgba(255, 105, 180, 0.4);
}
div.stButton > button:hover {
    background-color: #ff4d88;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# 💕 제목
st.markdown("""
<h1>💖 Girl’s Mood Music 💖</h1>
<p>hey babe~ 오늘은 어떤 기분이야? ✨ 네 mood에 찰떡인 곡 골라줄게 💅</p>
""", unsafe_allow_html=True)

# 🌈 선택지
moods = ["💞 러블리", "🔥 자신감 뿜뿜", "🌧 감성 촉촉", "🌸 여유로운", "🌈 파티 타임"]
singers = ["🌸 Ariana Grande", "💎 BLACKPINK", "🌷 NewJeans", "🌙 IU", "🌻 Taylor Swift"]

mood = st.selectbox("✨ 오늘의 Mood를 골라줘!", moods)
singer = st.selectbox("🎤 듣고 싶은 Singer는 누구야?", singers)

# 💿 노래 추천 데이터베이스 (+유튜브 링크)
songs = {
    "💞 러블리": {
        "🌸 Ariana Grande": [("Into You", "https://www.youtube.com/watch?v=1ekZEVeXwek")],
        "💎 BLACKPINK": [("As If It’s Your Last", "https://www.youtube.com/watch?v=Amq-qlqbjYA")],
        "🌷 NewJeans": [("Super Shy", "https://www.youtube.com/watch?v=ArmDp-zijuc")],
        "🌙 IU": [("좋은 날", "https://www.youtube.com/watch?v=jeqdYqsrsA0")],
        "🌻 Taylor Swift": [("Lover", "https://www.youtube.com/watch?v=-BjZmE2gtdo")]
    },
    "🔥 자신감 뿜뿜": {
        "🌸 Ariana Grande": [("7 rings", "https://www.youtube.com/watch?v=QYh6mYIJG2Y")],
        "💎 BLACKPINK": [("Pink Venom", "https://www.youtube.com/watch?v=gQlMMD8auMs")],
        "🌷 NewJeans": [("ETA", "https://www.youtube.com/watch?v=jOTfBlKSQYY")],
        "🌙 IU": [("Coin", "https://youtu.be/86BST8NIpNM?si=ZOsVaBdXmmzvcUov")],
        "🌻 Taylor Swift": [("Look What You Made Me Do", "https://youtu.be/3tmd-ClpJxA?si=UuMGIvLRNquAAJvv")]
    },
    "🌧 감성 촉촉": {
        "🌸 Ariana Grande": [("pov", "https://www.youtube.com/watch?v=nQJEp-k-ogs")],
        "💎 BLACKPINK": [("Hope Not", "https://youtu.be/l6zMnMMzsss?si=h2WJ9-_dcd9mRCAC")],
        "🌷 NewJeans": [("Ditto", "https://www.youtube.com/watch?v=pSUydWEqKwE")],
        "🌙 IU": [("Love poem", "https://youtu.be/OcVmaIlHZ1o?si=lMtUUQMrgZgL6YXw")],
        "🌻 Taylor Swift": [("Cardigan", "https://www.youtube.com/watch?v=K-a8s8OLBSE")]
    },
    "🌸 여유로운": {
        "🌸 Ariana Grande": [("Moonlight", "https://www.youtube.com/watch?v=fLaNnH9i1D0")],
        "💎 BLACKPINK": [("Stay", "https://www.youtube.com/watch?v=FzVR_fymZw4")],
        "🌷 NewJeans": [("Cool With You", "https://youtu.be/kKsivrgoyDw?si=TeMVP-OT03-YHuND")],
        "🌙 IU": [("Palette", "https://www.youtube.com/watch?v=d9IxdwEFk1c")],
        "🌻 Taylor Swift": [("Willow", "https://www.youtube.com/watch?v=RsEZmictANA")]
    },
    "🌈 파티 타임": {
        "🌸 Ariana Grande": [("Break Free", "https://www.youtube.com/watch?v=L8eRzOYhLuw")],
        "💎 BLACKPINK": [("BOOMBAYAH", "https://www.youtube.com/watch?v=bwmSjveL3Lc")],
        "🌷 NewJeans": [("How Sweet", "https://www.youtube.com/watch?v=ArmDp-zijuc")],
        "🌙 IU": [("Jam Jam", "https://youtu.be/KWjDSRdIFgc?si=PJ4rIe5vFDR0dktX")],
        "🌻 Taylor Swift": [("Bejeweled", "https://www.youtube.com/watch?v=b7QlX3yR2xs")]
    }
}

# 💫 추천하기 버튼
if st.button("💖 추천해줘! 💖"):
    pick = random.choice(songs[mood][singer])
    title, link = pick

    st.markdown(f"""
    <div style='text-align:center;'>
        <h2 style='color:#ff85a2;'>🎧 오늘의 Girl's vibe 추천곡은...</h2>
        <h1 style='color:#ff1493;'> 💖 <i>{title}</i> 💖 </h1>
        <p style='color:#f78fb3;'>완전 {mood} mood랑 {singer} vibe에 찰떡이야~ 💅</p>
    </div>
    """, unsafe_allow_html=True)

    # 🎥 YouTube 미리듣기
    st.video(link)

# 🌟 푸터
st.markdown("<hr style='border: 1px solid pink;'>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#f78fb3;'>✨ made with 💖 by your it girl bestie ✨</p>", unsafe_allow_html=True)
