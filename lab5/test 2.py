from salsa20 import XSalsa20_xor
from os import urandom
IV = urandom(24)
KEY = urandom(32)
print(KEY)
#KEY = b'*secret**secret**secret**secret*'
ciphertext = XSalsa20_xor(b"IT'S A YELLOW SUBMARINE", IV, KEY)
print(XSalsa20_xor(ciphertext, IV, KEY).decode())
