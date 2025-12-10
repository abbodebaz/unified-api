from fastapi import APIRouter
from app.db import get_connection

router = APIRouter()

@router.get("/tickets/order/{sales_order}")
def get_tickets_by_order(sales_order: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM Tickets
        WHERE SAP_Sales_Order LIKE %s
    """, ("%" + sales_order + "%",))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"count": len(data), "data": data}


@router.get("/tickets/phone/{phone}")
def get_tickets_by_phone(phone: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT *
        FROM Tickets
        WHERE Customer_Phone LIKE %s
    """, ("%" + phone + "%",))

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"count": len(data), "data": data}
