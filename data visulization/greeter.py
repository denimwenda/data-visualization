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