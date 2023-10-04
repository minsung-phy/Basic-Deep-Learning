import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for t in np.arange(0,10,0.1):
    x.append(t)
    y.append(np.sin(2 * t))
    
plt.plot(x,y)
plt.show()

