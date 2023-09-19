import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for t in np.arange(0,9,0.1):
    x.append(np.cos(t))
    y.append(np.sin(t))

plt.plot(x,y)
plt.show()
