# multiples_of_ten.py 
number = input("Give me a number, please: ")
number = int(number)

# if number % 10 == 0:
if number % 10:
    print(f"{number} is not a multiple of 10.")
else:
    print(f"{number} is a multiple of 10.") 