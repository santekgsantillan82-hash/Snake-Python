import pygame as pg

pg.init()
pantallita = pg.display.set_mode((720, 480))
tiempo = pg.time.Clock()
corriendo = True
dt = 0
pos_jug = pg.Vector2(pantallita.get_width()/2, pantallita.get_height()/2)
sp = pg.Surface((50, 50), pg.SRCALPHA)



jug= pg.Rect(pos_jug.x, pos_jug.y, 50, 50)
pared1 = pg.Rect(0, 0, 20, 480)
pared2 = pg.Rect(700, 0, 20, 480)
pared3 = pg.Rect(100, 100, 20, 120)
pared4 = pg.Rect(0, 0, 20, 480)


while corriendo: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            corriendo = False 

    pantallita.fill("red")

    pg.draw.rect(pantallita, "black", jug)
    pg.draw.rect(pantallita, "black", pared1)
    pg.draw.rect(pantallita, "black", pared2)
    pg.draw.rect(sp, "black", pared3)
    pg.draw.rect(sp, "black", pared4)

    sp_rot = pg.transform.rotate(sp, 90)

    if jug.colliderect(pared1):
          jug.left = pared1.right
    if jug.colliderect(pared2):
      jug.right = pared2.left

    controles = pg.key.get_pressed()
    if controles[pg.K_w]:
            jug.move_ip(0, -10)
    if controles[pg.K_s]:
            jug.move_ip(0, 10)
    if controles[pg.K_a]:
            jug.move_ip(-10, 0)
    if controles[pg.K_d]:
            jug.move_ip(10, 0)

    pg.display.flip()

    dt = tiempo.tick(60) / 1000

pg.quit()