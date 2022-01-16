from os import urandom
from salsa20 import XSalsa20_xor

database_user_cipheredDEK_KEKnonce = []

def ciphering (list_toCipher_key_nonce):
    print("pos417 task2 ciphering income: ", list_toCipher_key_nonce)
    cipher_text = XSalsa20_xor(list_toCipher_key_nonce[0], list_toCipher_key_nonce[2], list_toCipher_key_nonce[1])
    return cipher_text

def deciphering (list_toDecipher_key_nonce):
    print("task2 deciphering income: ", list_toDecipher_key_nonce)
    deciphered = XSalsa20_xor(list_toDecipher_key_nonce[0], list_toDecipher_key_nonce[2], list_toDecipher_key_nonce[1])
    return deciphered

def new_user_envelope (list_user_toCipher):
    nonce = urandom(24)
    key = urandom(32)
    DEK = list_user_toCipher[1]
    #print("new user envelope, nonce: ", nonce, " key: ", key, " DEK: ", DEK)
    cipheredDEK = ciphering([DEK, key, nonce])
    database_user_cipheredDEK_KEKnonce.append([list_user_toCipher[0], cipheredDEK, nonce])
    return key

def return_DEK (list_user_KEK):
    user = []
    for i in database_user_cipheredDEK_KEKnonce:
        if i[0] == list_user_KEK[0]:
            user = i
    #list_key_nonce = list_user_KEK[1].split(":")
    DEK = deciphering([user[1], list_user_KEK[1], user[2]])
    return DEK