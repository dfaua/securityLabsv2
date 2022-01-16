import sqlite3
from sqlalchemy import create_engine

db = sqlite3.connect('users_info.db')
sql = db.cursor()
engine=create_engine('sqlite:///users_info.db', echo=True, connect_args={"check_same_thread": False})

sql.execute("""CREATE TABLE IF NOT EXISTS users_info (
login TEXT, 
hash_salt_ciphered TEXT, 
key_to_ciphering TEXT,
nonce TEXT
)""")
db.commit()

#user_login = input('Login: ')
#user_password = input('Password: ')

def new_user(list_login_cipher_key_nonce):
    login = list_login_cipher_key_nonce[0]
    hash_salt_ciphered = list_login_cipher_key_nonce[1]
    key_to_ciphering = list_login_cipher_key_nonce[2]
    nonce = list_login_cipher_key_nonce[3]
    sql.execute("SELECT login FROM users_info")
    sql.execute(f"INSERT INTO users_info VALUES(?, ?, ?, ?)", (login, hash_salt_ciphered, key_to_ciphering, nonce))
    db.commit()

def check_user(login):
    sql.execute("SELECT login FROM users_info WHERE login = '{login}'")
    for line in sql.execute("SELECT * FROM users_info"):
        if line[0] == login:
            return line

