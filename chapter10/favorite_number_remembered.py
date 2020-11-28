# favorite_number_remembered.py 
import json

filename = 'text_files/favorite_number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open(filename, 'w') as f:
        json.dump(number, f)
    print("Thanks, I'll remember that.")
else:
    print(f"I know your favorite number! It's {number}.") 
