# greeter.py

# def greet_user():
#     """Display a simple greeting."""
#     print("Hello!")
# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello, {username.title()}!")

# # greet_user()
# greet_user('jesse')
# greet_user('sarah')

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     l_name = input("Last name: ")
#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name.strip().lower() == 'q':
        break
    l_name = input("Last name: ")
    if l_name.strip().lower() == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
