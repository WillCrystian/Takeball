from turtle import Turtle

class Raquete(Turtle):
    def __init__(self, pos_x, pos_y):
        super(Raquete, self).__init__()
        self.penup()
        self.shape('square')
        self.shapesize(0.4, 3)
        self.goto(pos_x, pos_y)
        self.vel = 20
        
    def mover_direita(self):
        nova_pos = self.xcor() + self.vel
        
        if nova_pos < -180:
            nova_pos = -180
            
        if nova_pos > 180:
            nova_pos = 180
            
        self.goto(nova_pos, self.ycor())
        
    def mover_esquerda(self):        
        nova_pos = self.xcor() - self.vel
        
        if nova_pos < -180:
            nova_pos = -180
            
        if nova_pos > 180:
            nova_pos = 180
        
        self.goto(nova_pos, self.ycor())
        
        
       
   
        
        