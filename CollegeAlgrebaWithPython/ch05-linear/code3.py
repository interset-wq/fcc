import matplotlib.pyplot as plt
import numpy as np

"""the equation"""
x1 = 0 # use 0 to express 2010
y1 = 55 # use 55 to express 55,000
x2 = 2
y2 = 76

# slope and y-interception
m = (y2 - y1) / (x2 - x1)
b = y1 - m*x1

print(f'y = {m}*x + {b}')

"""matplotlib"""
x_min = 0
x_max = 10
y_min = 40
y_max = 150

fig, ax = plt.subplots()
plt.axis([x_min, x_max, y_min, y_max])

ax.set_xlabel('years')
ax.set_ylabel('popularity')
ax.set_title('the popularity of a city')
ax.grid(True)
ax.set_xticks(np.arange(x_min, x_max, 1))
ax.set_yticks(np.arange(y_min, y_max, 10))

# line
y3 = m*x_min + b
y4 = m*x_max +b

plt.plot([x_min, x_max], [y3, y4], 'r')


plt.show()