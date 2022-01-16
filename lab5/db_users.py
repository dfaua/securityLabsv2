import sqlite3

db = sqlite3.connect('users_info.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users_info (
login TEXT, 
hash TEXT, 
key_to_hash TEXT,
salt TEXT,
nonce TEXT
)""")
db.commit()

#user_login = input('Login: ')
#user_password = input('Password: ')

def new_user(list_login_hash_key_salt_nonce):
    login = list_login_hash_key_salt_nonce[0]
    hash_pas = list_login_hash_key_salt_nonce[1]
    key_hash = list_login_hash_key_salt_nonce[2]
    salt = list_login_hash_key_salt_nonce[3]
    nonce = list_login_hash_key_salt_nonce[4]
    sql.execute("SELECT login from users_info WHERE login = '{login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users_info VALUES(?, ?, ?, ?, ?)", (login, hash_pas, key_hash, salt, nonce))
        db.commit()
        print(1)
    else:
        print(0)

def check_user(login):
    sql.execute("SELECT login from users_info WHERE login = '{login}'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO users_info VALUES(?, ?, ?, ?, ?)", (login, hash_pas, key_hash, salt, nonce))
        db.commit()
        print(1)
    else:
        print(0)


sql.execute("SELECT login from users WHERE login = '{user_login}'")
if sql.fetchone() is None:
    sql.execute(f"INSERT INTO users VALUES(?, ?, ?)", (user_login, user_password, 0))
    db.commit()
    print("Registered")
else:
    print("Already exists")

for value in sql.execute("SELECT * FROM users"):
    print(value)