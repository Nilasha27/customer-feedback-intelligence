import sqlite3
from datetime import datetime
from pathlib import Path


DB_PATH = Path("database/feedback.db")


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return sqlite3.connect(DB_PATH)

## Insert customer feedback into the database

def insert_customer_feedback(
    feedback_id,
    customer_name,
    feedback_text,
    channel,
    product,
    source="Streamlit"
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO customer_feedback
        (
            feedback_id,
            customer_name,
            feedback_text,
            feedback_date,
            channel,
            product,
            source,
            created_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        feedback_id,
        customer_name,
        feedback_text,
        datetime.now().strftime("%Y-%m-%d"),
        channel,
        product,
        source,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()

## Get unprocessed feedback

def get_unprocessed_feedback(): 
    conn = get_connection() 
    query = """ SELECT cf.feedback_id, cf.customer_name, cf.feedback_text, cf.feedback_date 
    FROM customer_feedback cf 
    LEFT JOIN llm_enriched_feedback ef 
    ON cf.feedback_id = ef.feedback_id 
    WHERE ef.feedback_id IS NULL ORDER BY cf.feedback_id """ 
    rows = conn.execute(query).fetchall() 
    conn.close() 
    return rows

### Insert LLM enrichment into the database

def insert_llm_enrichment(
    feedback_id,
    sentiment,
    category,
    priority,
    summary,
    recommended_action,
    support_ticket_number,
    customer_response
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO llm_enriched_feedback
        (
            feedback_id,
            sentiment,
            category,
            priority,
            summary,
            recommended_action,
            support_ticket_number,
            customer_response,
            processed_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        feedback_id,
        sentiment,
        category,
        priority,
        summary,
        recommended_action,
        support_ticket_number,
        customer_response,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()
