import turtle

t = turtle.Pen()
colors = ["red", "blue", "yellow"]

for x in range(87):
    t.pencolor(colors[x%3])
    t.forward(x)
    t.circle(x)
    t.left(91)
