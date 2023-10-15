import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for t in np.arange(0, 10, 0.5):
    x.append(t)
    y.append(t*t)

plt.subplot(1, 2, 1)
plt.scatter(x, y)
plt.title("scatter graph")

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("plot graph")

plt.show()
