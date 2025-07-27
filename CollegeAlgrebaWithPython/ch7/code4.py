import matplotlib.pyplot as plt
from meteostat import Point, Daily
from datetime import datetime

start = datetime(2025, 1, 1)
end = datetime(2025, 5, 20)

philly = Point(39.97, -75.13, 25)

data = Daily(philly, start, end)
data = data.fetch()

data.plot(y=['tavg', 'tmin', 'tmax'])
plt.show()