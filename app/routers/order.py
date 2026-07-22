from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)

# --------------------------------------------------
# [1] Request/Response 데이터 구조 정의 (Pydantic)
# --------------------------------------------------

# 주문에 담길 개별 메뉴 아이템
class OrderItem(BaseModel):
    name: str      # 메뉴 이름 (예: '매운 쌀국수')
    price: int     # 가격 (예: 10000)

# 결제 요청 시 백엔드로 넘어오는 전체 주문 데이터
class OrderCreateRequest(BaseModel):
    items: List[OrderItem]  # 선택한 메뉴 목록
    total_price: int        # 총 결제 금액

# --------------------------------------------------
# [2] 가짜 DB (메모리 저장소)
# --------------------------------------------------
orders_db = []
order_id_counter = 1

# --------------------------------------------------
# [3] 주문 결제 처리 API (POST /orders)
# --------------------------------------------------
@router.post("")
def create_order(order_data: OrderCreateRequest):
    global order_id_counter

    # 1. 새로운 주문 객체 생성
    new_order = {
        "order_id": order_id_counter,
        "items": order_data.items,
        "total_price": order_data.total_price,
        "status": "PAID"  # 결제 완료 상태
    }

    # 2. 가짜 DB에 저장
    orders_db.append(new_order)

    print(f"NEW ORDER RECEIVED! [주문번호 #{order_id_counter}] 총액: {order_data.total_price}원")

    # 3. 주문 번호 증가
    order_id_counter += 1

    # 4. 프론트엔드로 성공 응답 전달
    return {
        "message": "주문 및 결제가 성공적으로 완료되었습니다! 🍜",
        "order_id": new_order["order_id"],
        "total_price": new_order["total_price"]
    }