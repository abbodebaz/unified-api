from fastapi import APIRouter
from app.db import get_connection

router = APIRouter(prefix="/unified", tags=["Unified Search"])

@router.get("/{query}")
def unified_search(query: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    results = {
        "onestation": [],
        "ahd": [],
        "tickets": [],
    }

    # OneStation search
    cursor.execute("""
        SELECT * FROM onestation
        WHERE Sales_order = %s OR phone_number = %s
    """, (query, query))
    results["onestation"] = cursor.fetchall()

    # AHD search
    cursor.execute("""
        SELECT * FROM ahd
        WHERE Sales_order = %s OR phone_number = %s
    """, (query, query))
    results["ahd"] = cursor.fetchall()

    # Tickets search
    cursor.execute("""
        SELECT * FROM tickets
        WHERE SAP_Sales_Order = %s OR Customer_Phone = %s
    """, (query, query))
    results["tickets"] = cursor.fetchall()

    conn.close()

    return results
