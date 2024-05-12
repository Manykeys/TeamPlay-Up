import sqlite3


def create_messages_table():
    conn = sqlite3.connect('your_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages (
                 id INTEGER PRIMARY KEY,
                 chat_id INTEGER,
                 sender_id INTEGER,
                 message TEXT,
                 timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                 )''')
    conn.commit()
    conn.close()

#create_messages_table()
def add_message(chat_id, sender_id, message):
    conn = sqlite3.connect('your_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO messages (chat_id, sender_id, message) VALUES (?, ?, ?)", (chat_id, sender_id, message))
    conn.commit()
    conn.close()
def get_chat_history(chat_id):
    conn = sqlite3.connect('your_database.db')
    c = conn.cursor()
    c.execute("SELECT sender_id, message, timestamp FROM messages WHERE chat_id = ? ORDER BY timestamp ASC", (chat_id,))
    history = c.fetchall()
    conn.close()
    return history
