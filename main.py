# verifica se o jogador esta usando o bonus
player_mode = 0
#conta pontos do jogador
pontos = 0
#lista de alvos do jogador
alvos = []
pausa = False
if __name__ == '__main__':
    from ursina import *
    import main
    from bola import Bola
    from alvo import Alvo
    from player import Player
    #texto dos pontos
    t = Text(text='ab', scale=16, x=-7, y= 3.5)
    t.text = str(pontos)
    # define variaveis
    app,p,b = Ursina(), Player(), Bola()
    window.fullscreen = True
    # funcao para criar todos os alvos
    def criaalvos():
        global alvos


        for linha in range(5):
            for coluna in range (14):
                #cria alvos
                a = Alvo(x = -6.5+coluna)
                a.y = linha -1.3
                main.alvos.append(a)

    criaalvos()


    def resetarpontos():
        main.pontos = 0

    def resetarjogo():
        main.player_mode = 0
        criaalvos()
        b.enable()
        b.x = p.x
        b.y = p.y - 0.2
        b.y = p.y + 0.5
        b.velocidade_y = 0.1
        b.natela = True
        main.pontos = 0


    def input(key):
        global pausa
        # lança a bola se apertar b e a bola nao estiver na tela
        if key == 'b' and b.natela == False:
            main.alvos = []
            resetarjogo()

        if key == 'escape':
                mult = 0 if pausa == False else 1
                p.multiplicador_velocidade = mult
                b.multiplicador_velocidade = mult
                pausa = True if pausa == False else False

    def update():

        # verifica se todos os alvos foram destruidos e cria novos
        if len(main.alvos) == 0:
            main.alvos = []
            criaalvos()
        # verifica e ativa/desativa o super do jogador
        p.mode = main.player_mode
        t.text = str(main.pontos) if pausa == False else "Pausado"
        if b.natela == False:
            t.text = 'Aperte B para Iniciar '
    app.run()
