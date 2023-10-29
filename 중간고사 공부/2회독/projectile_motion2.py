import matplotlib.pyplot as plt
import numpy as np
import math

g = 9.8
velocity = 37
angle = math.radians(40)
t_flight = (velocity * math.sin(angle) + (((velocity ** 2) * (math.sin(angle) ** 2) + (90 * g)) ** 0.5)) / g
print(t_flight)

def x(t):
    return velocity * t * np.cos(angle)

def y(t):
    return 45 + (velocity * t * np.sin(angle)) - (0.5 * g * t * t)

t = np.arange(0, t_flight, 0.1)
plt.plot(x(t), y(t))
plt.show()
