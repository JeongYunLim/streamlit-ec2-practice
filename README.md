# EC2 Streamlit 배포 실습

오픈소스소프트웨어실습 과제용 Streamlit 앱입니다.

## 프로젝트 설명

이 프로젝트는 AWS Learner Lab의 EC2 환경에서 Streamlit 앱을 실행하고, 외부 브라우저에서 EC2 주소로 접속했을 때 앱이 정상적으로 열리는지 확인하기 위한 배포 실습입니다.

이번 과제의 핵심은 복잡한 기능 구현이 아니라, Streamlit 앱을 EC2 서버에서 실행하고 EC2 Public IPv4 주소와 8501 포트를 통해 접속 가능한 상태로 만드는 것입니다.

## 주요 기능

- 간단한 텍스트 입력
- 메시지 입력
- 버튼 클릭
- 입력 결과 출력
- EC2 배포 확인용 화면 제공

## 실행 방법

아래 명령어를 순서대로 실행합니다.

```bash
pip install -r requirements.txt
streamlit run app.py --server.address 0.0.0.0 --server.port 8501