import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move, "Up")

car = CarManager()


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
 
    car.create_cars()
    car.move()
    
    if player.ycor() > 280:
        player.reset()
        scoreboard.increase_score()
        car.increase_speed()

    for x in car.cars:
        if x.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()