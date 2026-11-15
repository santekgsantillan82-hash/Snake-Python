
import pygame as pg
import random as rd

class Juego():
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.celd = 20

        self.paredes = [
            pg.Rect(0, 0, 20, 480),
            pg.Rect(700, 0, 20, 480),
            pg.Rect(0, 0, 720, 20),
            pg.Rect(0, 460, 720, 20),
        ]

        self.fuente = pg.font.Font(None, 35)
        self.fuente2 = pg.font.Font(None, 30)
        self.text1 = self.fuente.render("Presiona La Tecla Espacio para inicia", True, "black")

        self.reInicio()

    def reInicio(self):
        self.movx = 0
        self.movy = 0
        self.cantBas = 0
        self.iniciado = False

        self.pos_jug = pg.Vector2(self.pantalla.get_width() / 2, self.pantalla.get_height() / 2)

        self.jugador = [
            pg.Rect(self.pos_jug.x + (i * 30), self.pos_jug.y, 20, 10)
            for i in range(3)
        ]

        self.manX = rd.randrange(20, 700, 20)
        self.manY = rd.randrange(20, 460, 20)

        self.manza = pg.Rect(self.manX, self.manY, 15, 15)

        self.text2 = self.fuente2.render(f"La cantidad de basura comida es: {self.cantBas}", True, "black" )

    def controles(self):
        controles = pg.key.get_pressed()

        if controles[pg.K_SPACE]:
            self.iniciado = True
            self.movx = -self.celd
            self.movy = 0

        if self.iniciado:
            if controles[pg.K_w]:
                self.movy = -self.celd
                self.movx = 0

            if controles[pg.K_s]:
                self.movy = self.celd
                self.movx = 0

            if controles[pg.K_a]:
                self.movx = -self.celd
                self.movy = 0

            if controles[pg.K_d]:
                self.movx = self.celd
                self.movy = 0

    def movimiento(self):
        for i in range(len(self.jugador) - 1, 0, -1):
            self.jugador[i].topleft = self.jugador[i-1].topleft

        self.jugador[0].move_ip(self.movx, self.movy)

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
        self.manXN = rd.randrange(20, 700, 20)
        self.manYN = rd.randrange(20, 460, 20)

        self.manza.update(self.manXN, self.manYN, 20, 20)


    def dibujar(self):
        self.pantalla.fill((65, 207, 65))


        for i in self.jugador:
            if self.jugador[0] == i:
                pg.draw.ellipse(
                    self.pantalla,
                    (179, 169, 97),
                    (i.x, i.y, 20, 20)
                )

            else:
                pg.draw.rect(
                    self.pantalla,
                    (179, 169, 97),
                    (i.x, i.y, 20, 20)
                )

        for i in self.paredes:
            pg.draw.rect(
                self.pantalla,
                (70, 89, 70),
                i
            )

        pg.draw.rect(self.pantalla, "red", self.manza)

        if not self.iniciado:
            self.pantalla.blit(self.text1, (100, 90))
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
                self.text2 = self.fuente2.render(f"La cantidad de basura comida es: {self.cantBas}", True, "black" )
                self.NewManza()

        return False
