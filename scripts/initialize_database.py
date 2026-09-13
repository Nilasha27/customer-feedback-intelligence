import sqlite3
import pandas as pd
from pathlib import Path
import uuid


# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

CSV_PATH = BASE_DIR / "data" / "reviews.csv"
DB_PATH = BASE_DIR / "database" / "feedback.db"


# ---------------------------------------------------------
# Generate Feedback ID
# ---------------------------------------------------------

def generate_feedback_id(index):

    return f"FB-{index:06d}"


# ---------------------------------------------------------
# Create database
# ---------------------------------------------------------

def create_database():

    # Create database directory
    DB_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Read existing CSV
    df = pd.read_csv(CSV_PATH)

    print(f"Total records found in CSV: {len(df)}")

    # Use only first 100 records
    df = df.head(100).copy()

    print(f"Loading {len(df)} records into database...")

    #Rename columns to match database schema
    df.rename(columns={'review': 'feedback_text'}, inplace=True)


    # -----------------------------------------------------
    # Normalize column names
    # -----------------------------------------------------

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )


    # -----------------------------------------------------
    # Validate required column
    # -----------------------------------------------------

    if "feedback_text" not in df.columns:

        raise ValueError(
            "CSV must contain a 'feedback_text' column."
        )


    # -----------------------------------------------------
    # Add missing columns if necessary
    # -----------------------------------------------------

    if "customer_name" not in df.columns:

        df["customer_name"] = "Anonymous"


    if "feedback_date" not in df.columns:

        df["feedback_date"] = pd.Timestamp.now().date()


    if "channel" not in df.columns:

        df["channel"] = "Historical"


    if "product" not in df.columns:

        df["product"] = "Unknown"


    # -----------------------------------------------------
    # Generate feedback IDs
    # -----------------------------------------------------

    df["feedback_id"] = [
        generate_feedback_id(i + 1)
        for i in range(len(df))
    ]


    # -----------------------------------------------------
    # Connect to SQLite
    # -----------------------------------------------------

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()


    # -----------------------------------------------------
    # Drop existing tables
    # -----------------------------------------------------

    cursor.execute(
        "DROP TABLE IF EXISTS llm_enriched_feedback"
    )

    cursor.execute(
        "DROP TABLE IF EXISTS customer_feedback"
    )


    # -----------------------------------------------------
    # Create customer_feedback table
    # -----------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_feedback (

            feedback_id TEXT PRIMARY KEY,

            customer_name TEXT,

            feedback_text TEXT NOT NULL,

            feedback_date TEXT,

            channel TEXT,

            product TEXT,

            source TEXT,

            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)


    # -----------------------------------------------------
    # Create LLM enriched table
    # -----------------------------------------------------

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS llm_enriched_feedback (

            feedback_id TEXT PRIMARY KEY,

            sentiment TEXT,
            
            category TEXT,

            priority TEXT,

            summary TEXT,

            recommended_action TEXT,

            requires_support BOOLEAN,

            support_ticket_number TEXT,

            customer_response TEXT,

            processed_at TEXT,

            FOREIGN KEY (feedback_id)
                REFERENCES customer_feedback(feedback_id)
        )
    """)


    # -----------------------------------------------------
    # Insert historical feedback
    # -----------------------------------------------------

    for _, row in df.iterrows():

        cursor.execute("""
            INSERT INTO customer_feedback
            (
                feedback_id,
                customer_name,
                feedback_text,
                feedback_date,
                channel,
                product,
                source
            )
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (

            row["feedback_id"],

            row["customer_name"],

            row["feedback_text"],

            str(row["feedback_date"]),

            row["channel"],

            row["product"],

            "Historical CSV"
        ))


    # -----------------------------------------------------
    # Commit
    # -----------------------------------------------------

    conn.commit()


    # -----------------------------------------------------
    # Verify
    # -----------------------------------------------------

    cursor.execute(
        "SELECT COUNT(*) FROM customer_feedback"
    )

    feedback_count = cursor.fetchone()[0]


    cursor.execute(
        "SELECT COUNT(*) FROM llm_enriched_feedback"
    )

    enrichment_count = cursor.fetchone()[0]


    print()
    print("=" * 50)
    print("DATABASE CREATED SUCCESSFULLY")
    print("=" * 50)

    print(f"Database : {DB_PATH}")

    print(
        f"Customer feedback records : {feedback_count}"
    )

    print(
        f"LLM enriched records      : {enrichment_count}"
    )

    print("=" * 50)


    conn.close()


# ---------------------------------------------------------
# Main
# ---------------------------------------------------------

if __name__ == "__main__":

    create_database()

