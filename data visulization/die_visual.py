import pygal
from die import Die

die = Die()          # Create an instance with default 6 sides
results = []    # Create an empty list to store results

# Make some rolls and show the results in a list
for roll_num in range(1000):
    result = die.roll()  # Roll the die and store the result in 'result'
    results.append(result)  # Append the result to the list

#Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()

hist.title = "Results for rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')