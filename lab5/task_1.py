import hashlib
import uuid
import string
import random
from os import urandom
from salsa20 import XSalsa20_xor


hash_object = hashlib.sha512(b'password')
hex_dig = hash_object.hexdigest()
database = {}

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


def registration(list_login_password):
    database[list_login_password[0]] = list_login_password[1]
    print(database)
    return "You are successfully registered"

pas = "12324tgef12f"
print("pas: ", pas)
hashed_pas = hashing_password(pas)
print("hashed pas: ", hashed_pas)
cipher_key_nonce = ciphering_something(hashed_pas)
print("cipher, key, nonce: ", cipher_key_nonce)


