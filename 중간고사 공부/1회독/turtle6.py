import turtle

t = turtle.Pen()

colors = ["red", "orange", "green", "blue", "purple"] # 총 5가지의 색 리스트

for x in range(5):
    t.pencolor(colors[x%5])
    t.forward(200)
    t.left(144)