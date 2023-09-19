import matplotlib.pyplot as plt

x = []
y = []

for t in range(0,9):
    x.append(t)
    y.append(t*t)

plt.scatter(x, y)
plt.show()
