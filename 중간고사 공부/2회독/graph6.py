# 가장 간단한(기본적인) 2차원 그래프를 그리는 코드를 작성하시오.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [10, 20, 30, 40, 50, 60]

plt.plot(x, y)
plt.title("Simple Plot")
plt.show()