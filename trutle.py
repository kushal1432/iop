import turtle
colors = ['red','yellow','black','green','orange']
t=turtle.pen()
t.speed()
turtle.bgcolor('blue')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)