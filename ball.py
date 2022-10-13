from turtle import Turtle
import random
BALL_SPEED = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("white")
        self.setheading(random.randint(30, 50))
        self.game_speed = 0.05

    def move(self):
        self.forward(BALL_SPEED)

    def bounce_wall(self):
        self.setheading(360 - self.heading())

    def bounce_paddle(self):
        self.setheading(180 - self.heading())
        self.move()
        self.game_speed *= 0.9

    def reset_to_start(self):
        self.goto(0, 0)
        self.setheading(self.heading() - random.randint(-25, 25))
        self.bounce_paddle()
        self.game_speed = 0.05
