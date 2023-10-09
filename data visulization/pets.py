#Passing functions.
#You can pass either through positional or keyword arguments.
#Positional arguments are written in same way the parameters were written.
#Keyword arguments consists of a variable and a value

#Example of positinal arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + "!")
    print("My " + animal_type + "'s name is " + pet_name.title() + "!")

describe_pet('hamster', 'jonny')
describe_pet('cat', 'rean')

#Example of keyword arguments.
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + "!")
    print("My " + animal_type + "'s name is " + pet_name.title() + "!")

describe_pet(animal_type='german shepherd', pet_name='alan')
describe_pet(pet_name='alan', animal_type='german shepherd')

#Setting a default value.
def describe_pet(pet_name, animal_type='dog'):
    print("\nI have a " + animal_type + "!")
    print("My " + animal_type + "'s name is " + pet_name.title() + "!")

describe_pet(pet_name='Willie')

def make_shirt(size, text):
    """Display inormation about a shirt"""
    print("\nMy shirt size is " + size + "!")
    print("The text printed is " + text + "!")

make_shirt('medium', "i love programming")
make_shirt(size='medium', text='i love programming')

def describe_city(city, country='Kenya'):
    """Display information about a city"""
    print(city + " is in " + country + "!")

describe_city(city='Nairobi')
describe_city(city='Mombasa')
describe_city(city='Eldoret')

def make_shirt(text, size='large'):
    print("\nMy shirt size is " + size + "!")
    print("The text printed on the shirt is " + text + "!")

make_shirt(text='I love python')