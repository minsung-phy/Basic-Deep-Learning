import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for t in np.arange(-10, 10.1, 0.1):
    x.append(t)
    y.append(1 - t*t)

plt.plot(x, y)
plt.show()