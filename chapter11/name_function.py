# name_function.py 

# def get_formatted_name(first, last):
# def get_formatted_name(first, middle, last):
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    # full_name = f"{first} {last}"
    # full_name = f"{first} {middle} {last}"
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title() 
    