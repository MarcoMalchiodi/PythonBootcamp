from turtle import Turtle

class Opponent(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.goto(-350,0)
        self.speed(10)
        
    def movement(self):
        self.forward(10)
        y = self.ycor()
        if y > 280:
            self.setheading(270)
        elif y < -280:
            self.setheading(90)