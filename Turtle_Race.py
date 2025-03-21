from turtle import Screen, Turtle
from random import Random

pointer=Turtle()
screen=Screen()
random=Random()

screen.setup(width=500,height=400)
screen.title("Welcome to the turtle race!!")

def tort_color(k,j):
    c = random.choice(k)
    if c not in j:
        return c
    else:
        return tort_color(k,j)

a=['red','blue','green','yellow','brown','pink']
b=[]
y=1
players=[]

for i in [-2,-1,0,1,2,3]:
    player = Turtle(shape="turtle")
    player.penup()
    if b!=a:
       ac=tort_color(a,b)
       b.append(ac)
       player.color(ac)
    player.goto(x=-220, y=i*30)
    players.append(player)

selection = screen.textinput(title="Make your bet",prompt="Choose your turtle by colour:")
race_on='False'
if selection:
    race_on='True'

while race_on=="True":
    for turtle in players:
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)
        xc= turtle.xcor()
        if xc > 230:
            race_on='False'
            winning_color=turtle.pencolor()
            if winning_color==selection:
                print(f"You've Won! {winning_color} turtle made the cut")
            else:
                print(f"You've Lost! {winning_color} turtle made the cut")

screen.exitonclick()