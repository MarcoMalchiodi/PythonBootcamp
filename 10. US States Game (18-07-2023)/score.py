from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.ht()
        self.color('black')
        self.penup()
        self.goto(140,180)
        self.score = 0
        self.write(f'Your current score: {self.score}/50', align="center", font=("Arial", 12, "normal"))
    
    def my_score(self):
        self.score += 1
        self.clear()
        self.write(f'Your current score: {self.score}/50', align="center", font=("Arial", 12, "normal"))