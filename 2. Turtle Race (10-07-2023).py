from turtle import Turtle, Screen
import random

victory = False
screen=Screen()
bet = screen.textinput('Make your bet','Which tutrtle do you wish to bet on? red/purple/yellow/green/blue')

colors = ['red','purple','yellow','green','blue']
y = -200

all_turtles = []

for x in range(0,5):
    balubba = Turtle()
    balubba.penup()
    balubba.color(colors[x])
    balubba.setx(-200)
    balubba.sety(y)
    balubba.speed(1)
    all_turtles.append(balubba)
    y += 100

if bet:
    victory = True
    
while victory:
    distances = [5,10,20,25]
    for x in all_turtles:
        if x.xcor() > 310:
            winner = x.pencolor()
            victory = False
        else:
            x.forward(distances[random.randint(0,3)])


print('The winner is '+winner)

if bet == winner:
    print('You won the bet!')
else:
    print('You lost the bet!')


screen.exitonclick()