from fastapi import APIRouter
from app.db import get_connection

router = APIRouter()

@router.get("/ahd/order/{sales_order}")
def get_ahd_by_order(sales_order: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM Ahd
        WHERE Sales_order = %s
    """, (sales_order,))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"count": len(data), "data": data}


@router.get("/ahd/phone/{phone}")
def get_ahd_by_phone(phone: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM Ahd
        WHERE phone_number LIKE %s
    """, ("%" + phone + "%",))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"count": len(data), "data": data}
