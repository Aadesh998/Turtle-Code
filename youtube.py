import turtle
t = turtle.Turtle()

t.penup()
t.goto(-10,0)
t.pendown()
t.color('red')
t.begin_fill()

t.forward(120)
t.circle(25,90)
t.forward(120)
t.circle(25,90)
t.forward(240)
t.circle(25,90)
t.forward(120)
t.circle(25,90)
t.forward(120)
t.end_fill()

t.penup()
t.goto(-30,45)
t.pendown()
t.color('#fff')
t.begin_fill()

t.left(90)
t.forward(75)
t.right(125)
t.forward(75)
t.right(115)
t.forward(72)



t.end_fill()
t.hideturtle()
t.done()