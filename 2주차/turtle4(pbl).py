import turtle

t = turtle.Pen()

colors = ["red", "orange", "green", "blue", "purple", "pink"]

for x in range(100):
    t.pencolor(colors[x%6])
    t.forward(x)
    t.left(60)
