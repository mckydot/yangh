from fastapi import FastAPI
app = FastAPI()

from fastapi.responses import FileResponse

@app.get("/")
def naming() :
    return "hello world"

 ##   5. FastAPI로 공부한다면 추천하는 학습 순서
##내가 추천하는 순서는 다음과 같아.
##FastAPI + Jinja2: 서버에서 HTML을 생성하는 방식 이해
##FastAPI + REST API: JSON을 반환하고 HTTP 요청을 처리하는 방식 이해
##HTTP Method: GET, POST, PUT, PATCH, DELETE 이해
##Pydantic: 요청 데이터와 응답 데이터 검증
##SQLAlchemy: 데이터베이스 연동
##React + FastAPI: 프론트엔드와 백엔드를 실제로 분리해서 구현
##CORS: 서로 다른 출처의 프론트엔드와 백엔드가 통신하는 원리 이해
##특히 1번과 2번은 동일한 게시판을 두 방식으로 구현해 보는 걸 추천해.