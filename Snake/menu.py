import pygame as pg

class Menu():
    def __init__(self):
        self.fuente = pg.font.Font(None, 40)
        self.fuente1 = pg.font.Font("C:/Windows/Fonts/seguiemj.ttf", 90)
        self.fuente2 = pg.font.Font(None, 60)
        self.texto0 = self.fuente2.render("EcoSerpiente", True, (168, 217, 108))
        self.texto1 = self.fuente.render("Play", True, (0, 176, 0))
        self.texto2 = self.fuente.render("Opciones", True, "white")
        self.texto3 = self.fuente.render("Exit", True, (0, 176, 0))
        self.texto4 = self.fuente2.render("Selecciona la dificultad", True, "white")
        self.texto5 = self.fuente.render("Facil", True, (0, 176, 0))
        self.texto6 = self.fuente.render("Normal", True, (0, 176, 0))
        self.texto7 = self.fuente.render("Dificil", True, (0, 176, 0))
        self.texto8 = self.fuente.render("Caracteristicas: Velocidad lenta, Mapa pequeño", True, "white")
        self.texto9 = self.fuente.render("Caracteristicas: +Velocidad, Mapa mediano", True, "white")
        self.textoa = self.fuente.render("Caracteristicas: ++Velocidad, Mapa grande", True, "white")
        self.textob = self.fuente1.render("🐍", True, "black")

        self.bot1 = pg.Rect(235, 180, 250, 60)
        self.bot2 = pg.Rect(235, 220, 250, 60)
        self.bot3 = pg.Rect(235, 280, 250, 60)
        self.bot4 = pg.Rect(100, 90, 250, 60)
        self.bot5 = pg.Rect(400, 90, 250, 60)
        self.bot6 = pg.Rect(235, 210, 250, 60)

    def dibujar(self, pantalla):
        pantalla.fill((24, 43, 39))


        for x in range(0, (pantalla.get_width()), 20):
            pg.draw.line(pantalla, (34, 57, 49), (x, 0), (x, (pantalla.get_height())))

        for y in range(0, (pantalla.get_height()), 20):
            pg.draw.line(pantalla, (34, 57, 49), (0, y), ((pantalla.get_width()), y))

        pg.draw.rect(pantalla, (168, 217, 108), self.bot1)
        pg.draw.rect(pantalla, (168, 217, 108), self.bot3)

        pantalla.blit(self.texto0, (220, 20))
        pantalla.blit(self.texto1, (330, 200))
        pantalla.blit(self.texto3, (330, 300))
        pantalla.blit(self.textob, (310, 65))

    def selDif(self, pantalla):
        pantalla.fill((24, 43, 39))


        for x in range(0, (pantalla.get_width()), 20):
            pg.draw.line(pantalla, (34, 57, 49), (x, 0), (x, pantalla.get_height()))

        for y in range(0, (pantalla.get_height()), 20):
            pg.draw.line(pantalla, (34, 57, 49), (0, y), ((pantalla.get_width()), y))       

        pg.draw.rect(pantalla, (168, 217, 108), self.bot4)
        pg.draw.rect(pantalla, (168, 217, 108), self.bot5)
        pg.draw.rect(pantalla, (168, 217, 108), self.bot6)  

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
        if self.bot3.collidepoint(self.posmouse):
            return "exit"
        return None
