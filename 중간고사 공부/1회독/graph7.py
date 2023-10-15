import matplotlib.pyplot as plt

x = []
y = []

for t in range(-9, 10): # -9 ~ 10 
    x.append(t)
    y.append(t*t)

plt.subplot(1, 2, 1)
plt.scatter(x, y)
plt.title("scatter graph")

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("plot graph")

plt.show()