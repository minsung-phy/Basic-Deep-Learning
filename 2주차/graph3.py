import matplotlib.pyplot as plt

x = [1, 2, 3, 7, 11, 13, 17]
y = [2, 4, 8, 11, 13, 17, 19]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Plot1")

x = [1, 2, 3, 7, 11, 13, 17]
y1 = [3, 5, 9, 13, 17, 19, 39]

plt.subplot(1, 2, 2)
plt.plot(x, y1)
plt.title("Plot2")

plt.show()
