from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        """Creates a ball."""
        super().__init__()
        self.shape("circle")
        self.color("white")
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)