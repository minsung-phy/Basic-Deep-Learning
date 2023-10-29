import turtle

t = turtle.Pen()

colors = ["red", "green", "orange", "blue", "pink", "purple"]

for x in range(100):
    t.pencolor(colors[x%6])
    t.forward(x)
    t.left(60)