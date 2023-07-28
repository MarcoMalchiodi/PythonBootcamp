from paddle import Paddle
from turtle import Screen
from opponent import Opponent
from ball import Ball
from Field import Field

paddle = Paddle()
opponent = Opponent()
ball = Ball()
scoreboard = Field()

screen = Screen()
screen.bgcolor('black')
screen.title('Ping Roman Pong')
screen.setup(width = 800, height=600)
screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")


game_on = True

paddle.setheading(90)
opponent.setheading(90)


while game_on:
    opponent.movement()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if (ball.distance(paddle) < 50 and ball.xcor() > 340) or (ball.distance(opponent) < 50 and ball.xcor() < -340):
        ball.bounce_x()
    
    if (ball.distance(paddle) > 50 and ball.xcor() > 380):
        ball.reset()
        scoreboard.score(r = 1, l = 0)
   
        
    if (ball.distance(opponent) > 50 and ball.xcor() < -380):
        ball.reset()
        scoreboard.score(r = 0, l = 1)
    
    
screen.exitonclick()
