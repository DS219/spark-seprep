# Hanifa Safdari

Hi, my name is Hanifa Safdari, and my favorite programming language is Python because it is easy to learn and code in.

Example code  

import matplotlib.pyplot as plt
import numpy as np

my_points = np.array([[2, 1],  [3, 4],  [5, 6]])

plt.plot(my_points[:, 0], my_points[:, 1], 'ro')

myfit_x = np.linspace(11, 4, 100)
myfit_y = np.linspace(1, 5, 100) # Same y/x slope for all segments - so, a line
plt.plot(myfit_x, myfit_y)
plt.show()

Code explantion

This code makes a simple graph by marking three red dots and drawing a straight line through the plot.
