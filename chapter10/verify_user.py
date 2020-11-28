# verify_user.py 
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'text_files/username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'text_files/username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

# def greet_user():
#     """Greet the user by name."""
#     username = get_stored_username()
#     if username:
#         correct = input(f"Are you {username}? (y/n) ")
#         if correct.strip().lower() == 'y':
#             print(f"Welcome back, {username}!")
#         else:
#             username = get_new_username()
#             print(f"We'll remember you when you come back, {username}!")
#     else:
#         username = get_new_username()
#         print(f"We'll remember you when you come back, {username}!")

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
            return

    # We got a username, but it's not correct.
    # Let's prompt for a new username.
    username = get_new_username()
    print(f"We'll remember you when you come back, {username}!") 
    
greet_user()
