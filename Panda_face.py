import turtle
pen = turtle.Turtle()

def ring(col,rad):
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()
    
pen.penup()
pen.setpos(-45,150)
pen.pendown()

ring('#000100',25)

pen.penup()
pen.setpos(45,150)
pen.down()
ring('#000100',25)

pen.penup()
pen.setpos(0,15)
pen.pendown()
ring('#fff',80)
pen.penup()
pen.setpos(-28,95)
pen.pendown()
ring('#000100',16)

pen.penup()
pen.setpos(28,95)
pen.pendown()
ring('#000100',16)

pen.penup()
pen.setpos(-28,97)
pen.pendown()
ring('#fff',8)
pen.penup()
pen.setpos(28,97)
pen.pendown()
ring('#fff',8)

pen.penup()
pen.setpos(0,65)
pen.pendown()
ring('#000100',10)

pen.penup()
pen.setpos(0,65)
pen.pendown()
pen.right(90)
pen.circle(10,180)
pen.penup()
pen.setpos(0,65)
pen.pendown()
pen.left(360)
pen.circle(10,-180)
pen.hideturtle()
pen.done()