import matplotlib.pyplot as plt

x = [1, 2, 3, 7, 11, 13, 17]
y = [2, 4, 8, 11, 13, 17, 19]

plt.subplot(1, 2, 1) # 그림이 1개가 아니라 여러 개 그림이 나옴 (행, 열, 인덱스)
plt.plot(x, y)
plt.title("Plot 1")

x = [1, 2, 3, 7, 11, 13, 17]
y = [3, 5, 9, 13, 17, 19, 39]

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("Plot 2")

plt.show()