import matplotlib.pyplot as plt
import numpy as np

Nt = 1000
x = np.empty(Nt, float)
y = np.empty(Nt, float)
z = np.empty(Nt, float)
x[0] = 0
y[0] = 1
z[0] = 1
dt = 0.001

for n in range(Nt - 1):
    y[n+1] = y[n] + dt * z[n]
    z[n+1] = z[n] + dt * y[n]
    x[n+1] = x[n] + dt


plt.plot(x, y)
plt.show()

`
