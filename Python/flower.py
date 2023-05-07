from turtle import *
import time # For delay 
hideturtle()
color('orangered', 'crimson')

def left_turn():
    for i in range(10):
        forward(15)
        left(9)
        
def petal():
    begin_fill()
    left_turn()
    left(90)
    left_turn()
    end_fill()
    left(90)

def flower():
    for i in range(5):
     petal()
     right(360/5)
    penup()
    back(15)
    right(70)
    pendown()
    # Middle 
    color('purple','yellow')
    begin_fill()
    for i in range(6):
      forward(20)
      left(60)
    end_fill()
    time.sleep(5) # A delay of 5 seconds 
flower()
bye()