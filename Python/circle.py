from turtle import *

width(2)

def circle(radius):
    penup()
    forward(radius)
    pendown()
    left(90)
    begin_fill()
    for i in range(60):
        forward(3.14 * radius / 30)
        left(6)
    end_fill()
    right(90)
    penup()
    back(radius)
    pendown()

# your code here
color('red','yellow')
circle(50)


hideturtle()
bye()