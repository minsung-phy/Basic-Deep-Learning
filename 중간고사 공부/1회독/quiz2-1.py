# 1. 리스트를 이용하여 2차 함수를 그리시오.

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for i in np.arange(-9, 9, 0.1):
    x.append(i)
    y.append(i*i)

plt.plot(x, y)
plt.show()