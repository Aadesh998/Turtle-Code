from turtle import *

bgcolor("black")
speed(10)
color = ['red','blue','purple','orange','yellow','green']

for x in range(200):
    pencolor(color[x%6])
    width(x/100 + 1)
    forward(x)
    left(59)

done()