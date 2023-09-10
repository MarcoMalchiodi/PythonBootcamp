from turtle import Turtle

class Bullet(Turtle):
    def __init__(self,player):
        super().__init__()
        self.hideturtle()
        self.shape('square')
        self.color('black')
        self.shapesize(stretch_wid=0.6,stretch_len=0.22)
        self.penup()
        self.speed(10)
        self.goto(x=player.xcor(),y=player.ycor())
        self.showturtle()
        self.color('white')

    def check_collision(self,list):
        for x in list:
            if self.distance(x) <= 20:
                if self.color() != ('black','black') and x.color() != ('black','black'):
                    self.color('black')
                    self.hideturtle
                    self.goto(x=600,y=600)
                    x.color('black')
    def check_alien(self,alien_list):
        global score
        for x in alien_list:
            if self.distance(x) <= 15:
                if self.color() != ('black','black') and x.color() == ('green','green'):
                    self.color('black')
                    self.hideturtle()
                    self.goto(x=600,y=600)
                    x.color('black')
                    x.hideturtle()

                    
                    
        
    def move(self,list,alien_list):
        if self.ycor() < 260:
            newy = self.ycor() + 5
            self.goto(x=self.xcor(),y=newy)
            self.check_collision(list=list)
            self.check_alien(alien_list=alien_list)
            self.move(list=list,alien_list=alien_list)
        else:
            return 
        
            
            