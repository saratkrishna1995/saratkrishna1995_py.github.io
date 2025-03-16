from turtle import Turtle, Screen
from random import Random

def rand_color(color_pallete):
    return random.choice(color_pallete)

def hirsh_spot(r):
    for h in range(1,11):
        for l in range(0,10):
            pointer.pendown()
            x=rand_color(color_list)
            screen.colormode(255)
            pointer.color(x)
            pointer.fillcolor(x)
            pointer.stamp()
            pointer.penup()
            pointer.forward(50)
        pointer.home()
        pointer.penup()
        pointer.left(90)
        pointer.forward(50*h)
        pointer.right(90)
    pointer.home()

color_list=[(184, 148, 94), (152, 104, 46), (178, 150, 22), (83, 34, 27), (228, 229, 231), (12, 57, 73), (31, 100, 120), (101, 41, 48), (57, 137, 121), (108, 40, 29), (22, 65, 50), (40, 80, 7), (94, 62, 68), (110, 8, 9), (199, 91, 65), (116, 167, 77), (131, 178, 92), (224, 231, 225), (139, 167, 175), (216, 202, 142), (178, 147, 150), (179, 205, 177), (225, 177, 167), (157, 110, 113), (27, 75, 93), (97, 141, 148), (214, 178, 181), (168, 202, 208)]
pointer=Turtle()
screen=Screen()
random=Random()
pointer.shape("circle")
hirsh_spot(20)
screen.exitonclick()
