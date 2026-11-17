
import pygame as pg
from menu import Menu
from juego import Juego

Dificultades={
    "fac": {"tam": (240, 360), "vel": 10},
    "nor": {"tam": (360, 480), "vel": 15},
    "dif": {"tam": (480, 600), "vel": 20}
}

pg.init()
pantallita = pg.display.set_mode((720, 480))
tiempo = pg.time.Clock()
pg.display.set_caption("EcoSnake")

corriendo = True
enMenu = True
selMenu = False
vel = 10
menu = Menu()
juego = Juego(pantallita)


while corriendo:
    click = False
    for event in pg.event.get():
        if event.type == pg.QUIT:
            corriendo = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            click = True

    if enMenu:
        if not selMenu:
            menu.dibujar(pantallita)
            opcion = menu.actualizar(click)
            if opcion == "play":
                selMenu = True
        else: 
            menu.selDif(pantallita)
            opcion = menu.actualizar(click)

            if opcion in Dificultades:
                cambiar = Dificultades[opcion]
                pantallita = pg.display.set_mode(cambiar["tam"])
                vel = cambiar["vel"]
                juego = Juego(pantallita)
                enMenu = False

    else:
        if juego.actualizar():
            pg.time.wait(500)

        juego.dibujar()

    pg.display.flip()

    dt = tiempo.tick(vel) / 1000


pg.quit()
