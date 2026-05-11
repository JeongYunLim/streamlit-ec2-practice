import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

st.set_page_config(
    page_title="EC2 Streamlit 배포 실습",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ EC2 Streamlit 배포 실습")
st.caption("오픈소스소프트웨어실습 과제용 기본 Streamlit 앱")

st.write(
    """
    이 앱은 AWS Learner Lab의 EC2 환경에서 Streamlit 앱이 정상적으로 실행되는지
    확인하기 위해 제작한 간단한 프론트엔드 앱입니다.
    """
)

st.write("브라우저에서 EC2 주소로 접속했을 때 이 화면이 보이면 배포가 정상적으로 된 것입니다.")

st.divider()

st.write("임정윤 | 2025404052 | 정보융합학부")

st.divider()

st.subheader("간단한 입력 테스트")

name = st.text_input("이름을 입력하세요")
message = st.text_input("확인 메시지를 입력하세요")

if st.button("결과 확인"):
    current_time = datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M:%S")

    print("========================================", flush=True)
    print("[LOG] Streamlit 앱에서 버튼이 클릭되었습니다.", flush=True)
    print(f"[LOG] 입력한 이름: {name}", flush=True)
    print(f"[LOG] 입력한 메시지: {message}", flush=True)
    print(f"[LOG] 확인 시간: {current_time} KST", flush=True)
    print("========================================", flush=True)

    if name and message:
        st.success("입력한 내용이 정상적으로 출력되었습니다.")
        st.write(f"입력한 이름: {name}")
        st.write(f"입력한 메시지: {message}")
        st.write(f"확인 시간: {current_time} KST")
    else:
        st.warning("이름과 확인 메시지를 모두 입력해주세요.")

st.divider()

