# y = x^2의 그래프를 0~10사이를 0.1의 간격으로 출력하는 그래프 작성
import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for t in np.arange(0, 10, 0.1):
    x.append(t)
    y.append(t*t)

plt.plot(x, y)
plt.show()