#Start with some designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each design, until none are left
#Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()

    #Simulate creating a 3D print from the design.
    print("Printing model: " + current_design)
    completed_models.append(current_design)

#Display all printed design.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

import turtle

# Create a turtle screen
window = turtle.Screen()

# Create a turtle
my_turtle = turtle.Turtle()

# Set the turtle's shape to "turtle"
my_turtle.shape("turtle")

# Customize the turtle's color and size
my_turtle.color("green")
my_turtle.shapesize(2)

# Move the turtle forward
my_turtle.forward(100)

# Close the window when clicked
window.exitonclick()
import turtle

# Create a turtle screen
window = turtle.Screen()

# Create a turtle
my_turtle = turtle.Turtle()

# Set the turtle's shape to "turtle"
my_turtle.shape("turtle")

# Customize the turtle's color and size
my_turtle.color("green")
my_turtle.shapesize(2)

# Move the turtle forward
my_turtle.forward(100)

# Close the window when clicked
window.exitonclick()