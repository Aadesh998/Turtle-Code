from turtle import *
speed(0)
bgcolor('black')
colors = ['#F4D03F','#82E0AA','#C32EF7','#DC7633']
for i in range(100):
    pencolor(colors[i%4])
    circle(25,90)
    for i in range(60):
        forward(1)
        left(1)
    left(90)
    for i in range(60):
        forward(1)
        right(1)
    left(90)   
    for i in range(60):
        forward(1)
        left(1)     
    circle(25,90)

hideturtle()
done()