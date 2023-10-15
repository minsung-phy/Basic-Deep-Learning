import turtle

t = turtle.Pen()
colors = ["red", "blue", "yellow"]

for x in range(100):
    t.pencolor(colors[x%3]) # 색을 3가지로 지정 (0%3 = 0, 1%3 = 2, 2%3 = 1, 3%3 = 0, 4%3 = 1, 5%3=2, 6%3 = 0 ... )
    t.forward(x) # 앞으로 x만큼 이동
    t.circle(x) # 반지름이 x인 원을 그림
    t.left(91) # 왼쪽으로 91도 이동 (각도를 변경 함에 따라 다른 그림이 나옴)