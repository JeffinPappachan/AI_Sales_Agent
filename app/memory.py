import sqlite3

conn = sqlite3.connect("conversations.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS conversations (
    lead_id TEXT,
    role TEXT,
    message TEXT
)
""")
conn.commit()

def save_message(lead_id, role, message):
    cursor.execute(
        "INSERT INTO conversations VALUES (?, ?, ?)",
        (lead_id, role, message)
    )
    conn.commit()

def get_last_messages(lead_id, limit=5):
    cursor.execute(
        "SELECT role, message FROM conversations WHERE lead_id=? ORDER BY rowid DESC LIMIT ?",
        (lead_id, limit)
    )
    rows = cursor.fetchall()
    return rows[::-1]
