from os import urandom
from salsa20 import XSalsa20_xor

database_user_cipheredDEK = []

def ciphering (list_toCipher_key_nonce):
    cipher_text = XSalsa20_xor(list_toCipher_key_nonce[0].encode(), list_toCipher_key_nonce[2], list_toCipher_key_nonce[1])
    return cipher_text

def deciphering (list_toDecipher_key_nonce):
    deciphered = XSalsa20_xor(list_toDecipher_key_nonce[0], list_toDecipher_key_nonce[2], list_toDecipher_key_nonce[1])
    return deciphered

def new_user_envelope (list_user_toCipher):
    nonce = urandom(24)
    key = urandom(32)
    cipheredDEK = ciphering(list_user_toCipher[1], key, nonce)
    database_user_cipheredDEK.append([list_user_toCipher[0], cipheredDEK])
    KEK = key + ":" + nonce
    return KEK

def return_DEK (list_user_KEK):
    user = []
    for i in database_user_cipheredDEK:
        if i[0] == list_user_KEK[0]:
            user = i
    list_key_nonce = list_user_KEK[1].split(":")
    DEK = deciphering(user[1], list_key_nonce[1], list_key_nonce[0])
    return DEK