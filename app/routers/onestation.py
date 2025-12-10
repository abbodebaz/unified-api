from fastapi import APIRouter
from app.db import get_connection

router = APIRouter()

@router.get("/onestation/order/{sales_order}")
def get_order_by_id(sales_order: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM one_station
        WHERE Sales_order = %s
    """, (sales_order,))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"count": len(data), "data": data}


@router.get("/onestation/phone/{phone}")
def get_order_by_phone(phone: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM one_station
        WHERE phone_number LIKE %s
    """, ("%" + phone + "%",))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"count": len(data), "data": data}
