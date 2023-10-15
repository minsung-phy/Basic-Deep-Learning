import matplotlib.pyplot as plt
import numpy as np

x1 = []
y1 = []

for t in np.arange(0, 10, 0.5):
    x1.append(t)
    y1.append(np.sin(t))

plt.subplot(1, 2, 1)
plt.plot(x1, y1)
plt.title("sin graph")

x2 = []
y2 = [] # 리스트는 변수랑 달리 데이터를 추가하는 것이라 새로운 y 리스트를 만들어줘야 된다.

for t in np.arange(0, 10, 0.5):
    x2.append(t)
    y2.append(np.cos(t))

plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.title("cos graph")

plt.show()