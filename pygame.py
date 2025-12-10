import pygame as pg

pg.init()

window = pg.display.set.mode((800,600))
pg.display.set_caption("Conceptos basicos")

background = (0,0,0)

running = True
while running:
    for event in pg.event.get():
        if event.type() == pg.QUIT:
            running = False
    window.fill(background)
pg.quit()