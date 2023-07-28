from turtle import Turtle, Screen
from score import Scoreboard
import pandas

data = pandas.read_csv('50_states.csv')
state = data["state"].to_list()
xcor = data["x"].to_list()
ycor = data["y"].to_list()

screen = Screen()
screen.title('US States Game')
image = 'C:/Users/Marco/Desktop/project/blank_states_img.gif'
screen.addshape(image)



turtle = Turtle()
turtle.shape(image)

already_guessed = []

score = Scoreboard()

game_on = True

while game_on:
    answer = screen.textinput(title='Guess the State',prompt="What's another State name?")
    if answer == 'exit':
        game_on = False
        
    for x in range(len(state)):
        if state[x-1] == answer and answer not in already_guessed:
            newx = xcor[x-1]
            newy = ycor[x-1]
            new_state = Turtle()
            new_state.ht()
            new_state.penup()
            new_state.color('black')
            new_state.goto(newx,newy)
            new_state.write(f"{answer}", align='center')
            already_guessed.append(answer)
            score.my_score()

screen.exitonclick()
