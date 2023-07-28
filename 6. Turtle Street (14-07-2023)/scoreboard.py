from turtle import Turtle

FONT = ("Courier", 12, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(-270,270)
        self.score = 0
        self.write(f'Your current level: {self.score}', font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f'Your current level: {self.score}', font=FONT)
    
    def game_over(self):
        gamo = Turtle()
        gamo.penup()
        gamo.ht()
        gamo.goto(0,0)
        gamo.write('Game Over', align='center', font=('Arial',12,'normal'))
