import sqlite3
from datetime import datetime


def save_history(
        test_name,
        status,
        execution_time
):

    conn = sqlite3.connect(
        "test_history.db"
    )

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history(
        id INTEGER PRIMARY KEY,
        test_name TEXT,
        date TEXT,
        status TEXT,
        execution_time TEXT
    )
    """)


    cursor.execute(
    """
    INSERT INTO history
    VALUES(NULL,?,?,?,?)
    """,
    (
        test_name,
        datetime.now(),
        status,
        execution_time
    ))

    conn.commit()

    conn.close()