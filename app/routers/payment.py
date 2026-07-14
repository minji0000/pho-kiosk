from fastapi import APIRouter

router = APIRouter(
    prefix="/api/payments",
    tags=["Payments"]
)

@router.post("")
def process_payment():
    return {"message": "결제가 안전하게 완료되었습니다! 💳"}