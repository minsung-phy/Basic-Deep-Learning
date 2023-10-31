import matplotlib.pyplot as plt
import numpy as np

Nt = 1000
dx = 0.001

x = np.empty(Nt, float)
y = np.empty(Nt, float)
z = np.empty(Nt, float)

x[0] = 0
y[0] = 1
z[0] = 1

for i in range(Nt-1):
    y[i+1] = y[i] + dx * z[i]
    z[i+1] = z[i] + dx * y[i]
    x[i+1] = x[i] + dx

plt.plot(x, y)
plt.show()
