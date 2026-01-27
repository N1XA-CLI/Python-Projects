from turtle import Turtle
import time
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_level()

    def game_end(self):
        self.clear()
        self.goto(0, 0)
        self.write(f" Game Ended!\nFinal Score: {self.level}", align="center", font=FONT)

    def update_level(self):
        self.clear()
        self.goto((-225, 260))
        self.write(f"Level: {self.level}", align="center", font=FONT)
    
    def level_up(self):
        self.level += 1
        self.update_level()