from turtle import *

getscreen().bgcolor("red")
pencolor("black")

color("white")
penup()
goto(-160,160)
pendown()

begin_fill()
left(18)
circle(-500,40)
right(90)
forward(17)

right(89.5)
circle(500,39)
right(90)
forward(17)
end_fill()

penup()
goto(-155,133)
pendown()
begin_fill()
right(90.5)
circle(-500,38)
right(70)
circle(-30,80)
left(90)
circle(-20,-70)
right(10)
circle(-300,-15)
right(93)
forward(280)
right(160)
forward(280)
left(80)
circle(300,15)
circle(20,70)
left(80)
circle(30,-80)
end_fill()

penup()
goto(-20,155)
pendown()
pencolor("black")
color("red")
begin_fill()
left(30)
forward(60)
# left(30)
# forward(60)
left(130)
forward(65)
end_fill()

done()
