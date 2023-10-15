# 6. 포물체 운동을 코드로 작성하시오.
import matplotlib.pyplot as plt
import numpy as np
import math

g = 9.8
velocity = 37 # 초기 속도
angle = math.radians(40) # 초기에 공을 던지는 지면과의 각도
t_flight = 2 * velocity * math.sin(angle) / g # 총 비행 시간
print(t_flight)

def x(t):
    return velocity * np.cos(angle) * t

def y(t):
    return velocity * np.sin(angle) * t - 0.5 * g * t * t

t = np.arange(0, t_flight, 0.1)
plt.plot(x(t), y(t))
plt.show()