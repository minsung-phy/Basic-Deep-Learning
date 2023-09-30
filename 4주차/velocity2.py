import matplotlib.pyplot as plt
import numpy as np
import math

g = 9.8
velocity = 37
angle = math.radians(40)
t_flight = (velocity * math.sin(angle) + ((velocity * velocity) * (math.sin(angle) * math.sin(angle)) + (18 * g)) ** 0.5) / g
print(t_flight)

def x(t):
    return velocity * np.cos(angle) * t

def y(t):
    return 9 + velocity * np.sin(angle) * t - 0.5 * g * t * t

t = np.arange(0, t_flight, 0.1)
plt.plot(x(t), y(t))
plt.show()
