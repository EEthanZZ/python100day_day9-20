import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
print(states_list)
guessed_state = []

while len(guessed_state) < 50:
    answer = screen.textinput(title=f"{len(guessed_state)}/50", prompt="what's the state name?").title()
    print(answer)

    if answer in states_list:
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state_data = data[data["state"] == answer]
        x_cord = int(state_data["x"])
        y_cord = int(state_data["y"])
        tim.goto(x_cord, y_cord)
        tim.write(answer)
        guessed_state.append(answer)

    if answer == 'Exit':
        missing_state = []
        for i in states_list:
            if i not in guessed_state:
                missing_state.append(i)

        break

screen.exitonclick()