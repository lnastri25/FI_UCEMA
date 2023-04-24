#!/bin/python3

# A) Vamos a modelar de manera muy simple la mecánica de un nuevo juego de Pac-Man con algunas modificaciones al original. Consideremos tanto los puntos que obtiene comiendo bolitas como los puntos que obtiene al comerse a los fantasmas, sin embargo en este nuevo juego cada fantasma otorga distinta cantidad de puntos, siendo el rosa el que mayor puntaje da (8 puntos), seguido del verde (6), el naranja (4) y el rojo (2). Además mientras más puntos tiene, más rápido se va a mover (aumenta su velocidad tantas veces como puntaje otorga la bolita).

# Como en todo juego de Pac-Man, si lo toca un fantasma se pierde una vida y si se queda sin vidas se termina el juego, se lo informa y ya no se puede seguir jugando; inicialmente Pac-Man tiene 3 vidas. Considerá que también habrá fantasmas aterradores que le quitarán dos vidas.

# Modelar las clases y mensajes necesarios para resolver esta situación.

# B) A medida que avanza el juego Pac-Man obtiene nuevas habilidades: sí llega a 200 puntos, gana una vida extra. Además, ahora gana más velocidad a medida que suma puntos de la forma: cada punto extra le da un 1% más de velocidad.

class PacMan:
    def __init__(self, vidas=3, velocidad=1):
        self.vidas = vidas
        self.velocidad = velocidad

    def comer_bolita(self, bolita):
        self.velocidad += bolita.puntaje * 0.01

    def comer_fantasma(self, fantasma):
        self.vidas -= fantasma.puntaje // 2

class Bolita:
    def __init__(self, puntaje):
        self.puntaje = puntaje
    
class Fantasma:
    def __init__(self, puntaje):
        self.puntaje = puntaje
    
class FantasmaRojo(Fantasma):
    def __init__(self):
        super().__init__(puntaje=2)
    
class FantasmaNaranja(Fantasma):
    def __init__(self):
        super().__init__(puntaje=4)
    
class FantasmaVerde(Fantasma):
    def __init__(self):
        super().__init__(puntaje=6)
    
class FantasmaRosa(Fantasma):
    def __init__(self):
        super().__init__(puntaje=8)

class FantasmaAterrador(Fantasma):
    def __init__(self):
        super().__init__(puntaje=0)
    
    def comer_fantasma(self, fantasma):
        fantasma.puntaje = 0
    
    def comer_pacman(self, pacman):
        pacman.vidas -= 2


