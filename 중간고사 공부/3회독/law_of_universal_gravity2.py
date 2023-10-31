# 만류 인력의 법칙

import matplotlib.pyplot as plt
import numpy as np

G = 6.674 * (10 ** -11)
m = 2
M = 9

def f(r):
    return G * m * M / (r ** 2)

r = np.arange(10, 100, 0.1)
plt.plot(r, f(r))
plt.show()
