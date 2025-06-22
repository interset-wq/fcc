import matplotlib.pyplot as plt

"""The equation"""
x1 = 1
y1 = 3
x2 = 4
y2 = 9

# the slope is m
m = (y2 - y1) / (x2 - x1)

# y intercept is b
b = y1 - m*x1
print(f'The equation is y = {m}*x + {b}')

"""set some varieties to express the range of x-axis and y-axis"""
x_min = -10
x_max = 10
y_min = -10
y_max = 10

"""matplotlib"""
fig, ax = plt.subplots()

plt.axis([x_min, x_max, y_min, y_max])

# y-axis and x-axis
plt.plot([0, 0], [y_min, y_max], 'b')
plt.plot([x_min, x_max], [0, 0], 'b')

# plot more the line
y3 = m*x_min + b
y4 = m*x_max + b

plt.plot([x_min, x_max], [y3, y4], 'r')

plt.show()