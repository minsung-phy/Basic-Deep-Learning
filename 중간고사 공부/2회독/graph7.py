# 2차 함수 그래프를 그려보시오.

import matplotlib.pyplot as plt

x = []
y = []

for t in range(-9,10):
    x.append(t)
    y.append(t*t)

plt.plot(x, y)
plt.show()