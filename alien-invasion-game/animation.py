import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create a figure and axis
fig, ax = plt.subplots()

# Define the number of frames and the interval between frames
num_frames = 100
interval = 100  # in milliseconds

# Initialize the data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a line plot
line, = ax.plot(x, y)

# Function to update the plot for each frame
def update(frame):
    line.set_ydata(np.sin(x + frame * 0.1))  # Update the y-data
    return line,

# Create an animation object
ani = animation.FuncAnimation(fig, update, frames=num_frames, interval=interval)

# Display the animation (this opens a window)
plt.show()