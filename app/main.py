from fastapi import FastAPI
from app.routers import order, payment  # 우리가 만든 컨트롤러 로드

app = FastAPI(title="🍜 쌀국수 키오스크 시스템")

# 각각의 도메인 라우터(Controller)를 스프링 컨테이너에 빈으로 등록하듯 등록해줍니다!
app.include_router(order.router)
app.include_router(payment.router)

@app.get("/")
def home():
    return {"message": "쌀국수 키오스크 API 서버가 정상 가동 중입니다!"}