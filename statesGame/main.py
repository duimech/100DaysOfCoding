# This program uses a CSV file containing the US states and checks to see how many of them you know while displaying an image of the US.
# Author: Ray Bolin
# Date: 1/29/2022
# 100DaysOfCoding

import turtle
import pandas

screen = turtle.Screen()
screen.title("States Game")
image = "100DaysOfCoding/statesGame/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("100DaysOfCoding/statesGame/50_states.csv")
states_list = states_data.state.to_list()
guessed_correctly = 0
game_running = True
remaining_states_dictionary = {
    "States": []
}

# Create a turtle to write the name of the state on the map using the coordinates from the CSV file.
def write_on_map(user_answer):
    state_row = states_data[states_data.state == user_answer]

    # xcor = state_row.iloc[0][1]
    # ycor = state_row.iloc[0][2]
    # xcor = int(state_row.x)
    # ycor = int(state_row.y)
    # xcor = state_row.x.item()
    # ycor = state_row.y.item()

    my_turtle = turtle.Turtle()
    my_turtle.penup()
    my_turtle.hideturtle()
    my_turtle.goto(int(state_row.x), int(state_row.y))
    my_turtle.write(f"{user_answer}", align="center", font=("Courier", 8, "normal"))


while game_running:
    if guessed_correctly < 50:
        # Get user answer in Title Case to compare to our list of states
        user_answer = (screen.textinput(title=f"{guessed_correctly}/50 - Guess a State", prompt="Name a State:")).title()

        # for state in states_list:
            # if user_answer == state:
        if user_answer in states_list:
            guessed_correctly += 1
            states_list.remove(user_answer)
            write_on_map(user_answer)
        elif user_answer == "Exit":
            print(f"You guessed {guessed_correctly} states correctly.")
            remaining_states_dictionary["States"] = states_list
            df = pandas.DataFrame(remaining_states_dictionary)
            df.to_csv("100DaysOfCoding/statesGame/remaining_states.csv")
            game_running = False
    else:
        print("You guessed all 50 states")
        game_running = False


# Show the x, y coordinates on the map image
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()