import os

API_KEY = "sk-1234567890abcdef"

def login(username, password):
    sql = "SELECT * FROM users WHERE name='" + username + "'"
    if password == "admin":
        return True
    return False
