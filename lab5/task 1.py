import hashlib
import uuid
from simpl


hash_object = hashlib.sha512(b'password')
hex_dig = hash_object.hexdigest()


def hashing_password(password_to_hash):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(salt.encode() + password_to_hash.encode()).hexdigest()
    list_password_salt = [hashed_password, salt]
    return list_password_salt




print(hashing_password("12345"))