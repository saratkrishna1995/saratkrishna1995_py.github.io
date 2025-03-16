from turtle import Turtle, Screen
from random import Random
screen=Screen()
pointer = Turtle()
random = Random()
pointer.shape("turtle")
pointer.width(5)

#Challenge A - Printing a square with dotted line
pointer.penup()
pointer.setx(300)
for x in range(1,5):
    for i in range(1,51):
        if i%2!=0:
            pointer.pendown()
        else:
            pointer.penup()
        pointer.forward(5)
    pointer.left(90)

#Challenge B - Printing shapes of different number of sides - Triangle, Square, Pentagon etx.
pointer.penup()
pointer.home()
pointer.pendown()
for x in range(3,11):
    angle=360/x
    r= random.randint(1,255)
    g= random.randint(1,255)
    b= random.randint(1,255)
    y=(r,g,b)
    screen.colormode(255)
    pointer.pencolor(y)
    for i in range(0,x+1):
        pointer.forward(100)
        pointer.left(angle)
    pointer.home()
screen.exitonclick()