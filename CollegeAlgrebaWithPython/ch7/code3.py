import matplotlib.pyplot as plt
from ipywidgets import interactive
import numpy as np

def f(m: float, b: float, zoom: float) -> None:
    """plot graph with slope and intercept, use zoom to control the range of axises"""
    xmin = -zoom
    xmax = zoom
    ymin = -zoom
    ymax = zoom

    points = 10 * (xmax - ymin)
    x = np.linspace(xmin, xmax, points)

    plt.axis([xmin, xmax, ymin, ymax])
    plt.plot([xmin, xmax], [0, 0], 'k')
    plt.plot([0, 0], [ymin, ymax], 'k')
    plt.title('y = mx + b')

    plt.plot(x, m*x + b)
    plt.show()

# use slider to plot different graphs
interactive_plot = interactive(f, m=(-9, 9), b=(-9, 9), zoom=(1, 100))
interactive_plot