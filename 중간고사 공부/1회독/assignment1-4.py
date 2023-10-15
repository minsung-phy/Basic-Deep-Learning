import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for t in np.arange(-3.14, 3.14, 0.1):
    x.append(t)
    y.append(t*t)

plt.plot(x, y)
plt.show()