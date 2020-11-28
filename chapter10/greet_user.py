# greet_user.py 

import json
filename = 'username.json'
with open('text_files/'+filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")