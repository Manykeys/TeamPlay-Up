import sqlite3

dota_connect = sqlite3.connect('dota.db')
dota_cursor = dota_connect.cursor()

dota_list = [
    (1, 4000, 'Лирой', 'Ищу друзей', "Carry"),
    (2, 3500, 'Саня', 'Ищу друзей', "Support"),
    (3, 4500, 'Хуй', 'Ищу друзей', "Mid"),
]

dota_pos = ['Carry', 'Mid', "Offlainer", "Semi_sup", "Full_sup"]

def dota_db(data_of_dota):
    dota_cursor.execute("""CREATE TABLE IF NOT EXISTS dota(
        user_id KEY,
        user_MMR INTEGER,
        user_nickname TEXT,
        user_comment TEXT,
        user_pos TEXT
    )
    """)
    dota_cursor.executemany("INSERT INTO dota VALUES(?,?,?,?,?);", dota_list)
    dota_connect.commit()

#dota_db(dota_list)

def view_dota():
    dota_cursor.execute("SELECT * FROM dota")
    rows = dota_cursor.fetchall()
    if rows:
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")
            
def search_dota_db():
    with sqlite3.connect('dota.db') as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM dota")
        all_results = cursor.fetchall()
    return all_results


def get_dictionary_of_quest():
    data = search_dota_db()
    result = {}
    for user in data:
        result[user[2]] = (user[0], user[1], user[3], user[4])
    return result

def filter_by_mmr_and_position(min_mmr=None, max_mmr=None, position=None):
    with sqlite3.connect('dota.db') as connection:
        cursor = connection.cursor()
        if min_mmr is not None and max_mmr is not None and position is not None:
            cursor.execute("SELECT * FROM dota WHERE user_MMR BETWEEN ? AND ? AND user_pos = ?", (min_mmr, max_mmr, position))
        elif min_mmr is not None and max_mmr is not None:
            cursor.execute("SELECT * FROM dota WHERE user_MMR BETWEEN ? AND ?", (min_mmr, max_mmr))
        elif position is not None:
            cursor.execute("SELECT * FROM dota WHERE user_pos = ?", (position,))
        else:
            cursor.execute("SELECT * FROM dota")
        filtered_results = cursor.fetchall()
    return filtered_results


def filter_by_mmr(min_mmr, max_mmr):
    with sqlite3.connect('dota.db') as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM dota WHERE user_MMR BETWEEN ? AND ?", (min_mmr, max_mmr))
        filtered_results = cursor.fetchall()
    return filtered_results

def add_application(user_id, user_MMR, user_nickname, user_comment, user_pos):
    with sqlite3.connect('dota.db') as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO dota (user_id, user_MMR, user_nickname, user_comment, user_pos) VALUES (?, ?, ?, ?, ?);",
                       (user_id, user_MMR, user_nickname, user_comment, user_pos))
        connection.commit()

print(get_dictionary_of_quest())
#view_dota()