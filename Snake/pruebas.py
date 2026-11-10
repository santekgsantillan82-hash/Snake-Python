import pygame as pg

pg.init()
pantallita = pg.display.set_mode((720, 480))
tiempo = pg.time.Clock()
corriendo = True
dt = 0
movy = 0
movx = 0
iniciado= False
pos_jug = pg.Vector2(pantallita.get_width()/2, pantallita.get_height()/2)

jugador =[
    pg.Rect(pos_jug.x, pos_jug.y, 30, 15),
    pg.Rect(pos_jug.x+20, pos_jug.y, 30, 15),
    pg.Rect(pos_jug.x+40, pos_jug.y, 30, 15),
    pg.Rect(pos_jug.x+60, pos_jug.y, 30, 15),
    pg.Rect(pos_jug.x+80, pos_jug.y, 30, 15),
    pg.Rect(pos_jug.x+100, pos_jug.y, 30, 15),
    pg.Rect(pos_jug.x+120, pos_jug.y, 30, 15),
    pg.Rect(pos_jug.x+140, pos_jug.y, 30, 15),
    pg.Rect(pos_jug.x+160, pos_jug.y, 30, 15),
    pg.Rect(pos_jug.x+180, pos_jug.y, 30, 15),
    pg.Rect(pos_jug.x+200, pos_jug.y, 30, 15)
]

pared1 = pg.Rect(0, 0, 20, 480)
pared2 = pg.Rect(700, 0, 20, 480)
pared3 = pg.Rect(0, 0, 720, 20)
pared4 = pg.Rect(0, 460, 720, 20)


while corriendo: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            corriendo = False 
    pantallita.fill("red")

    for i in jugador:
        if jugador[0]==i:
            pg.draw.ellipse(pantallita, "black", (i.x, i.y, 30, 20))
        else:
            pg.draw.ellipse(pantallita, "black", (i.x, i.y, 30, 15))
    
    pg.draw.rect(pantallita, "black", pared1)
    pg.draw.rect(pantallita, "black", pared2)
    pg.draw.rect(pantallita, "black", pared3)
    pg.draw.rect(pantallita, "black", pared4)

    pos=[]

    for i in jugador:
        pos.append(i.topleft)

    for i in range(len(jugador)-1, 0, -1):
        jugador[i].topleft = jugador[i-1].topleft


    jugador[0].move_ip(movx, movy)

    controles = pg.key.get_pressed()
    if controles[pg.K_SPACE]:
        iniciado = True

    if iniciado:
        if controles[pg.K_w]:
           movy= -15
           movx= 0
        if controles[pg.K_s]:
           movy= 15
           movx= 0
        if controles[pg.K_a]:
           movx= -15
           movy= 0
        if controles[pg.K_d]:
           movx= 15
           movy= 0


    pg.display.flip()

    dt = tiempo.tick(10) / 1000

pg.quit()