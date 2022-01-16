import hashlib
import sqlite3
import uuid
import string
import random
from os import urandom
from salsa20 import XSalsa20_xor
from db_users import new_user, check_user

database = []


def hashing_password(password_to_hash):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(salt.encode() + password_to_hash.encode()).hexdigest()
    str_password_salt = hashed_password + ":" + salt
    return str_password_salt


def ciphering_something(text_to_cipher):
    nonce = urandom(24)
    key = urandom(32)
    cipher_text = XSalsa20_xor(text_to_cipher.encode(), nonce, key)
    list_cipher_key_nonce = [cipher_text, key, nonce]
    return list_cipher_key_nonce


def deciphering_something(list_to_decipher):
    deciphered = XSalsa20_xor(list_to_decipher[0], list_to_decipher[])
    return


def registration(list_login_password):
    #print("YESSSS")
    user_login = list_login_password[0]
    user_password = list_login_password[1]
    str_password_salt = hashing_password(user_password)
    list_cipher_key_nonce = ciphering_something(str_password_salt)
    list_login_hash_key_nonce = [user_login, list_cipher_key_nonce[0], list_cipher_key_nonce[1], list_cipher_key_nonce[2]]
    database.append(list_login_hash_key_nonce)
    for i in database:
        print(i)
    return "Done"

def check_user(list_login_password):
    user = []
    for i in database:
        if i[1] == list_login_password[0]:
            user = i
    if range(user) == 0:
        return "No such user"






#pas = "12324tgef12f"
#print("pas: ", pas)
#hashed_pas = hashing_password(pas)
#print("hashed pas: ", hashed_pas)
#cipher_key_nonce = ciphering_something(hashed_pas)
#print("cipher, key, nonce: ", cipher_key_nonce)

#def registration(list_login_password):
    #conn = sqlite3.connect('users_info.db', check_same_thread=False)
    #user_login = list_login_password[0]
    #user_password = list_login_password[1]
    #str_password_salt = hashing_password(user_password)
    #list_cipher_key_nonce = ciphering_something(str_password_salt)
    #list_login_hash_key_salt_nonce = [user_login, list_cipher_key_nonce[0], list_cipher_key_nonce[1], list_cipher_key_nonce[2]]
    #result = new_user(list_login_hash_key_salt_nonce)
    #return "Done"







