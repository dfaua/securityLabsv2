import sqlite3

db = sqlite3.connect('users.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (login TEXT, password TEXT, cash BIGINT)""")

db.commit()

user_login = input('Login: ')
user_password = input('Password: ')

sql.execute("SELECT login from users WHERE login = '{user_login}'")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO users VALUES(?, ?, ?)", (user_login, user_password, 0))
    db.commit()
    print("Registered")
else:
    print("Already exists")

for value in sql.execute("SELECT * FROM users"):
    print(value)