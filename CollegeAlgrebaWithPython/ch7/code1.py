import matplotlib.pyplot as plt
import numpy as np

xmin = -10
xmax = 10
ymin = -10
ymax = 10

# if the line is not linear, we need more points
points = 10 * (xmax - xmin)
x = np.linspace(xmin, xmax, points)

plt.rcParams['font.sans-serif'] = ['SimHei'] # 解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False # 解决负号显示问题

fig, ax = plt.subplots()

plt.axis([xmin, xmax, ymin, ymax])
plt.plot([xmin, xmax], [0, 0], 'b')
plt.plot([0, 0], [ymin, ymax], 'b')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('two line')

# line 1
y = 2 * x
plt.plot(x, y, 'y')

# line 2
y = x**2 - 3
plt.plot(x, y, 'g')

plt.show()