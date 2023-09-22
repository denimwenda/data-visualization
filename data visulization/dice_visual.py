import pygal
from die import Die

#Create two D6 dice.
die_1 = Die()
die_2 = Die()

results = []    # Create an empty list to store results

# Make some rolls and show the results in a list
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() # Roll the die and store the result in 'result'
    results.append(result)  # Append the result to the list

#Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()

hist.title = "Results for rolling two D6 dice 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')