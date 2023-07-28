from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
screen= Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('Snake Game')


foodo = Food()
snake=Snake()
game_on = True
scoreboard = Score()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    snake.move()
    
    if snake.head.distance(foodo) < 15:
        foodo.refresh()
        scoreboard.increase()
        snake.extend()
        
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_on = False
        
    for x in snake.snakes[1:]:
        if snake.head.distance(x) < 10:
            scoreboard.game_over()
            game_on = False

screen.exitonclick()