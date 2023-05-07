from turtle import *

def right_arc(radius, angle):
    for i in range(angle):
        forward(2*3.14*radius/360)
        right(1)
        
def centered_arc(radius, angle):
    left(angle/2)
    penup()
    forward(radius)
    right(90)
    pendown()
    right_arc(radius, angle)
    penup()
    left(90)
    back(radius)
    left(angle/2)
        
left(90)
centered_arc(50,90)
centered_arc(-50,90)
        
getscreen().getcanvas().postscript(file='output.ps')