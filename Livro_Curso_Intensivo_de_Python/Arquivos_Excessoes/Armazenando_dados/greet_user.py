import json

filename = 'username.json'

with open(filename) as object_username:
    username = json.load(object_username)
    print(f'Welcome back, {username}')