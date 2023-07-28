from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

file = open('highscore.txt','r')
SCORE = int(file.read())
file.close()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        global SCORE
        self.score = 0
        self.highscore = SCORE
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            file = open('highscore.txt', mode='w')
            file.write(str(self.highscore))
            file.close()
            
        self.score = 0
        self.update_scoreboard()
        
    #def game_over(self):
        #self.goto(0, 0)
        #self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

