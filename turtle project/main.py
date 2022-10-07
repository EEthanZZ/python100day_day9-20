import turtle
from turtle import Turtle, Screen
from random import choice, randint
timmy = Turtle()
timmy.shape("circle")
angle = [90, 270]
turtle.colormode(255)
timmy.speed("fastest")


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_circles(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.left(size_of_gap)


draw_circles(11)
screen = Screen()
screen.exitonclick()
