# Bond line representation of alkanes

print("Bond line alkanes ")
compound = input("Which alkane do you want ? ")

compound = compound.lower()

c = 0
if compound == "propane":
    c = 1
elif compound == "pentane":
    c = 2
elif compound == "heptane":
    c = 3 
elif compound == "nonane":
    c = 4
elif compound == "butane":
    c = -1
elif compound == "hexane":
    c = -2
elif compound == "octane":
    c = -3
elif compound == "decane":
    c = -4
    
from turtle import *
color('yellow')
speed(3)
width(5)

penup()
back(200)
pendown()

if c > 0 :
    for i in range(c):
        left(60)
        forward(100)
        right(120)
        forward(100)
        left(60)
        hideturtle()
elif c < 0 :
    c = c * -1
    for i in range(c):
        left(60)
        forward(100)
        right(120)
        forward(100)
        left(120)
        forward(100)
        back(100)
        left(-60)
        hideturtle()
bye()