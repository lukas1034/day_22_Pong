from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_speed = 0.05
current_score_r = 0
current_score_l = 0
game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

while game_is_on:
    screen.update()
    time.sleep(ball.game_speed)
    ball.move()
    # detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_wall()
    # detect collision with paddle
    if ball.xcor() >= 340:
        if r_paddle.detect_collision(ball.ycor()):
            ball.bounce_paddle()
    if ball.xcor() <= -340:
        if l_paddle.detect_collision(ball.ycor()):
            ball.bounce_paddle()
    # detect miss
    if ball.xcor() > 380:
        ball.reset_to_start()
        scoreboard.add_l_score()
    if ball.xcor() < -380:
        ball.reset_to_start()
        scoreboard.add_r_score()
    # end the game after 5 points
    if scoreboard.check_score() == 10:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
