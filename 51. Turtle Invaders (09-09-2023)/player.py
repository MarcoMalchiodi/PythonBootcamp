from turtle import Turtle, ontimer
from bullet import Bullet
from fence import Fence
from alien import Alien


first_row_direction = 'right'
second_row_direction = 'left'
third_row_direction = 'right'

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('triangle')
        self.color('white')
        self.penup()
        self.left(90)
        self.goto(x=0,y=-220)
        self.bullet_list = []
        self.fences = []
        self.enemies = []
        
    def create_fences(self):
        xpos = 300
        ypos = 0
        counter = 0
        for x in range(21):
            if counter <= 6:
                fence = Fence()
                fence.goto(x=xpos,y=ypos)
                xpos -= 100
                counter += 1
                self.fences.append(fence)
            elif counter >= 6 and counter <= 13:
                ypos = -50
                xpos += 100
                fence = Fence()
                fence.goto(x=xpos,y=ypos)
                counter += 1
                self.fences.append(fence)
            elif counter > 13 and counter < 20:
                ypos = -100
                xpos -= 100
                fence = Fence()
                fence.goto(x=xpos,y=ypos)
                counter += 1
                self.fences.append(fence)
            else:
                ypos = -100
                xpos += 600
                fence = Fence()
                fence.goto(x=xpos,y=ypos)
                self.fences.append(fence)
    
    
    def create_enemies(self):
        xpos = 200
        ypos = 200
        counter = 0
        for x in range(19):
            if counter <= 6:
                alien = Alien()
                alien.goto(x=xpos,y=ypos)
                xpos -= 70
                counter += 1
                self.enemies.append(alien)
            elif counter >= 6 and counter <= 13:
                ypos = 150
                xpos += 70
                alien = Alien()
                alien.goto(x=xpos,y=ypos)
                alien.direction = 'left'
                counter += 1
                self.enemies.append(alien)
            elif counter > 13 and counter < 20:
                ypos = 100
                xpos -= 70
                alien = Alien()
                alien.goto(x=xpos,y=ypos)
                counter += 1
                self.enemies.append(alien)
            

            
    def go_right(self):
        newx = self.xcor() + 30
        self.goto(y=self.ycor(),x=newx)
    def go_left(self):
        newx = self.xcor() - 30
        self.goto(y=self.ycor(),x=newx)
    
    def shoot(self):
        cannot_shoot = True
        if len(self.bullet_list) == 0:
            bullet = Bullet(player=self)
            self.bullet_list.append(bullet)
            bullet.move(list=self.fences,alien_list=self.enemies)
        else:
            for bulletto in self.bullet_list:
                if bulletto.ycor() <= 250:
                    cannot_shoot=True
                else:
                    cannot_shoot=False
        if cannot_shoot==False:
            new_bullet = Bullet(player=self)
            self.bullet_list.append(new_bullet)
            new_bullet.move(list=self.fences,alien_list=self.enemies)



    def aliens_moving(self):
        for x in range(7):
            self.enemies[x].alien_move_right()
            if self.enemies[x].xcor() >= 320:
                self.enemies[x].hideturtle()
                ycor = self.enemies[x].ycor()
                self.enemies[x].goto(x=-340,y=ycor)
                self.enemies[x].showturtle()
        for x in range(7,14):
            self.enemies[x].alien_move_left()
            if self.enemies[x].xcor() <= -340:
                self.enemies[x].hideturtle()
                ycor = self.enemies[x].ycor()
                self.enemies[x].goto(x=320,y=ycor)
                self.enemies[x].showturtle()
        for x in range(14,19):
            self.enemies[x].alien_move_right()
            if self.enemies[x].xcor() >= 320:
                self.enemies[x].hideturtle()
                ycor = self.enemies[x].ycor()
                self.enemies[x].goto(x=-340,y=ycor)
                self.enemies[x].showturtle()

