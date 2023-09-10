from turtle import Turtle

class Alien(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.speed(10)
        self.right(90)
        self.color('green')

    
    def alien_move_right(self):
        newx = self.xcor() + 30
        self.goto(x=newx,y=self.ycor())
    
    def alien_move_left(self):
        newx = self.xcor() - 30
        self.goto(x=newx,y=self.ycor())
        
    
    