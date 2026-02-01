import turtle
import pandas
from write_state import WriteState

image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
guessed_states = []

state_writer = WriteState()

def save_progress():
    # TODO: Save the Game progress by saving the guessed_states along with it's x and y co-ordiantes into a csv then read and plot the state if data exist else continue.
    # TODO: Do ask the user if the user want to resume the game or to start new game(2 confirmation before new game).
    # TODO: Also try to save the progress while running the game (maybe use thread)
    pass

while len(guessed_states) != len(states_list):
    answer = screen.textinput(title="Guess the state.", prompt="What another's state name?")
    if answer is None:
        save_progress()
        break
    answer = answer.title()
    if answer in states_list:

        if answer in guessed_states:
            continue
        else:
            guessed_states.append(answer)

        state = data[data["state"] == answer]
        # Get State (x, y) co-ordinates
        state_xcor = state.x.iloc[0]
        state_ycor = state.y.iloc[0]

        state_writer.write(text=answer, x_cor=state_xcor, y_cor=state_ycor)

screen.exitonclick()
