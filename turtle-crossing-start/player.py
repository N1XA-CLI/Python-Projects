from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)
        
    def move(self):
        self.forward(MOVE_DISTANCE)

    def got_collidied(self, object):
        if self.distance(object) <= 15:
            return True
    
    def next_level(self):
        self.goto(STARTING_POSITION)

    def is_level_complete(self):
        current_ycor = self.ycor()
        if current_ycor >= FINISH_LINE_Y:
            self.next_level()
            return True
    