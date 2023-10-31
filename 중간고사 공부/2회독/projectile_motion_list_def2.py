import matplotlib.pyplot as plt
import numpy as np
import math

g = 9.8
velocity = 37
angle = math.radians(40)
t_flight = 2 * velocity * math.sin(angle) / g
print(t_flight)

x = []

def y(t):
    return velocity * t * np.sin(angle) - 0.5 * g * t * t

for t in np.arange(0, t_flight, 0.1):
    x.append(velocity * t * np.cos(angle))

t = np.arange(0, t_flight, 0.1)
plt.plot(x, y(t))
plt.show()
