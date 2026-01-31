import turtle
import pandas
# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)

data = pandas.read_csv("50_states.csv") # pandas.core.frame.DataFrame
states_list = data.state # pandas.core.series.Series
states_x_cor = data.x    # pandas.core.series.Series
states_y_cor = data.y    # pandas.core.series.Series

print(states_list == "Alaska")

# while True:
#     answer = screen.textinput(title="Guess the state.", prompt="What another's state name?").title()
#     if answer in states_list:
#         print("It's there")



# screen.exitonclick()
