import turtle

t = turtle.Pen()
turtle.speed(100)
turtle.bgcolor('white')
colors = ['magenta', 'purple', 'blue', 'green', 'orange', 'yellow', 'magenta']
for i in range(360):
    t.pencolor(colors[i // 150])
    t.width(i // 100 + 1)
    t.forward(i)
    t.left(50)
