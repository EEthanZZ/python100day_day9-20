import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=750, height=600)
user_guess = int(screen.textinput(title="turtle race", prompt="which number will win the race: "))
color = ["red", "yellow", "blue", "green", "orange", "pink", "purple", "grey", "cyan", "navy"]
tur_list = list()


for i in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(x=-300, y=-250 + i * 50)
    new_turtle.color(random.choice(color))
    new_turtle.write(f"{i + 1}", font='Courier, 30')
    tur_list.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for i in tur_list:
        if i.xcor() > 320:
            win_tur = tur_list.index(i) + 1
            i.goto(-30, 0)
            i.turtlesize(7)
            print(f"{win_tur} win")
            xx = Turtle()
            xx.hideturtle()
            xx.penup()
            xx.goto(x=0, y=-120)
            win_color = i.pencolor()
            xx.color(win_color)
            xx.write(f"{win_tur} is the WINNER", font="Courier, 30", align='center')
            is_race_on = False
            if win_tur == user_guess:
                print(f"you win, the winner is {win_tur}")
            else:
                print(f"you lose, the winner is {win_tur}")
        rand_distance = random.randint(1, 10)
        i.forward(rand_distance)
screen.exitonclick()
