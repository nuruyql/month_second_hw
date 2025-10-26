# import sqlite3
#
# def create_table(conn):
#     conn.execute('''
#     CREATE TABLE IF NOT EXISTS users(
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER
#     )
#     ''')
#
# def add_user(conn, name, age):
#     conn.execute("""
#     INSERT INTO users (name, age)
#     VALUES(?, ?)
#     """, (name, age))
#     conn.commit()
#
# if __name__ == "__main__":
#     conn = sqlite3.connect("database.db")
#     create_table(conn)
#
#     add_user(conn, "Nurbol", 17)
#     add_user(conn, "Aza", 18)
#     add_user(conn, "Akjol", 15)
#     add_user(conn, "Nurbolot", 19)
#     add_user(conn, "Nurgul", 15)
#
#     conn.close()
