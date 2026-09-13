
import sqlite3
from datetime import datetime
from pathlib import Path


DB_PATH = Path("database/feedback.db")

def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)

def get_count(): 
    conn = get_connection() 
    query = """ SELECT * FROM customer_feedback""" 
    rows = conn.execute(query).fetchall() 
    conn.close() 
    return rows

rows = get_count()

print(
        f"Feedback records: {len(rows)}"
    )
