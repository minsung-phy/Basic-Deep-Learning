import matplotlib.pyplot as plt

x1 = [1, 2, 3, 7, 11, 13, 17]
y1 = [2, 4, 8, 11, 13, 17, 19]

plt.subplot(1, 2, 1)
plt.plot(x1, y1)
plt.title("plot1")

x2 = [1, 2, 3, 7, 11, 13, 17]
y2 = [3, 5, 9, 13, 17, 19, 39]

plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.title("plot 2")

plt.show()