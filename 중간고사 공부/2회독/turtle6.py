import turtle

t = turtle.Pen()

colors = ["red", "orange", "blue", "green", "purple"]

for x in range(5):
    t.pencolor(colors[x%5])
    t.forward(200)
    t.left(144)