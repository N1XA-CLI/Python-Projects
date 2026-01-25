from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self, position):
        """Creates a ball."""
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
    
    def random_position(self):
        random_x = random.randint(400, -400)
        random_y = random.randint(280, -280)
        self.goto(random_x, random_y)