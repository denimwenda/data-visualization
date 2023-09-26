import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

x_labels = np.array([0, 6])
y_labels = np.array([0, 250])

plt.plot(x_labels, y_labels)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()