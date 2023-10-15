import turtle

t = turtle.Pen()

colors = ["red", "orange", "green", "blue", "purple", "pink"]

for x in range(100):
    t.pencolor(colors[x%6])
    t.left(60)
    t.forward(x)
