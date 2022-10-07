from turtle import Turtle, Screen
from random import choice
timmy = Turtle()
timmy.shape("circle")
timmy.pensize(5)
color = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
angle = [90, 270]

for i in range(100):
    timmy.forward(10)
    timmy.color(choice(color))
    timmy.right(choice(angle))
    timmy.forward(10)
    timmy.speed(100)


screen = Screen()
screen.exitonclick()
