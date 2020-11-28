# favorite_number_write.py

import json

number = input("What's your favorite number? ")

with open('text_files/favorite_number.json', 'w') as f:
    json.dump(number, f)
    print("Thanks! I'll remember that.")