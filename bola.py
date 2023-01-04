import colorsys
import random

from ursina import *

import main


class Bola(Entity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = 'quad'
        self.name = "Bola"
        self.scale_x = 0.2
        self.scale_y = 0.2
        self.color = color.blue
        self.velocidade_x = 0.1
        self.velocidade_y = -0.1
        self.y = 0
        self.collider = 'box'
        # verifica se a bola esta sendo exibida
        self.natela = False
        self.multiplicador_velocidade = 1
        self.disable()
    def update(self):


        # se a bola passar de y=-4 ela esta fora da tela
        if self.y < -5:
            self.natela = False
        # define colisoes da bola
        if self.x >= 7 or self.x <= -7 :
            self.velocidade_x *= -1

        if self.y >= 4:
            self.velocidade_y*=-1

        # muda a posicao da bola de acordo com a velocidade
        self.x += self.velocidade_x * self.multiplicador_velocidade
        self.y += self.velocidade_y * self.multiplicador_velocidade

        #verifica colisoes
        if self.intersects().hit:
            colidido = self.intersects().entities[0]

            # caso ouver colisao . inverte a velocidade
            self.velocidade_y *= -1
            if str(colidido) == 'player':
                self.y += 0.1
                a = Audio('batendo.wav', pitch=1, loop=False, autoplay=True)
            #verifica se a bola colidiu com um alvo
            if str(colidido) == 'alvo':
                # define quantos pontos esse alvo vai dar, se for verde vai dar 3 pontos
                bonus = 3 if colidido.color == color.green else 1
                a = Audio('batendo_alvo.wav', pitch=1, loop=False, autoplay=True)
                self.verifica_alvo(colidido)
                #remove o alvo da lista de alvos ao colidir
                main.alvos.pop(0)
                #soma pontos
                main.pontos +=bonus

    def verifica_alvo(self,colidido):

        if colidido.color == color.red:
            main.player_mode = 1 if main.player_mode != 1 else 0

        if colidido.color == color.pink:
            main.player_mode = 2 if main.player_mode != 2 else 0

        if colidido.color == color.yellow:
            main.player_mode = random.choice((1,2,3))