import matplotlib.pyplot as plt
import numpy as np

Nt = 1000
dt = 0.001
m = 2
k = 3

x = np.empty(Nt, float)
z = np.empty(Nt, float)
t = np.empty(Nt, float)

x[0] = 1
z[0] = 1
t[0] = 0

for n in range(Nt-1):
    x[n+1] = x[n] + dt * z[n]
    z[n+1] = z[n] - k * dt * x[n] / m
    t[n+1] = t[n] + dt

plt.plot(t, x)
plt.show()
