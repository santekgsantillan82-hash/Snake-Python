import pygame as pg

class Menu():
    def __init__(self):
        self.fuente = pg.font.Font(None, 40)
        self.texto1 = self.fuente.render("Play", True, "white")
        self.texto2 = self.fuente.render("Opciones", True, "white")
        self.texto3 = self.fuente.render("Exit", True, "white")

        self.bot1 = pg.Rect(235, 70, 250, 60)
        self.bot2 = pg.Rect(235, 220, 250, 60)
        self.bot3 = pg.Rect(235, 370, 250, 60)

    def dibujar(self, pantalla):
        pantalla.fill("white")

        pg.draw.rect(pantalla, (0, 170, 228), self.bot1)
        pg.draw.rect(pantalla, (0, 170, 228), self.bot2)
        pg.draw.rect(pantalla, (0, 170, 228), self.bot3)

        pantalla.blit(self.texto1, (330, 90))
        pantalla.blit(self.texto2, (300, 240))
        pantalla.blit(self.texto3, (330, 385))

    def actualizar(self):
        posmouse = pg.mouse.get_pos()
        mouseEstado = pg.mouse.get_pressed()

        if self.bot1.collidepoint(posmouse):
            if mouseEstado[0]:
                return "play"

        return None
