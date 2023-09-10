from turtle import Screen, ontimer
from player import Player

# Remembers that colors are tuples
# ex. ('white', 'white')

screen = Screen()
screen.bgcolor('black')
screen.title('Turtle Invasion')
screen.setup(width = 700, height=500)
screen.listen()

game_on = True

player=Player()
screen.onkey(player.go_right,"Right")
screen.onkey(player.go_left,"Left")
screen.onkey(player.shoot,'Up')

player.create_fences()
player.create_enemies()

def looping_func(func):
    func()
    looping_func(func)

looping_func(func=player.aliens_moving)




screen.exitonclick()