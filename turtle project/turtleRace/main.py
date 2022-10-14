import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=750, height=600)
screen.textinput(title="turtle race", prompt="which number will win the race: ")
color = ["red", "yellow", "blue", "green", "orange", "pink", "purple", "grey", "cyan", "navy"]
tur_list = list()
for i in range(0, 11):
    jim = Turtle("turtle")
    jim.penup()
    jim.goto(x=-350, y=-250 + i*50)
    jim.color(random.choice(color))


screen.exitonclick()
