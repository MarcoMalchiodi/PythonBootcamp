from turtle import Turtle

starting_pos = [(0,0),(-20,0),(-40,0)]
move_distance = 20
r = 0
l = 180
u = 90
d = 270

class Snake:
    
    def __init__(self):
        self.snakes = []
        self.snake_creation()
        self.head = self.snakes[0]

    
    def snake_creation(self):
        for x in starting_pos:
            self.add(x)
    
    def add(self,position):
        turtle = Turtle('square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(position)
        self.snakes.append(turtle)
    
    def extend(self):
        self.add(self.snakes[-1].position())
    
    
    def move(self):
        for x in range(len(self.snakes)-1,0,-1):
            newx = self.snakes[x-1].xcor()
            newy = self.snakes[x-1].ycor()
            self.snakes[x].goto(newx,newy)
        self.head.forward(move_distance)
    
    
    def up(self):
        if self.head.heading() != d:
            self.head.setheading(u)
        else:
            pass
        
    
    def left(self):
        if self.head.heading() != r:
            self.head.setheading(l)
        else:
            pass
    
    def down(self):
        if self.head.heading() != u:
            self.head.setheading(d)
        else:
            pass
    def right(self):
        if self.head.heading() != l:
            self.head.setheading(r)
        else:
            pass