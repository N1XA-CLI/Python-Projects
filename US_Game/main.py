import turtle
import pandas
from write_state import WriteState

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv") # pandas.core.frame.DataFrame
states_list = data.state.to_list() # pandas.core.series.Series but without .to_list()
guessed_states = []

state_writer = WriteState()

while not guessed_states in states_list:
    answer = screen.textinput(title="Guess the state.", prompt="What another's state name?").title()
    if answer in states_list:
        state = data[data["state"] == answer]
        # Get State (x, y) co-ordinates
        state_xcor = state.x[1]
        state_ycor = state.y[1]
        print(f"State: {state}\nX_COR: {state_xcor}\nY_COR: {state_ycor}")
        state_writer.write(text=answer, x_cor=state_xcor, y_cor=state_ycor)


