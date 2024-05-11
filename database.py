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


def add_user(login, password):
    with sqlite3.connect('users.db') as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO users (user_login, user_password) VALUES (?, ?);",
            (login, password))
        connection.commit()


def search_users_db():
    with sqlite3.connect('users.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM users")
        all_results = cursor.fetchall()
    return all_results


def get_dictionary_of_users():
    data = search_users_db()
    result = {}
    for user in data:
        result[user[1]] = (user[2], user[0])
    return result


#
# users_db(users_list)

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

def get_user_id_by_login(login):
    with sqlite3.connect('users.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT user_id FROM users WHERE user_login = ?;", (login,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

# view_users()
