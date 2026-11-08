import pygame as pg

pg.init()
pantallita = pg.display.set_mode((720, 480))
tiempo = pg.time.Clock()
corriendo = True
dt = 0
pos_jug = pg.Vector2(pantallita.get_width()/2, pantallita.get_height()/2)




while corriendo: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            corriendo = False 
    pantallita.fill("red")

    pg.draw.ellipse(pantallita, "blue", (pos_jug.x, pos_jug.y, 40, 120))
    pg.draw.ellipse(pantallita, "green", (pos_jug.x -100, pos_jug.y, 40, 40))
    controles = pg.key.get_pressed()
    if controles[pg.K_w]:
        pos_jug.y -= 300 * dt
    if controles[pg.K_s]:
        pos_jug.y += 300 *dt
    if controles[pg.K_a]:
        pos_jug.x -= 300 * dt
    if controles[pg.K_d]:
        pos_jug.x += 300 * dt    

    pg.display.flip()

    dt = tiempo.tick(60) / 1000

pg.quit()