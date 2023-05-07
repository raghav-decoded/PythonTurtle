from turtle import *
from time import sleep

color('deepskyblue')
speed(0)
width(25) # make the stroke 5 pixels wide
#Make a diameter 200 semicircle, curving down
for i in range(125):
    forward(1.416)
    right(1.8)
forward(75)

#Make a diameter 200 circle, curving down
for i in range(155):
    forward(1.416)
    left(1.8)
forward(77)
for i in range(50):
    forward(1.416)
    right(1.8)
hideturtle() # hide the turtle from the final image
sleep(0.1) 
bye()