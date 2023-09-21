#Data visulization involves exploring data through visual representation
#Ploting a simple line graph
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

#Set chart title and lebal axes.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set size of tick labels
plt.tick_params(axis='both', labelsize=14)

plt.show()