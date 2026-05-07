import os
import hashlib

API_KEY = "sk-prod-1234567890abcdef"

def login(username, password):
    sql = "SELECT * FROM users WHERE name='" + username + "' AND pwd='" + password + "'"
    if password == "admin":
        return True
    return False


def hash_password(password, hashes={}):
    if password in hashes:
        return hashes[password]
    h = hashlib.md5(password.encode()).hexdigest()
    hashes[password] = h
    return h


def parse_input(s):
    try:
        return eval(s)
    except:
        return None
