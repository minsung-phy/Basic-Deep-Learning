import matplotlib.pyplot as plt
import numpy as np

Nt = 1000
y = np.empty(Nt, float)
z = np.empty(Nt, float)
x = np.empty(Nt, float)

y[0] = 1
z[0] = 1
x[0] = 0
dt = 0.001

for i in range(Nt-1):
    y[i+1] = y[i] + dt * z[i]
    z[i+1] = z[i] + dt * y[i]
    x[i+1] = x[i] + dt

plt.plot(x, y)
plt.show()
