import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")
states_list = states_data.state.to_list()
guess_states = []

game_is_on = True
score = 0
while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct", prompt="What's another state's name?")

    if answer_state == "Exit":
        miss_list = [state for state in states_list if state not in guess_states]

        data_new = pandas.DataFrame(miss_list)
        data_new.to_csv("miss_list.csv")
        break
    for state in states_list:
        if state.lower() == answer_state.lower():
            state_row = states_data[states_data.state == state]
            state_name = turtle.Turtle()
            state_name.ht()
            state_name.penup()
            state_name.goto(int(state_row.x), int(state_row.y))
            state_name.write(f"{state_row.state.item()}")
            guess_states.append(state_row.state.item())

