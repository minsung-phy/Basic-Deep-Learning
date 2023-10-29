import matplotlib.pyplot as plt
import numpy as np

Nt = 1000
dx = 0.001

x = np.empty(Nt, float)
y = np.empty(Nt, float)

x[0] = 0
y[0] = 0

for n in range(Nt - 1):
    y[n+1] = y[n] + dx
    x[n+1] = x[n] + dx

plt.plot(x, y)
plt.show()
