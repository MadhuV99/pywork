# cats_and_dogs.py

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    # print(f"\nReading file: {filename}")
    # try:
    #     with open('text_files/'+filename) as f:
    #         contents = f.read()
    #         print(contents)
    # except FileNotFoundError:
    #     print("  Sorry, I can't find that file.")

    try:
        with open('text_files/'+filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents)    