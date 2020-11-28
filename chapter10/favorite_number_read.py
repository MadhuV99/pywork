# favorite_number_read.py

import json

with open('text_files/favorite_number.json') as f:
    number = json.load(f)

print(f"I know your favorite number! It's {number}.")