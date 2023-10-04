import matplotlib.pyplot as plt
import numpy as np
import math

g = 9.8
velocity = 37
angle = math.radians(40)

t_flight = 2 * velocity * math.sin(angle) / g
print(t_flight)

x_list = []
y_list = []

#def x(t):
#    return velocity * np.cos(angle) * t

#def y(t):
#    return velocity * np.sin(angle) * t - 0.5 * g * t * t     

t = np.arange(0, t_flight, 0.1)

for t in np.arange(0, t_flight, 0.1):
    x_list.append(velocity * np.cos(angle) * t)
    y_list.append(velocity * np.sin(angle) * t - 0.5 * g * t * t  )


plt.plot(x_list, y_list)
plt.show()
