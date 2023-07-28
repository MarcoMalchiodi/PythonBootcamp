from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=5)
        self.goto(350,0)
        self.speed(5)
    

    def up(self):
        newy = self.ycor() + 40
        self.goto(self.xcor(),newy)
    
    def down(self):
        newy = self.ycor() - 40
        self.goto(self.xcor(),newy)
