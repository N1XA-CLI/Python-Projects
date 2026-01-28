from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Times New Roman', 20, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_score()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score()
        self.score = 0
        self.update_scoreboard()

    def write_score(self):
        with open("data.txt", "w") as h_score:
            h_score.write(str(self.high_score))
    
    def read_score(self):
        with open("data.txt", "r") as r_score:
            currently_high_score = r_score.read()
            return int(currently_high_score)
            

