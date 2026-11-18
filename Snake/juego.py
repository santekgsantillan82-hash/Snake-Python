
import pygame as pg
import random as rd
from enco import recurso
class Juego():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.celd = 20
        self.tamX = self.pantalla.get_width()
        self.tamY = self.pantalla.get_height()

        self.paredes = [
            pg.Rect(0, 0, 20, self.tamY),
            pg.Rect(self.tamX -20, 0, 20, self.tamY),
            pg.Rect(0, 0, self.tamX, 20),
            pg.Rect(0, self.tamY -20, self.tamX, 20),
        ]
        self.basuras = [
            "img/bolsa_plastico.png",
            "img/bollo_papel.png",
            "img/refresco.png",
            "img/basura.png"
        ]
        self.imgBas= []
        for i in self.basuras:
            img = pg.image.load(recurso(i)).convert_alpha()
            img = pg.transform.scale(img, (20, 20))
            self.imgBas.append(img)



        self.fuente = pg.font.Font(None, max(18, self.tamX// 15))
        self.fuente2 = pg.font.Font(None, max(22, self.tamX// 13))
        self.text1 = self.fuente.render("Presiona al tecla ESPACIO para inicia", True, "white")

        self.reInicio()

    def reInicio(self):
        self.movx = 0
        self.movy = 0
        self.ultX = 0
        self.ultY = 0
        self.cantBas = 0
        self.iniciado = False

        self.pos_jug = pg.Vector2(self.pantalla.get_width() / 2, self.pantalla.get_height() / 2)

        self.jugador = [
            pg.Rect(self.pos_jug.x + (i * 20), self.pos_jug.y, 20, 10)
            for i in range(3)
        ]

        self.manza = pg.Rect(0, 0, 20, 20)
        self.NewManza()

        self.actuCont()

    def controles(self):
        controles = pg.key.get_pressed()

        if controles[pg.K_SPACE] and not self.iniciado:
            self.iniciado = True
            self.movx = -self.celd
            self.movy = 0
            self.ultX = self.movx
            self.ultY = self.movy

        if self.iniciado:
            if controles[pg.K_w] and self.ultY != self.celd:
                self.movy = -self.celd
                self.movx = 0

            if controles[pg.K_s] and self.ultY != -self.celd:
                self.movy = self.celd
                self.movx = 0

            if controles[pg.K_a] and self.ultX != self.celd:
                self.movx = -self.celd
                self.movy = 0

            if controles[pg.K_d] and self.ultX != -self.celd:
                self.movx = self.celd
                self.movy = 0

    def movimiento(self):
        for i in range(len(self.jugador) - 1, 0, -1):
            self.jugador[i].topleft = self.jugador[i-1].topleft

        self.jugador[0].move_ip(self.movx, self.movy)

        self.ultY = self.movy
        self.ultX = self.movx

    def colisiones(self):
        for i in self.jugador[1:]:
            if self.jugador[0].colliderect(i):
                return True
            

        if self.jugador[0].colliderect(self.paredes[0]):
            self.jugador[0].left = self.paredes[0].right
            return True

        if self.jugador[0].colliderect(self.paredes[1]):
            self.jugador[0].right = self.paredes[1].left
            return True

        if self.jugador[0].colliderect(self.paredes[2]):
            self.jugador[0].top = self.paredes[2].bottom
            return True

        if self.jugador[0].colliderect(self.paredes[3]):
            self.jugador[0].bottom = self.paredes[3].top
            return True

        return False

    def NewManza(self):
        while True:

            self.manXN = rd.randrange(20, self.tamX -20, 20)
            self.manYN = rd.randrange(20, self.tamY -20, 20)

            self.manza.update(self.manXN, self.manYN, 20, 20)

            if self.manza.collidelist(self.jugador) == -1:
                break

        self.basura = rd.choice(self.imgBas)
        
    def ajusText(self, superficie):
        anchMax = self.tamX -40
        if superficie.get_width() > anchMax:
            escale= anchMax / superficie.get_width()
            newTam = (int(superficie.get_width() * escale), int(superficie.get_height() * escale)) 
            superficie = pg.transform.smoothscale(superficie, newTam)
        return superficie

    def actuCont(self):
        self.text2 = self.ajusText(self.fuente2.render(f"Basura comida: {self.cantBas}", True, "white"))

    def dibujar(self):
        self.pantalla.fill((24, 43, 39))

        for x in range(0, self.tamX, 20):
            pg.draw.line(self.pantalla, (34, 57, 49), (x, 0), (x, self.tamY))

        for y in range(0, self.tamY, 20):
            pg.draw.line(self.pantalla, (34, 57, 49), (0, y), (self.tamX, y))

        for i in self.jugador:
            if self.jugador[0] == i:
                pg.draw.ellipse(
                    self.pantalla,
                    (213, 240, 165),
                    (i.x, i.y, 20, 20)
                )

            else:
                pg.draw.rect(
                    self.pantalla,
                    (168, 217, 108),
                    (i.x, i.y, 20, 20)
                )

        for i in self.paredes:
            pg.draw.rect(
                self.pantalla,
                (52, 74, 64),
                i
            )

        self.pantalla.blit(self.basura, (self.manza.x, self.manza.y))

        if not self.iniciado:
            rect = self.text1.get_rect(center=(self.tamX // 2, self.tamY // 2 - 40))
            self.pantalla.blit(self.text1, rect)
        else:
            self.pantalla.blit(self.text2, (0, 0))

    def actualizar(self):
        self.controles()

        if self.iniciado:
            self.movimiento()

            if self.colisiones():
                self.reInicio()
                return True

            if self.jugador[0].colliderect(self.manza):
                self.jugador.append(pg.Rect(0, 0, 20, 20))
                self.cantBas += 1
                self.actuCont()
                self.NewManza()

        return False
