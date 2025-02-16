import pygame as pg

import extension.Window as window

class labelClass(pg.sprite.Sprite):
    def __init__(self, win, font, Size, Text, X, Y):
        super().__init__()
        self.image=pg.Surface((0,0))
        self.rect=self.image.get_rect()

        self.win=win
        self.font=font
        self.Text=Text
        self.size=Size
        self.x=X
        self.y=Y
    def draw(self):
        self.win.blit(pg.font.Font(self.font, self.size).render(self.Text, 1, (0,0,0)), (self.x,self.y))

        window.Labels.add(self)

def Label(Surface, Text, Size, Font, X, Y):
    label = labelClass(Surface, Font, Size, Text, X, Y)

    label.draw()

    return label