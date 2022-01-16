import hashlib
import sqlite3
import uuid
import string
import random
from os import urandom
from salsa20 import XSalsa20_xor


database = []
database_homecity_phonenumber = []


def hashing_password(password_to_hash):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(salt.encode() + password_to_hash.encode()).hexdigest()
    str_password_salt = hashed_password + ":" + salt
    return str_password_salt

def hashing_password_salt(list_password_salt):
    print("hashing password salt income: ", list_password_salt)
    hashed_password = hashlib.sha512(list_password_salt[1] + list_password_salt[0].encode()).hexdigest()
    return hashed_password


def ciphering_something(text_to_cipher):
    nonce = urandom(24)
    key = urandom(32)
    cipher_text = XSalsa20_xor(text_to_cipher.encode(), nonce, key)
    list_cipher_key_nonce = [cipher_text, key, nonce]
    return list_cipher_key_nonce

def ciphering_something_key_nonce(list_tocipher_key_nonce):
    cipher_text = XSalsa20_xor(list_tocipher_key_nonce[0].encode(), list_tocipher_key_nonce[1].encode(), list_tocipher_key_nonce[2].encode())
    return cipher_text

def deciphering_something(list_to_decipher):
    print("deciphering something income: ", list_to_decipher)
    deciphered = XSalsa20_xor(list_to_decipher[1], list_to_decipher[3], list_to_decipher[2])
    return deciphered


def registration(list_login_password_homecity_phonenumber):
    #print("YESSSS")
    user_login = list_login_password_homecity_phonenumber[0]
    user_password = list_login_password_homecity_phonenumber[1]
    home_city = list_login_password_homecity_phonenumber[2]
    phone_number = list_login_password_homecity_phonenumber[3]
    str_password_salt = hashing_password(user_password)
    list_cipher_key_nonce = ciphering_something(str_password_salt)
    list_login_hash_key_nonce = [user_login, list_cipher_key_nonce[0], list_cipher_key_nonce[1], list_cipher_key_nonce[2]]
    database.append(list_login_hash_key_nonce)

    key = "\xbf)J\xe1Lv\x1amS\x86\xa2\xff*\xce\xfc\x99k0\xc2w>\xd7\x1c\xf0\xa6\xa4\xc3\x96m\x84\xf3I".encode()
    nonce = "b\x8f'm7\x14<\x00l=;\xd0,\x13d\x81e\x92|\xddic\xb1\t".encode()

    str_homecity_phonenumber = home_city + ":" + phone_number
    ciphered_homecity_phonenumber = ciphering_something_key_nonce([str_homecity_phonenumber, key, nonce])
    to_db_user_homecity_phonenumber = [user_login, ciphered_homecity_phonenumber]

    for i in database:
        print(i)
    return "Done"

def check_user(list_login_password):
    user = []
    print(list_login_password)
    for i in database:
        print("I'm in 0001")
        if i[0] == list_login_password[0]:
            print("in 0002")
            print(i)
            user = i
    if not user:
        return "No such user"
    deciphered_hash_salt = deciphering_something(user)
    #print("check user -- str to list before decoding: ", deciphered_hash_salt)
    deciphered_hash_salt = deciphered_hash_salt.decode()
    #print("check user -- str to list: ", deciphered_hash_salt)
    #list_hash_salt = deciphered_hash_salt.split(":")
    list_hash_salt = list(deciphered_hash_salt.split(":"))
    list_to_hashing = [list_login_password[1], list_hash_salt[1].encode()]
    hashed_new_pas = hashing_password_salt(list_to_hashing)
    if hashed_new_pas == list_hash_salt[0]:
        return "User found"
    else:
        return "Password is incorrect"






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







