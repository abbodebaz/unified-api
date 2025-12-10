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

    # ========================
    # 🔵 1) OneStation search
    # ========================
    cursor.execute("""
        SELECT * FROM one_station
        WHERE Sales_order = %s OR phone_number = %s
    """, (query, query))
    results["onestation"] = cursor.fetchall()

    # ========================
    # 🔵 2) AHD search
    # ========================
    cursor.execute("""
        SELECT * FROM Ahd
        WHERE Sales_order = %s OR phone_number = %s
    """, (query, query))
    results["ahd"] = cursor.fetchall()

    # ========================
    # 🔵 3) Tickets search
    # ========================
    cursor.execute("""
        SELECT * FROM Tickets
        WHERE SAP_Sales_Order = %s OR Customer_Phone = %s
    """, (query, query))
    results["tickets"] = cursor.fetchall()

    conn.close()

    return {
        "query": query,
        "sources": results
    }
