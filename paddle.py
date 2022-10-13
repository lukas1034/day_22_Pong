from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color("white")
        self.goto(position)
        self.y_pos = 0

    def up(self):
        if self.ycor() < 225:
            self.y_pos = self.ycor() + 20
            self.goto(self.xcor(), self.y_pos)

    def down(self):
        if self.ycor() > -225:
            self.y_pos = self.ycor() - 20
            self.goto(self.xcor(), self.y_pos)

    def detect_collision(self, ball_y_pos):
        if self.y_pos + 55 >= ball_y_pos >= self.y_pos - 55:
            return True
        else:
            return False
