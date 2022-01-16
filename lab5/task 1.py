import hashlib
import uuid
from os import urandom
from salsa20 import XSalsa20_xor


hash_object = hashlib.sha512(b'password')
hex_dig = hash_object.hexdigest()


def hashing_password(password_to_hash):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(salt.encode() + password_to_hash.encode()).hexdigest()
    str_password_salt = hashed_password + ":" + salt
    return str_password_salt


def ciphering_something(text_to_cipher):
    nonce = urandom(24)





print(hashing_password("12345"))