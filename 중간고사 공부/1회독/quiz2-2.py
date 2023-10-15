# 2. 함수를 이용하여 2차 함수를 그리시오.

import matplotlib.pyplot as plt
import numpy as np

def y(x):
    return x * x

x = np.arange(-9, 9, 0.1)
plt.plot(x, y(x))
plt.show()