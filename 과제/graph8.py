import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for t in np.arange(-2,1.5,0.1):
    x.append(t)
    y.append(np.sin(t)/t)
    
plt.plot(x,y)
plt.show()

