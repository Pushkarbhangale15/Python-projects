from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))

ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #Detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #Detect Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        
        ball.bounce_x()
        
    #detect right paddle miss
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()
    #detect left paddle miss
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()
#work from here
screen.exitonclick()