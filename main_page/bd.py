import sqlite3

db1_connect = sqlite3.connect('users.db')
db1_cursor = db1_connect.cursor()

users_list = [
    (1, 'Firchalka', 'Nikta2004'),
    (2, 'Sanya', 'Artem13Chlen'),
]

def users_db(data_of_users):
    db1_cursor.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        user_login TEXT,
        user_password TEXT
    )
    """)
    db1_cursor.executemany("INSERT INTO users VALUES(?,?,?);", users_list)
    db1_connect.commit()


users_db(users_list)

def view_users():
    db1_cursor.execute("SELECT * FROM users")
    rows = db1_cursor.fetchall()
    if rows:
        print("User ID | User Login | User Password")
        print("-------------------------------------")
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]}")
    else:
        print("Таблица пользователей пуста.")


view_users()
