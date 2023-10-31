import matplotlib.pyplot as plt
import numpy as np

g = 9.8
v0 = 37

def velocity(t):
    return v0 -  g * t

timeEnd = 7.7
dt = 0.01
Nt = (int)(timeEnd/dt) + 1

y = np.empty(Nt, float)
t = np.empty(Nt, float)

y[0] = 0
t[0] = 0

for i in range(Nt - 1):
    y[i+1] = y[i] + dt * velocity(t[i]) # y[i+1] = y[i] + dt * (velocity(t[i]) + y[i] * y[i] / 3)
    t[i+1] = t[i] + dt

plt.plot(t, y)
plt.title("Differential Equation")
plt.xlabel("t")
plt.ylabel("y")
plt.show()
