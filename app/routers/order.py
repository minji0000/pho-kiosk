from fastapi import APIRouter

# 스프링의 @RequestMapping("/api/orders") 와 같은 역할을 합니다!
router = APIRouter(
    prefix="/api/orders",
    tags=["Orders"]  # Swagger UI에서 'Orders' 그룹으로 묶어줘요
)

@router.post("")
def create_order():
    return {"message": "주문이 성공적으로 접수되었습니다! 🍜"}

@router.get("/{order_id}")
def get_order_detail(order_id: int):
    return {
        "order_id": order_id,
        "item": "차돌양지 쌀국수",
        "quantity": 1,
        "status": "PREPARING"
    }