from ursina import *
class Player(Entity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = 'quad'
        self.name = "player"
        self.scale_x = 2
        self.scale_y = 0.3
        self.color = color.green
        self.velocidade_x = 0
        self.collider = 'box'
        self.y = -4

        #define se ele vai ser extendido de tamanho ou nao
        self.mode = 0
        #multiplicador de velocidade , assume o valor 0 quando o jogo é pausado
        self.multiplicador_velocidade = 1
        # fator de velocidade de acordo com os modos do jogador
        self.velocidade_mudanca = 0.2
        self.max_x = 0

    def update(self):

        # extende/diminui de tamanho
        self.changemodes()
        # variavel que define a borda da tela, dependendo do tamanho do player
        self.change_x_limit()
        #verifica colisoes com as paredes
        if self.x > self.max_x:
            self.x = self.max_x
        if self.x < -self.max_x:
            self.x = -self.max_x

        self.x += self.velocidade_x * self.multiplicador_velocidade

    #movimentaçao
    def input(self,key):
        if key == 'a':
            self.velocidade_x = -self.velocidade_mudanca

        if key == 'd':
            self.velocidade_x = self.velocidade_mudanca

        if key == 'a up' or key == 'd up':
            self.velocidade_x = 0

    def changemodes(self):
        if self.mode == 1:
            self.scale_x = 4

        elif self.mode == 2:
            self.scale_x = 1.4

        elif self.mode == 0:
            self.scale_x = 2

        elif self.mode == 3:
            self.velocidade_mudanca = 0.3

        if self.mode != 3:
            self.velocidade_mudanca = 0.2


    def change_x_limit(self):
        self.max_x = (14.55/2) - (self.scale_x/2)
