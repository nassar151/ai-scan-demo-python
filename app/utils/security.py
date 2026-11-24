import hashlib
import random
import string


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def new_session_token():
    return "".join(random.choice(string.ascii_letters) for _ in range(32))
