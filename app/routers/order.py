from fastapi import APIRouter
from pydantic import BaseModel   
from typing import List

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

# 1. Pydantic 요청 스키마 정의
class OrderItem(BaseModel):
    name: str
    price: int

class OrderCreateRequest(BaseModel):
    items: List[OrderItem]
    total_price: int

# 2. 임시 저장용 리스트
orders_db = []
order_id_counter = 1

# 3. 결제 처리 API (POST /orders)
@router.post("")
@router.post("/")  # 슬래시(/) 유무 상관없이 둘 다 받도록 처리
def create_order(order_data: OrderCreateRequest):
    global order_id_counter

    new_order = {
        "order_id": order_id_counter,
        "items": [item.model_dump() for item in order_data.items],
        "total_price": order_data.total_price,
        "status": "PAID"
    }

    orders_db.append(new_order)
    print(f"\n==========================================")
    print(f"🎉 [주문 성공] 번호: #{order_id_counter} | 총액: {order_data.total_price}원")
    print(f"==========================================\n")

    order_id_counter += 1

    return {
        "message": "주문 및 결제가 성공적으로 완료되었습니다! 🍜",
        "order_id": new_order["order_id"],
        "total_price": new_order["total_price"]
    }