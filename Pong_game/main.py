"""
create the screen

Create and move a paddle

Create the second paddle

create the ball and make it move

detect collision with wall and bounce

detect with paddle

detect when paddle misses

keep score
"""
PADDLE_LOCATION = [(350,)]

# create the screen
from turtle import Turtle, Screen
screen = Screen()
screen.bgcolor("black")
screen.title("Welcome to the Pong game")
screen.setup(width=800, height=600)


tim = Turtle()
tim.shapesize(stretch_len=1, stretch_wid=5)
tim.shape("square")
tim.color("white")
tim.penup()
screen.tracer(0)
tim.goto(x=350, y=0)


def go_up():
    new_y = tim.ycor() + 20
    tim.goto(x=350, y=new_y)


def go_down():
    new_y = tim.ycor() - 20
    tim.goto(x=350, y=new_y)


screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")


# create the paddle


screen.update()
screen.exitonclick()
