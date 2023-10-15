import turtle

t = turtle.Pen()
colors = ["red", "blue", "yellow"]

for x in range(89):
    t.pencolor(colors[x%3])
    t.forward(x)
    t.circle(x)
    t.left(90)