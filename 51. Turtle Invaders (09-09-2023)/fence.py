from turtle import Turtle

class Fence(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=0.8,stretch_len=3)
        self.penup()
        self.speed(10)
        