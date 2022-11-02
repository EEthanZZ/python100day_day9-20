import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
tim = turtle.Turtle()
# tim.hideturtle()
# tim.penup()

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
print(states_list)
data_dic = data.to_dict()
print(data_dic)
answer = screen.textinput(title="guess the state", prompt="what's the state name?").title()
print(answer)

if answer in states_list:
    x_cord = data[answer]["x"]
    y_cord = data[answer]["y"]
    tim.goto(x_cord, y_cord)
    tim.write("aaaa")

screen.exitonclick()