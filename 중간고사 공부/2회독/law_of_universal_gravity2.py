# 만류 인력의 법칙을 시각화하시오. (m = 2, M = 9)

import matplotlib.pyplot as plt
import numpy as np

G = 6.674 * (10 ** -11)
m = 2
M = 9

x = []
y = []

def f(r):
    return G * (m * M) / (r ** 2)

for r in np.arange(10, 100, 0.1):
    x.append(r)
    y.append(f(r))

plt.plot(x, y)
plt.xlabel("distance")
plt.ylabel("force")
plt.show()