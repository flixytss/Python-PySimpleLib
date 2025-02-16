import pygame as pg
from extension.Window import rects

class Vector2():
    def __init__(self):
         self.X=0
         self.Y=0

class rect(pg.sprite.Sprite):
    def __init__(self, win, X, Y, Widht, Height, Lenght, Parent):
        super().__init__()
        self.image=pg.Surface((0,0))
        self.rect=self.image.get_rect()

        self.Vector = Vector2()

        self.render = pg.Rect(self.Vector.X, self.Vector.Y, Widht, Height)

        self.Vector.X=X
        self.Vector.Y=Y

        self.win=win
        self.lenght=Lenght

        self.Widht=Widht
        self.Height=Height

        self.Parent=Parent

        self
    def draw(self):
        self.render = pg.Rect(self.Vector.X, self.Vector.Y, self.Widht, self.Height)
        
        pg.draw.rect(self.win, (0,0,0), self.render, self.lenght)
def Rect(win, X, Y, Widht, Height, Lenght):
        rect_obj = rect(win, X, Y, Widht, Height, Lenght)

        rects.add(rect_obj)

        return rect_obj