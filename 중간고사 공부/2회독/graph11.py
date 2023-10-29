# y = 1-x^2 그래프를 -9~9까지 0.1 간격으로 그려보시오.

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for t in np.arange(-9, 9.1, 0.1):
    x.append(t)
    y.append(1-t*t)

plt.plot(x, y)
plt.title("y = 1-x^2")
plt.show()