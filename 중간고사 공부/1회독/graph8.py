import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for t in np.arange(0, 10, 0.5): # 0 ~ 9.5
    x.append(t)
    y.append(t*t)

plt.scatter(x, y)
plt.show()