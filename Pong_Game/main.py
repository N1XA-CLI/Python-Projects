#!/usr/bin/env python3

from turtle import Screen
from paddel import Paddel
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

l_paddel = Paddel(position=(-350, 0))
r_paddel = Paddel(position=(350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddel.go_up, "Up")
screen.onkey(r_paddel.go_down, "Down")
screen.onkey(l_paddel.go_up, "w")
screen.onkey(l_paddel.go_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.09)
    screen.update()
    ball.move_right()

    # Detect collision with wall(y-axis)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddel and l_paddel
    if ball.distance(r_paddel) < 50 and ball.xcor() > 320 or ball.distance(l_paddel) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Missed by r_paddel
    if ball.xcor() > 380:
        # Increase l_paddel score
        score.l_point()
        ball.reset_position()

    # Missed by l_paddel
    elif ball.xcor() < -380:
        # Increase r_paddel score
        score.r_point()
        ball.reset_position()

screen.exitonclick()
