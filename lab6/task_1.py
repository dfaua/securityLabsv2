import hashlib
import sqlite3
import uuid
import string
import random
from os import urandom
from salsa20 import XSalsa20_xor


database = []
database_homecity_phonenumber = []

temp_key = b'"\xee\x93k\xe1C\x96\xa4\xb2\x8a\xe6\x03\xe4\xc9\xd9\xec\xb2zb\x18\xfaO\x11\xc1\x14\x1e\t\xaa\x07v-\xa6'
temp_nonce = b'\x17\xbb\xf2\x8d}\xad\xa7\x81J4f\x03\x0c\xca\xd2g9\x8f\x15"OR\xd0\x15'


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
    #print("ciphering_something_key_nonce income: ", list_tocipher_key_nonce)
    cipher_text = XSalsa20_xor(list_tocipher_key_nonce[0].encode(), list_tocipher_key_nonce[2], list_tocipher_key_nonce[1])
    return cipher_text

def deciphering_something(list_toDecipher_key_nonce):
    #print("pos 1324 deciphering something income: ", list_toDecipher_key_nonce)
    deciphered = XSalsa20_xor(list_toDecipher_key_nonce[1], list_toDecipher_key_nonce[3], list_toDecipher_key_nonce[2])
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

    str_homecity_phonenumber = home_city + ":" + phone_number
    ciphered_homecity_phonenumber = ciphering_something_key_nonce([str_homecity_phonenumber, temp_key, temp_nonce])
    to_db_user_homecity_phonenumber = [user_login, ciphered_homecity_phonenumber]
    database_homecity_phonenumber.append(to_db_user_homecity_phonenumber)

    for i in database:
        print("user, pass", i)
    for i in database_homecity_phonenumber:
        print("hc pn: ", i)
    return "Done"

def check_user(list_login_password_userToCheck):
    user = []
    user_to_check = list_login_password_userToCheck[2]
    #print(list_login_password_userToCheck)
    for i in database:
        #print("I'm in 0001")
        if i[0] == list_login_password_userToCheck[0]:
            #print("in 0002")
            #print(i)
            user = i
    if not user:
        return "No such user"
    deciphered_hash_salt = deciphering_something(user)
    #print("check user -- str to list before decoding: ", deciphered_hash_salt)
    deciphered_hash_salt = deciphered_hash_salt.decode()
    #print("check user -- str to list: ", deciphered_hash_salt)
    #list_hash_salt = deciphered_hash_salt.split(":")
    list_hash_salt = list(deciphered_hash_salt.split(":"))
    list_to_hashing = [list_login_password_userToCheck[1], list_hash_salt[1].encode()]
    hashed_new_pas = hashing_password_salt(list_to_hashing)
    if hashed_new_pas == list_hash_salt[0]:
        login_answer = "user found"
        user_to_check_answer = ""
        user_to_check_from_db = []
        for i in database_homecity_phonenumber:
            if i[0] == user_to_check:
                user_to_check_from_db = i
                str_to_dechiper = user_to_check_from_db[1]
                str_hm_pn_userToCheck = deciphering_something(["", str_to_dechiper, temp_key, temp_nonce])
                list_plain_homecity_phonenumber = str_hm_pn_userToCheck.decode().split(":")
                user_to_check_answer = "User: " + user_to_check + ", Home city: " + list_plain_homecity_phonenumber[0] + ", Phone number: " + list_plain_homecity_phonenumber[1]
            if not user_to_check_from_db:
                user_to_check_answer = "no such user in db"
        return [login_answer, user_to_check_answer]
    else:
        return ["Password is incorrect", ""]






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







