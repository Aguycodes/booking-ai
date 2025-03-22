import sqlite3
import pandas as pd

DB_PATH = "data/bookings.db"
HIST_PATH = "data/history.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hotel TEXT,
        arrival_date_year INTEGER,
        arrival_date_month INTEGER,
        arrival_date_day_of_month INTEGER,
        country TEXT,
        adr FLOAT,
        reservation_status INTEGER
    )
    """)
    conn.commit()
    conn.close()

def add_booking(hotel, arrival_date_year, arrival_date_month, arrival_date_day_of_month, country, adr, reservation_status):
    from rag import update_embeddings
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO bookings (hotel, arrival_date_year, arrival_date_month, arrival_date_day_of_month, country, adr, reservation_status) VALUES (?, ?, ?, ?, ?, ?, ?)", (hotel, arrival_date_year, arrival_date_month, arrival_date_day_of_month, country, adr, reservation_status))
    conn.commit()
    conn.close()

    update_embeddings()

def fetch_bookings():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM bookings", conn)
    conn.close()
    return df

#query history
def init_query_history():
    conn = sqlite3.connect(HIST_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS query_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

#save a query and answer
def log_query(question, answer):
    conn = sqlite3.connect(HIST_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO query_history (question, answer) VALUES (?, ?)", (question, answer))

    conn.commit()
    conn.close()

#fetch query history
def fetch_query_history():
    conn = sqlite3.connect(HIST_PATH)
    df = pd.read_sql_query("SELECT * FROM query_history ORDER BY timestamp DESC", conn)
    conn.close()
    return df

if __name__ == "__main__":
    init_db()
    init_query_history()