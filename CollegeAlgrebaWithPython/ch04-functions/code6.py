import matplotlib.pyplot as plt

x_min = -10
x_max = 10
y_min = -10
y_max = 10

fig, ax = plt.subplots()

# 设置坐标轴刻度范围
plt.axis([x_min, x_max, y_min, y_max])

# 通过(x_min, 0)和(x_max, 0)绘制一条横线
# 'b'表示'blue'蓝色
plt.plot([x_min, x_max], [0, 0], 'b')

# 通过(0, y_min)和(0, y_max)绘制一条熟悉那
plt.plot([0, 0], [y_min, y_max], 'b')

# 绘制一个点(5, 4)
# 'ro'中的'r'表示'red'红色，'o'表示圆圈⭕
plt.plot([5], [4], 'ro')

# plot a line
plt.plot([0, 10], [0, 10], 'r')

# 根据函数关系绘制多个点
for x in range(10):
    y = 0.5*x + 1
    plt.plot([x], [y], 'yo')

# show the graph
plt.show()