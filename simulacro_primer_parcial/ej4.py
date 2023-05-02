#!/bin/python3

# A) Vamos a modelar de manera muy simple la mecánica de un nuevo juego de Pac-Man con algunas modificaciones al original. Consideremos tanto los puntos que obtiene comiendo bolitas como los puntos que obtiene al comerse a los fantasmas, sin embargo en este nuevo juego cada fantasma otorga distinta cantidad de puntos, siendo el rosa el que mayor puntaje da (8 puntos), seguido del verde (6), el naranja (4) y el rojo (2). Además mientras más puntos tiene, más rápido se va a mover (aumenta su velocidad tantas veces como puntaje otorga la bolita).

# Como en todo juego de Pac-Man, si lo toca un fantasma se pierde una vida y si se queda sin vidas se termina el juego, se lo informa y ya no se puede seguir jugando; inicialmente Pac-Man tiene 3 vidas. Considerá que también habrá fantasmas aterradores que le quitarán dos vidas.

# Modelar las clases y mensajes necesarios para resolver esta situación.

"""
Modificación de enunciado:

- come_bolitas --> doble cantidad
- come_fantasma --> rosa = 8; verde = 6, naranja = 4; rojo = 2
- velocidad --> (2xpuntos)/100
- perder_vida --> contador - 1 (reseteo puntos)
              --> -3 vidas --> "Game Over"
"""


# PRIMERA OPCIÓN DE RESOLUCIÓN

class PacMan:
    def __init__(self):
        self.vidas = 3
        self.puntos = 0
        # velocidad opcional

    def comerBolita(self, cantidad):
        self.puntos += (cantidad * 2)

    def velocidad(self):
        return self.puntos 
    
    def perderVida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print ("GAME OVER")

    def comerFantasma(self, fantasma):
        if fantasma == "rosa":
            self.puntos += 8
        elif fantasma == "verde":
            self.puntos += 6
        elif fantasma == "naranja":
            self.puntos += 4
        elif fantasma == "rojo":
            self.puntos += 2
        else: 
            print ("No es un fantasma")

pacman = PacMan()
print(pacman.puntos)
pacman.comerBolita(10)
print(pacman.puntos)
pacman.comerFantasma("rojo")
print(pacman.puntos)
pacman.comerFantasma("verde")
print(pacman.puntos)


# SEGUNDA OPCIÓN DE RESOLUCIÓN

class PacMan:

    def __init__(self):
        self.vidas = 3
        self.puntos = 0
        
    def comerBolita(self, cantidad):
        self.puntos += (cantidad * 2)

    def velocidad(self):
        return self.puntos 
    
    def perderVida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print ("GAME OVER")
    
    def comerFantasma(self, fantasma, color):
        self.puntos += fantasma.puntos_color(color)

class Fantasma:
    def __init__(self):
        self.fantasmas = {"rosa": 8, "verde": 6, "naranja": 4, "rojo": 2}
    
    def puntos_color(self, color):
        return self.fantasmas[color]
    
pacman = PacMan()


# TERCERA OPCIÓN DE RESOLUCIÓN

class PacMan:
    def __init__(self):
        self.vidas = 3
        self.puntos = 0
        # velocidad opcional

    def comerBolita(self, cantidad):
        self.puntos += (cantidad * 2)

    def velocidad(self):
        return self.puntos 
    
    def perderVida(self):
        self.puntos = 0
        self.vidas -= 1
        if self.vidas == 0:
            print ("GAME OVER")

    def comerFantasma(self, fantasma, color):
        fantasma.set_color(color)
        self.puntos += fantasma.puntos_color(color)

class Fantasma:
    def __init__(self):
        self.color = None

    def set_color(self, color):
        self.color = color
    
    def puntos_color(self, color):
        return self.color.puntos()

class Rojo:
    def puntos(self):
        return 2

class Naranja:
    def puntos(self):
        return 4

class Verde:
    def puntos(self):
        return 6

class Rosa:
    def puntos(self):
        return 8

pacman = PacMan()
rojo = Rojo()
rosa = Rosa()
naranja = Naranja()
verde = Verde()
fantasma = Fantasma()

print(pacman.puntos)
pacman.comerBolita(10)
print(pacman.puntos)
pacman.comerFantasma(fantasma, rojo)
print(pacman.puntos)
pacman.comerFantasma(fantasma, verde)
print(pacman.puntos)

# B) A medida que avanza el juego Pac-Man obtiene nuevas habilidades: sí llega a 200 puntos, gana una vida extra. Además, ahora gana más velocidad a medida que suma puntos de la forma: cada punto extra le da un 1% más de velocidad.

class PacManMejorado(PacMan):
    def vidaExtra(self):
        if self.puntos >= 200:
            self.vidas += 1
            self.puntos -= 200
        else:
            print("Faltan", 200 - self.puntos, "puntos para ganar una vida extra")
    
    def velocidad(self):
        return 3 + self.puntos / 100