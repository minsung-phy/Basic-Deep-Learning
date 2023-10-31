import turtle

t = turtle.Pen()
colors = ["red", "blue", "green", "pink", "orange"]

for x in range(5):
    t.pencolor(colors[x%5])
    t.forward(200)
    t.left(144)
