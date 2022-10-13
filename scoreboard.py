from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_l = 0
        self.score_r = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_l, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_r, align="center", font=("Courier", 80, "normal"))

    def add_l_score(self):
        self.score_l += 1
        self.update_scoreboard()

    def add_r_score(self):
        self.score_r += 1
        self.update_scoreboard()

    def check_score(self):
        if self.score_r == 5 or self.score_l == 5:
            return 10

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", move=False, align="center", font=("Courier", 50, "normal"))
