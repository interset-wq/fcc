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
plt.plot([xmin, xmax], [0, 0], 'k')
plt.plot([0, 0], [ymin, ymax], 'k')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('more lines')
ax.set_xticks(np.arange(xmin, xmax, 1))
ax.set_yticks(np.arange(ymin, ymax, 1))

# if an area has two or more colors, the latter will override the former


# line 1
y1 = x + 6
plt.plot(x, y1, 'k', label='y=x+6')
plt.fill_between(x, y1, ymax, facecolor='r')

# line 2
y2 = x + 3
plt.plot(x, y2, 'k')
plt.fill_between(x, y2, y1, facecolor='y')

# line 3
y3 = x - 1
plt.plot(x, y3, 'k')
plt.fill_between(x, y3, y2, facecolor='g')

# line 4
y4 = x - 4
plt.plot(x, y4, 'k')
plt.fill_between(x, y4, y3, facecolor='b')

# plt.legend()
plt.show()