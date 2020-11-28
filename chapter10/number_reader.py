# number_reader.py
import json

filename = 'numbers.json'
with open('text_files/'+filename) as f:
    numbers = json.load(f)
    print(numbers)