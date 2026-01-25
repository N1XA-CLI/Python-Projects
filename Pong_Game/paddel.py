from turtle import Turtle

class Paddel(Turtle):

    def __init__(self, position):
        """Creates a paddel."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        
    def go_up(self):
        """Vertically moves the paddel up by 20px."""
        self.goto(self.xcor(), (self.ycor() + 20))
        
    def go_down(self):
        """Vertically moves the paddel down by 20px."""
        self.goto(self.xcor(), (self.ycor() - 20))
