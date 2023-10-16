import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
Nt = 1000

x = np.empty(Nt, float)
y = np.empty(Nt, float)
z = np.empty(Nt, float)
w = np.empty(Nt, float)

x[0] = 0
y[0] = 1
z[0] = 0
w[0] = 0

for i in range(Nt-1):
    y[i+1] = y[i] + dt * z[i]
    z[i+1] = z[i] + dt * w[i]
    w[i+1] = w[i] + dt * y[i]
    x[i+1] = x[i] + dt

plt.plot(x, y)
plt.show()


