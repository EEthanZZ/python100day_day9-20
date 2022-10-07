from turtle import Turtle, Screen
from random import choice
timmy = Turtle()
timmy.shape("circle")

color = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']


def draw(x):
    angle = 360 / x
    for i in range(x):
        timmy.forward(50)
        timmy.right(angle)


for i in range(3, 10):
    draw(i)
    timmy.color(choice(color))


screen = Screen()
screen.exitonclick()
