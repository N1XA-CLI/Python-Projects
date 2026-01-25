from turtle import Turtle, Screen
from paddel import Paddel

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

paddel_left = Paddel()
paddel_left.goto(350, 0)

paddel_right = Paddel()
paddel_right.goto(-350, 0)

game_is_on = True

while game_is_on:
    screen.update()
    
    screen.listen()
    screen.onkey(paddel_right.go_up, "Up")
    screen.onkey(paddel_right.go_down, "Down")

    screen.onkey(paddel_left.go_up, "w")
    screen.onkey(paddel_left.go_down, "s")


screen.exitonclick()
