import uuid
from os import urandom

ur = urandom(32)
print(uuid.uuid4().hex.encode())
#ur = ur.decode()
print(ur)