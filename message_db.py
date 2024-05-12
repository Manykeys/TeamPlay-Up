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

def view_table_contents(table_name):
    conn = sqlite3.connect('your_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM {}".format(table_name))
    table_contents = c.fetchall()
    conn.close()
    return table_contents

def get_chat_partner_by_id(id):
    partners = set()
    for item in view_table_contents('messages'):
        if str(id) in item[1]:
            partners.add(item[1].split("_")[1] if item[1].split("_")[0] == str(id) else item[1].split("_")[0])
    return list(partners)
