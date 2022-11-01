import turtle


screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x,y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()



screen.exitonclick()