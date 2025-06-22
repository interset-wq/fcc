import matplotlib.pyplot as plt
import numpy as np

x_min = -10
x_max = 10
y_min = -10
y_max = 10

# the number of points
points = 2 * (x_max - x_min)

# use numpy create a lot of x, all of x has the same space with each other
# x is an array
x = np.linspace(x_min, x_max, points)
# print(x)

# y is also an array
y = 2*x + 1
# print(y)

fig, ax = plt.subplots()

# dimensions
plt.axis([x_min, x_max, y_min, y_max])

# labels of axis
ax.set_xlabel('x values')
ax.set_ylabel('y values')

# graph title
ax.set_title('My Graph')

# grid
ax.grid(True)

# set the space between the ticks
ax.set_xticks(np.arange(x_min, x_max, 1))
ax.set_yticks(np.arange(y_min, y_max, 1))

# create a horizonal line and a vertical line
plt.plot([x_min, x_max], [0, 0], 'b')
plt.plot([0, 0], [y_min, y_max], 'b')

# plot x and y
plt.plot(x, y, 'r', label='y=2x+1')

# show the label of the fig, 
# if don't use the function, the label arguement in plt() is useless
plt.legend()

plt.show()