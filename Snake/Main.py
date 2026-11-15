
import pygame as pg
from menu import Menu
from juego import Juego

pg.init()
pantallita = pg.display.set_mode((720, 480))
tiempo = pg.time.Clock()
pg.display.set_caption("EcoSnake")

corriendo = True
enMenu = True

menu = Menu()
juego = Juego(pantallita)


while corriendo:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            corriendo = False

    if enMenu:
        menu.dibujar(pantallita)
        opcion = menu.actualizar()
        if opcion == "play":
            enMenu = False

    else:
        if juego.actualizar():
            pg.time.wait(500)

        juego.dibujar()

    pg.display.flip()

    dt = tiempo.tick(10) / 1000


pg.quit()
