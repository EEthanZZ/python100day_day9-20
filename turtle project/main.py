from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("circle")


for i in range(0,20):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()
screen.exitonclick()