import turtle
from turtle import Turtle, Screen
from random import choice, randint
timmy = Turtle()
timmy.shape("circle")
timmy.pensize(5)
angle = [90, 270]
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


for i in range(100):
    timmy.forward(10)
    timmy.color((random_color()))
    timmy.right(choice(angle))
    timmy.forward(10)
    timmy.speed(100)


screen = Screen()
screen.exitonclick()
