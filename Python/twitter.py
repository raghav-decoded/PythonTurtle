from turtle import *
color('deepskyblue','deepskyblue') #Drawing filled shapes

width(5)
speed(0)

begin_fill()
#Stomach
for i in range(125):
    forward(1.416)
    left(0.8)
# Beak
right(70)
forward(50)
left(170)
forward(50)
right(170)
forward(50)
left(170)
forward(50)
right(90)
# Head
for i in range(105):
    forward(1.416)
    left(1.8)
left(-100)
#Wing
for i in range(110):
    forward(1.416)
    right(0.8)
left(157)
# Wing ending
for i in range(110):
    forward(1.416)
    left(0.6)
right(120)
# Tail
for i in range(27):
    forward(1.416)
    right(0.4)
left(120)
# Tail ending
for i in range(50):
    forward(1.516)
    left(1.26)
forward(10)
end_fill()

hideturtle()
getscreen().getcanvas().postscript(file = 'output.ps')

bye()