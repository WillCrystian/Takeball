from turtle import Turtle
import random

class Bola(Turtle):
    def __init__(self):
        super(Bola, self).__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(0.8)
        self.mover_x = 1
        self.mover_y = 1      

    
    def mover_bolinha(self):
        novo_x = self.xcor() + self.mover_x
        novo_y = self.ycor() + self.mover_y
        self.goto(novo_x, novo_y)