import pygame as pg

class Menu():
    def __init__(self):
        self.fuente = pg.font.Font(None, 40)
        self.fuente2 = pg.font.Font(None, 60)
        self.texto0 = self.fuente2.render("EcoSerpiente", True, "black")
        self.texto1 = self.fuente.render("Play", True, "white")
        self.texto2 = self.fuente.render("Opciones", True, "white")
        self.texto3 = self.fuente.render("Exit", True, "white")
        self.texto4 = self.fuente2.render("Selecciona la dificultad", True, "Black")
        self.texto5 = self.fuente.render("Facil", True, "white")
        self.texto6 = self.fuente.render("Normal", True, "white")
        self.texto7 = self.fuente.render("Dificil", True, "white")
        self.texto8 = self.fuente.render("Caracteristicas: Velocidad lenta, Mapa pequeño", True, "black")
        self.texto9 = self.fuente.render("Caracteristicas: +Velocidad, Mapa mediano", True, "black")
        self.textoa = self.fuente.render("Caracteristicas: ++Velocidad, Mapa grande", True, "black")

        self.bot1 = pg.Rect(235, 70, 250, 60)
        self.bot2 = pg.Rect(235, 220, 250, 60)
        self.bot3 = pg.Rect(235, 370, 250, 60)
        self.bot4 = pg.Rect(100, 90, 250, 60)
        self.bot5 = pg.Rect(400, 90, 250, 60)
        self.bot6 = pg.Rect(235, 210, 250, 60)

    def dibujar(self, pantalla):
        pantalla.fill("white")

        pg.draw.rect(pantalla, (0, 170, 228), self.bot1)
        pg.draw.rect(pantalla, (0, 170, 228), self.bot2)
        pg.draw.rect(pantalla, (0, 170, 228), self.bot3)

        pantalla.blit(self.texto0, (220, 20))
        pantalla.blit(self.texto1, (330, 90))
        pantalla.blit(self.texto2, (300, 240))
        pantalla.blit(self.texto3, (330, 385))

    def selDif(self, pantalla):
        pantalla.fill("white")

        pg.draw.rect(pantalla, (0, 170, 228), self.bot4)
        pg.draw.rect(pantalla, (0, 170, 228), self.bot5)
        pg.draw.rect(pantalla, (0, 170, 228), self.bot6)  

        pantalla.blit(self.texto4, (145, 40))
        pantalla.blit(self.texto5, (200, 109))
        pantalla.blit(self.texto6, (480, 108))
        pantalla.blit(self.texto7, (320, 228))      

        if self.bot4.collidepoint(self.posmouse):
            pantalla.blit(self.texto8, (50, 150))
        if self.bot5.collidepoint(self.posmouse):
            pantalla.blit(self.texto9, (80, 150))
        if self.bot6.collidepoint(self.posmouse):
            pantalla.blit(self.textoa, (80, 288))

    def actualizar(self, click):
        self.posmouse = pg.mouse.get_pos()

        if not click:
            return None
        if self.bot1.collidepoint(self.posmouse):
            return "play"
        if self.bot4.collidepoint(self.posmouse):
            return "fac"
        if self.bot5.collidepoint(self.posmouse):
            return "nor"
        if self.bot6.collidepoint(self.posmouse):
            return "dif"
        return None
