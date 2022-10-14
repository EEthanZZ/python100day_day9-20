from turtle import Turtle, Screen

turtle_1 = Turtle("turtle")
screen = Screen()
screen.setup(width=750, height=600)
screen.textinput(title="turtle race", prompt="which number will win the race: ")

turtle_1.penup()
turtle_1.goto(x=-350, y=-250)

screen.exitonclick()
