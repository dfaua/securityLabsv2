from os import urandom

print("nonce: ", urandom(24))
print("key: ", urandom(32))