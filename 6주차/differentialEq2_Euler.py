# 미분 방정식 풀기2 (Euler 방법)

import matplotlib.pyplot as plt
import numpy as np

g = 9.8
v0 = 37

def velocity(t):
    return v0 - g * t

timeEnd = 7.7 # second
dt = 0.01
g = 9.8
Nt = (int)(timeEnd/dt) + 1
yList = np.empty(Nt, float)
tList = np.empty(Nt, float)
yList[0] = 0
tList[0] = 0

for i in range(Nt-1):
    yList[i+1] = yList[i] + dt * velocity(tList[i]) - 1/3 * yList[i] * yList[i]
    tList[i+1] = tList[i] + dt
    print(Nt)

plt.plot(tList, yList)
plt.show()
