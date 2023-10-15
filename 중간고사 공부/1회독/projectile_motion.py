# 초기 x의 위치: 0, 초기 y의 위치: 0

import matplotlib.pyplot as plt
import numpy as np
import math

g = 9.8
velocity = 37 # 공을 던질 때 초기 속도
angle = math.radians(40) # 초기 속도의 지면과의 각도: 40도
t_flight = 2 * velocity * math.sin(angle) / g # 총 비행 시간
print(t_flight)

def x(t):
    return velocity * np.cos(angle) * t

def y(t):
    return velocity * np.sin(angle) * t - 0.5 * g * t * t

t = np.arange(0, t_flight, 0.1)
plt.plot(x(t), y(t))
plt.show()


