import pygame as pg

pg.init()
pantallita = pg.display.set_mode((720, 480))
tiempo = pg.time.Clock()
corriendo = True
dt = 0
movy = 0
movx = 0
celd= 20
iniciado= False
fuente = pg.font.Font(None, 40)
texto1= fuente.render("Play", True, "white")
texto2= fuente.render("Opciones", True, "white")
texto3= fuente.render("Exit", True, "white")
texto4= fuente.render("Presiona La Tecla Espacio para inicia", True, "black")
Menu= True
pos_jug = pg.Vector2(pantallita.get_width()/2, pantallita.get_height()/2)

jugador =[
    pg.Rect(pos_jug.x+(i*30), pos_jug.y, 20, 10)
    for i in range(11)
]

paredes= [
    pg.Rect(0, 0, 20, 480),
    pg.Rect(700, 0, 20, 480),
    pg.Rect(0, 0, 720, 20),
    pg.Rect(0, 460, 720, 20),
]

while corriendo: 
    for event in pg.event.get():
        if event.type == pg.QUIT:
            corriendo = False 
    pantallita.fill("white")

    if Menu:
        pantallita.fill("white")

        bot1 = pg.Rect(235, 70, 250, 60)
        pg.draw.rect(pantallita, (0, 170, 228), bot1)
        pantallita.blit(texto1, (330, 90))

        bot2 = pg.Rect(235, 220, 250, 60)
        pg.draw.rect(pantallita, (0, 170, 228), bot2)
        pantallita.blit(texto2, (300, 240))

        bot3 = pg.Rect(235, 370, 250, 60)
        pg.draw.rect(pantallita, (0, 170, 228), bot3)
        pantallita.blit(texto3, (330, 385))

        mouse = pg.mouse.get_pos()
        mouseEstado = pg.mouse.get_pressed()

        if bot1.collidepoint(mouse):
            if mouseEstado[0]:
                Menu = False

    else:

        controles = pg.key.get_pressed()
        if controles[pg.K_SPACE]:
            iniciado = True
            movx= -celd
            movy= 0

        if iniciado:
            if controles[pg.K_w]:
                movy= -celd
                movx= 0
            if controles[pg.K_s]:
                movy= celd
                movx= 0
            if controles[pg.K_a]:
                movx= -celd
                movy= 0
            if controles[pg.K_d]:
                movx= celd
                movy= 0
            for i in range(len(jugador)-1, 0, -1):
                jugador[i].topleft = jugador[i-1].topleft
            
            jugador[0].move_ip(movx, movy)
            
            for i in jugador[1:]:
                if jugador[0].colliderect(i):
                    Menu= True
        else:
            pantallita.blit(texto4, (100, 90))

        for i in jugador:
            if jugador[0]==i:
                pg.draw.ellipse(pantallita, (0, 170, 228), (i.x, i.y, 30, 20))
            else:
                pg.draw.ellipse(pantallita, (0, 170, 228), (i.x, i.y, 30, 15))
    
        for i in paredes:
            pg.draw.rect(pantallita, (0, 170, 228), i)

        if jugador[0].colliderect(paredes[0]):
            jugador[0].left = paredes[0].right
        if jugador[0].colliderect(paredes[1]):
            jugador[0].right = paredes[1].left
        if jugador[0].colliderect(paredes[2]):
            jugador[0].top = paredes[2].bottom
        if jugador[0].colliderect(paredes[3]):
            jugador[0].bottom = paredes[3].top





    pg.display.flip()

    dt = tiempo.tick(10) / 1000

pg.quit()