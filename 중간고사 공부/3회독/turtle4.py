import turtle

t = turtle.Pen()
colors = ["red", "orange", "yellow", "blue", "purple", "pink"]

for x in range(6):
    t.pencolor(colors[x%6])
    t.forward(200)
    t.left(60)
