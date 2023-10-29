import turtle

t = turtle.Pen()

colors = ["yellow", "blue", "red", "pink"]

for x in range(100):
    t.pencolor(colors[x%4])
    t.forward(x)
    t.circle(x)
    t.left(90)