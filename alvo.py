from ursina import *
import random
import main


class Alvo(Entity):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.model = 'quad'
        self.name = "alvo"
        self.scale_x = 0.5
        self.scale_y = 0.2
        self.color = color.orange
        self.y = 0
        self.collider = 'box'
        self.setcolor()
    def update(self):
        if self.intersects().hit:
            #destroi a si mesmo caso colida

            destroy(self)

    def setcolor(self):
        r = random.random()
        if r > 0.95 and r < .98:
            self.color = color.red
        elif r > .98:
            self.color = color.pink
        elif r < 0.2:
            self.color = color.green
        elif r > .30 and r < .32:
            self.color = color.yellow




