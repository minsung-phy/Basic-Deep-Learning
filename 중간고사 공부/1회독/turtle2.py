import turtle # turtle 모듈 가져오기

t = turtle.Pen() # turtle 모듈의 Pen() 함수를 t로 지정

for x in range(10): # 0 ~ 9
    print(x)
    t.forward(x)
    t.left(90)