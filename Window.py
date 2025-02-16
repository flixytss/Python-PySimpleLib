import pygame as pg
import sys

pg.init()

rects = pg.sprite.Group()
Labels = pg.sprite.Group()

class window():
    def __init__(self, RESIZABLE):
        super().__init__()

        if RESIZABLE==True:
            self.win = pg.display.set_mode((800,600), pg.RESIZABLE)
        else:
            self.win = pg.display.set_mode((800,600))
        
        self.fps=60
        self.color=(255,255,255)

        self.ShouldClose=True
        
    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    if self.ShouldClose==True:
                        sys.exit()
                        pg.quit()
                    else:
                        print("ShouldClose: False")
            self.win.fill(self.color)

            self.StartDrawing()
            
            pg.display.update()
            pg.time.Clock().tick(self.fps)
    def StartDrawing(self):
        for sprite in rects:
            sprite.draw()
        for sprite in Labels:
            sprite.draw()

def Window():
    win = window(True)
    return win