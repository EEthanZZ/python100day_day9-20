import turtle
from turtle import Turtle, Screen
from random import choice, randint
import colorgram


colors = colorgram.extract("dot_paint.jpeg", 30)
color_list = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    new_color = (r, g, b)
    color_list.append(new_color)


timmy = Turtle()
timmy.shape("circle")
angle = [90, 270]
turtle.colormode(255)
timmy.speed("fastest")
timmy.penup()
timmy.goto(x=-300, y=-300)

for i in range(101):
    timmy.dot(20, choice(color_list))
    timmy.forward(50)

    if i % 10 == 0:
        timmy.goto(x=-300, y=i*5-300)


screen = Screen()
screen.exitonclick()
