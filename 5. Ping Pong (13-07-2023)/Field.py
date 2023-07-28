from turtle import Turtle

class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(100,200)
        self.write(self.r_score, align='center', font=("Courier",80,"normal"))
        self.goto(-100,200)
        self.write(self.l_score, align='center', font=("Courier",80,"normal"))
        
        
    def score(self, r, l):
        self.clear()
        self.r_score += r
        self.l_score += l
        self.goto(100,200)
        self.write(self.r_score, align='center', font=("Courier",80,"normal"))
        self.goto(-100,200)
        self.write(self.l_score, align='center', font=("Courier",80,"normal"))
        