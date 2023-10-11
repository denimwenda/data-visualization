#defining a function
def greet_user():
    """Display a simple greeting"""
    print("Hello!")

greet_user()

#Passing information to a function
def greet_user(username):
    """Display a simple greeting"""
    print("Hello, " + username + "!")

greet_user('denny')

def dislay_message():
    """Display a simple information"""
    print("I am learning about functions!")

dislay_message()

def favorite_book(title):
    """Display a book title"""
    print("My favorite book is " + title + "!")

favorite_book('The Reverse Call')

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

#This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")