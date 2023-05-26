from turtle import *
from campo import Campo
from raquete import Raquete
from bola import Bola

import time

tela = Screen()
tela.setup(600,600)
tela.title('Takeball')
tela.tracer(0)
tela.listen()

campo = Campo(210, 220)
r1 = Raquete(0, -200)
r2 = Raquete(0, 200)
bola = Bola()

tela.onkeypress(r1.mover_esquerda, 'Left')
tela.onkeypress(r1.mover_direita, 'Right')

tela.onkeypress(r2.mover_esquerda, 'a')
tela.onkeypress(r2.mover_direita, 'd')


jogo_on = True

while jogo_on:
    time.sleep(0.05) 
    bola.mover_bolinha()
    tela.update()

tela.exitonclick()