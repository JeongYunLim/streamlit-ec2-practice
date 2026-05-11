import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="EC2 Streamlit 배포 실습",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ EC2 Streamlit 배포 실습")
st.write("오픈소스소프트웨어실습 과제용 Streamlit 앱입니다.")

st.divider()

st.subheader("학생 정보")
st.write("학번: 2025404052")
st.write("이름: 임정윤")
st.write("과목: 오픈소스소프트웨어실습")

st.divider()

st.subheader("간단한 입력 테스트")

name = st.text_input("이름을 입력하세요")
message = st.text_area("메시지를 입력하세요")

if st.button("결과 출력"):
    if name and message:
        st.success(f"{name}님이 입력한 메시지입니다.")
        st.write(message)
        st.info(f"버튼 클릭 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        st.warning("이름과 메시지를 모두 입력해주세요.")

st.divider()

st.subheader("EC2 배포 확인용")
st.write("이 앱은 AWS Learner Lab EC2 환경에서 실행됩니다.")
st.write("브라우저에서 EC2 주소로 접속하면 이 화면이 보여야 합니다.")