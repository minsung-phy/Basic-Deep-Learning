import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for t in np.arange(0,1.57,0.1):
    x.append(t)
    y.append(np.cos(t) * np.cos(t))

plt.plot(x,y)
plt.show()

