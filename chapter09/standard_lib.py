# standard_lib.py 

# from random import randint
# for i in range(10):
#     print(randint(1, 6))

from random import choice
players = ['maradona', 'charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)