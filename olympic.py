import turtle

def draw_circle(x,y,color,radius):
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.circle(radius)

def main():
    turtle.speed(1)
    position = [
        (-110,0,"blue"),
        (0,0,"black"),
        (110,0,"red"),
        (-55,-50,"yellow"),
        (55,-50,"green")
    ]

    for x,y,color in position:
        draw_circle(x,y,color,50)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()