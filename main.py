import streamlit as st
st.title('김예지의 첫번째 앱')
st.subheader('배고파~~~')
st.write('안녕하세용ㅇ')
st.image('https://i.pinimg.com/236x/42/46/47/42464737a827965520363057c2169c65.jpg')
st.write('https://naver.com')
st.link_button("네이버 바로가기",'https://naver.com')

name=st.text_input('이름을 입력해주세요:')
if st.button('환영인사'):
    st.write(name+'님 안녕하세요!')
    st.balloons()
    st.image('https://talkimg.imbc.com/TVianUpload/tvian/TViews/image/2025/01/17/4777a40d-4cd1-4828-a0c1-a1d5bd7bdbbd.jpg')
    st.write('하루만 네 곁에 침대가 되고 싶어~~')
st.success('성공!')
st.warning('경고')
st.error('오류')
st.info('안내문')
