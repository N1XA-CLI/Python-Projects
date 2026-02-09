import turtle
import pandas
from write_state import WriteState

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

state_writer = WriteState()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []

while len(guessed_states) != len(states_list):
    answer = screen.textinput(title=f"{len(guessed_states)}/{len(states_list)} state.", prompt="What another's state name?")
    answer = answer.title()
    if answer == "Exit":
        missed_states = [state for state in states_list if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states).to_csv("missed_state.csv")
        break
    if answer in states_list:
        if answer in guessed_states:
            continue
        else:
            guessed_states.append(answer)
            state = data[data["state"] == answer]
            state_xcor = state.x.iloc[0]
            state_ycor = state.y.iloc[0]
            state_writer.write(text=answer, x_cor=state_xcor, y_cor=state_ycor)


