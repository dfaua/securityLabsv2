import sqlite3

db = sqlite3.connect('users.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT,
    hesh TEXT,
    key TEXT,
    salt TEXT,
    nonce TEXT
)""")

db.commit()

user_login = input('Login: ')
user_password = input('Password: ')