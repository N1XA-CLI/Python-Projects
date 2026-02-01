from turtle import Turtle


class WriteState:
    def __init__(self):
        self.writer = Turtle()
        self.writer.penup()
        self.writer.color("black")
        self.writer.hideturtle()

    def write(self, text, x_cor, y_cor):
        self.writer.goto((x_cor, y_cor))
        self.writer.write(text, font=("Courier", 10, "normal"))
