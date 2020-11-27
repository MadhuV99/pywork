# guest.py

name = input("What's your name? ")
filename = 'text_files/guest.txt'
with open(filename, 'w') as f:
    f.write(name) 