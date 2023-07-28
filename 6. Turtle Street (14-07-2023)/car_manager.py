from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
rand1 = 1
rand2 = 6



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.cars = []
    
    def create_cars(self):
        global rand1
        global rand2
        random_num = random.randint(rand1,rand2)
        if random_num == 1:
            car = Turtle()
            car.shape('square')
            car.penup()
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.color(random.choice(COLORS))
            randomy = random.randint(-250,250)
            car.goto(300,randomy)
            self.cars.append(car)
    
    def move(self):
        for x in self.cars:
            x.backward(STARTING_MOVE_DISTANCE)
        
    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        global MOVE_INCREMENT
        global rand2
        
        if rand2 > 4:
            rand2 -= 1
        
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT