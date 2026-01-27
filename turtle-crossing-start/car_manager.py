from turtle import Turtle
import random

COLORS = ["violet", "indigo","blue", "green", "yellow", "orange", "red"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
MAX_CAR = 20

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2)
        self.setheading(180)
        self.penup()
        self.y_axis = random.randint(-220, 220)
        self.goto((270, self.y_axis))
        
    def move(self):
        self.forward(STARTING_MOVE_DISTANCE)
    
    def level_up(self):
        new_y = STARTING_MOVE_DISTANCE + MOVE_INCREMENT
        self.goto((self.xcor() + new_y, self.ycor()))
