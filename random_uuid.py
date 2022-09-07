from uuid import uuid4

rand_token = uuid4()
print(rand_token)


import secrets

x = secrets.token_hex(20)
print(x)