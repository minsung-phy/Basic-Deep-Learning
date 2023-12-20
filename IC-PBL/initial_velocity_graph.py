import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rc
rc('font', family='AppleGothic')

plt.rcParams['axes.unicode_minus'] = False

# 속도 계산 함수 정의
def velocity(f, d, G):
    value = 254.0146 * d * (f + G)
    if value < 0:
        # 음수 값 처리, 예: None 반환 또는 특정 값 반환
        return None
    return value ** 0.5


# 주어진 데이터
d = 107 # Skid mark 거리
f_aspalt_dry = 0.8
f_aspalt_humid = 0.7
f_concrete_dry = 0.8
f_concrete_humid = 0.6

# 오르막 길 계산 (1도부터 30도)
angles_uphill = np.arange(1, 31)
velocity_uphill_asphalt_dry = [velocity(f_aspalt_dry, d, np.tan(np.deg2rad(angle))) for angle in angles_uphill]
velocity_uphill_asphalt_humid = [velocity(f_aspalt_humid, d, np.tan(np.deg2rad(angle))) for angle in angles_uphill]
velocity_uphill_concrete_dry = [velocity(f_concrete_dry, d, np.tan(np.deg2rad(angle))) for angle in angles_uphill]
velocity_uphill_concrete_humid = [velocity(f_concrete_humid, d, np.tan(np.deg2rad(angle))) for angle in angles_uphill]

# 내리막 길 계산 (-30도부터 -1도)
angles_downhill = np.arange(-30, 0)
velocity_downhill_asphalt_dry = [velocity(f_aspalt_dry, d, np.tan(np.deg2rad(angle))) for angle in angles_downhill]
velocity_downhill_asphalt_humid = [velocity(f_aspalt_humid, d, np.tan(np.deg2rad(angle))) for angle in angles_downhill]
velocity_downhill_concrete_dry = [velocity(f_concrete_dry, d, np.tan(np.deg2rad(angle))) for angle in angles_downhill]
velocity_downhill_concrete_humid = [velocity(f_concrete_humid, d, np.tan(np.deg2rad(angle))) for angle in angles_downhill]

# 평평한 길 계산 (0도)
velocity_straight_asphalt_dry = velocity(f_aspalt_dry, d, 0)
velocity_straight_asphalt_humid = velocity(f_aspalt_humid, d, 0)
velocity_straight_concrete_dry = velocity(f_concrete_dry, d, 0)
velocity_straight_concrete_humid = velocity(f_concrete_humid, d, 0)

# 그래프 그리기
plt.figure(figsize=(18, 6))

# 오르막 길 그래프
plt.subplot(1, 3, 1)
plt.plot(angles_uphill, velocity_uphill_asphalt_dry, label='아스팔트, 건조')
plt.plot(angles_uphill, velocity_uphill_asphalt_humid, label='아스팔트, 습도')
plt.plot(angles_uphill, velocity_uphill_concrete_dry, label='콘크리트, 건조')
plt.plot(angles_uphill, velocity_uphill_concrete_humid, label='콘크리트, 습도')
plt.title('오르막 길')
plt.xlabel('경사도 (도)')
plt.ylabel('A의 초기 속도 (km/h)')
plt.legend() # 범례
plt.grid(True) # 격자

# 내리막 길 그래프
plt.subplot(1, 3, 2)
plt.plot(angles_downhill, velocity_downhill_asphalt_dry, label='아스팔트, 건조')
plt.plot(angles_downhill, velocity_downhill_asphalt_humid, label='아스팔트, 습도')
plt.plot(angles_downhill, velocity_downhill_concrete_dry, label='콘크리트, 건조')
plt.plot(angles_downhill, velocity_downhill_concrete_humid, label='콘크리트, 습도')
plt.title('내리막 길')
plt.xlabel('경사도 (도)')
plt.ylabel('A의 초기 속도 (km/h)')
plt.legend()
plt.grid(True)

# 평평한 길 그래프
plt.subplot(1, 3, 3)
bar_labels = ['아스팔트,\n 건조', '아스팔트,\n 습도', '콘크리트,\n 건조', '콘크리트,\n 습도']
velocities_straight = [velocity_straight_asphalt_dry, velocity_straight_asphalt_humid, 
                       velocity_straight_concrete_dry, velocity_straight_concrete_humid]
bar = plt.bar(bar_labels, velocities_straight, color=['blue', 'green', 'red', 'purple'])
plt.title('평평한 길')
plt.xlabel('도로 조건')
plt.ylabel('A의 초기 속도 (km/h)')
plt.grid(True)

# 숫자 넣는 부분
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1f' % height, ha='center', va='bottom', size = 10)

plt.show()

# 오르막 길 속도 출력
print("오르막 길 속도:")
for angle, v_asphalt_dry, v_asphalt_humid, v_concrete_dry, v_concrete_humid in zip(angles_uphill, velocity_uphill_asphalt_dry, \
                                                                                   velocity_uphill_asphalt_humid, velocity_uphill_concrete_dry, velocity_uphill_concrete_humid):
    if None in [v_asphalt_dry, v_asphalt_humid, v_concrete_dry, v_concrete_humid]:
        print(f"경사도 {angle}도: 계산 불가")
    else:
        print(f"경사도 {angle}도: 아스팔트 건조 - {v_asphalt_dry:.2f} km/h, 아스팔트 습도 - {v_asphalt_humid:.2f} km/h, 콘크리트 건조 - {v_concrete_dry:.2f} km/h, \
              콘크리트 습도 - {v_concrete_humid:.2f} km/h")

# 내리막 길 속도 출력
print("\n내리막 길 속도:")
for angle, v_asphalt_dry, v_asphalt_humid, v_concrete_dry, v_concrete_humid in zip(angles_downhill, velocity_downhill_asphalt_dry, \
                                                                                   velocity_downhill_asphalt_humid, velocity_downhill_concrete_dry, velocity_downhill_concrete_humid):
    if None in [v_asphalt_dry, v_asphalt_humid, v_concrete_dry, v_concrete_humid]:
        print(f"경사도 {angle}도: 계산 불가")
    else:
        print(f"경사도 {angle}도: 아스팔트 건조 - {v_asphalt_dry:.2f} km/h, 아스팔트 습도 - {v_asphalt_humid:.2f} km/h, 콘크리트 건조 - {v_concrete_dry:.2f} km/h, \
              콘크리트 습도 - {v_concrete_humid:.2f} km/h")

# 평평한 길 속도 출력
print("\n평평한 길 속도:")
velocities_straight = [velocity_straight_asphalt_dry, velocity_straight_asphalt_humid, 
                       velocity_straight_concrete_dry, velocity_straight_concrete_humid]
velocities_straight_labels = ['아스팔트, 건조', '아스팔트, 습도', '콘크리트, 건조', '콘크리트, 습도']

for label, velocity in zip(velocities_straight_labels, velocities_straight):
    if velocity is None:
        print(f"{label}: 계산 불가")
    else:
        print(f"{label}: {velocity:.2f} km/h")