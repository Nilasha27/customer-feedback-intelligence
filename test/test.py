
import sqlite3
from datetime import datetime
from pathlib import Path


DB_PATH = Path("database/feedback.db")

def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)

def get_count(): 
    conn = get_connection() 
    query = """ SELECT category, count(*) as c FROM llm_enriched_feedback group by category order by c desc """ 
    rows = conn.execute(query).fetchall() 
    conn.close() 
    return rows

rows = get_count()
print(rows)
# print(
#         f"Feedback records: {len(rows)}"
#     )
