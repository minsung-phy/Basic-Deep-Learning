import matplotlib.pyplot as plt
import numpy as np
import math

g = 9.8
velocity = 37
angle = math.radians(40)
t_flight = 2 * velocity * math.sin(angle) / g
print(t_flight)

x = []
y = []

for t in np.arange(0, t_flight, 0.1):
    x.append(velocity * np.cos(angle) * t)
    y.append(velocity * np.sin(angle) * t - 0.5 * g * t * t)

plt.plot(x, y)
plt.show()