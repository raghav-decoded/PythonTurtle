from turtle import *
from time import sleep

hideturtle()
# Setting the turtle position
penup()
left(90)
forward(200)
right(90)
back(100)
pendown()

# drawing blue circle
color('blue','blue')
#Make a diameter 200 circle, curving down
begin_fill()
for i in range(200):
    forward(7.416)
    right(1.8)
end_fill()

# setting turtle position
penup()
right(90)
forward(250)
left(90)
back(190)
pendown()

# Drawing red arcs
color('red')
width(10)
left(30)
forward(430) # First arc
right(160)
forward(500) # Second arc

#Setting turtle position
penup()
right(50) 
forward(50) # Turtle on the -ve X axis
right(90)
forward(120) #Adjusting the height of word NASA in the circle
right(90)
pendown()

# alphabet functions
def N():
    ### N ###
    left(90)
    forward(100)
    right(150)
    forward(115)
    left(150)
    forward(100)
    
def A(): 
  ### A ###
  left(60)
  forward(115)
  right(120)
  forward(115)
  left(180)
  forward(40)
  left(60)
  forward(73)
  left(180)
  forward(73)
  right(60)
  forward(40)
  
def S():
    ### S ###
    forward(50)
    left(45)
    forward(25)
    left(45)
    forward(25)
    left(45)
    forward(25)
    left(45)
    forward(35)
    right(45)
    forward(25)
    right(45)
    forward(25)
    right(45)
    forward(25)
    right(45)
    forward(50)
    
def charSpace():
    penup()
    forward(15)
    pendown()
    
#Writing NASA
color('white')
width(14)
N()
back(100)
right(90)
charSpace()
A()
left(60)
charSpace()
S()
penup()
right(90)
forward(110)
left(90)
pendown()
charSpace()
A()

sleep(4) # Wait for 4 seconds.(optional) 
bye()