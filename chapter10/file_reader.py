# file_reader.py 

# with open('pi_digits.txt') as file_object:
# with open('text_files/pi_digits.txt') as file_object:
# file_path = 'c:/users/madhu/projects/pywork/chapter10/text_files/pi_digits.txt'
# file_path = 'c:\\Users\\madhu\\projects\\pywork\\chapter10\\text_files\\pi_digits.txt'
# with open(file_path) as file_object:
#     contents = file_object.read()
# print(contents)
# print(contents.rstrip()) 
    # for line in contents:
    #     print(line.rstrip())

# filename = 'text_files/pi_digits.txt'
filename = 'text_files/pi_million_digits.txt'
with open(filename) as file_object:
    # for line in file_object:
        # print(line)  
    lines = file_object.readlines()
    # for line in lines:
    #     print(line.rstrip())
    pi_string = ''
    for line in lines:
        # pi_string += line.rstrip()
        pi_string += line.strip()
    # print(pi_string)
    print(f"{pi_string[:52]}...")
    print('length:',len(pi_string))

    # birthday = input("Enter your birthday, in the form mmddyy: ")
    birthday = '160498'
    # birthday = '100769'
    if birthday in pi_string:
        find = "Your birthday appears in the first million digits of pi"
        find += f" at position {pi_string.index(birthday)}!"
    else:
       find = "Your birthday does not appear in the first million digits of pi." 
    print(find)

