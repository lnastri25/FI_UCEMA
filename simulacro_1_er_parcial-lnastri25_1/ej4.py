#!/bin/python3

# A) Vamos a modelar de manera muy simple la mecánica de un nuevo juego de Pac-Man con algunas modificaciones al original. Consideremos tanto los puntos que obtiene comiendo bolitas como los puntos que obtiene al comerse a los fantasmas, sin embargo en este nuevo juego cada fantasma otorga distinta cantidad de puntos, siendo el rosa el que mayor puntaje da (8 puntos), seguido del verde (6), el naranja (4) y el rojo (2). Además mientras más puntos tiene, más rápido se va a mover (aumenta su velocidad tantas veces como puntaje otorga la bolita).

# Como en todo juego de Pac-Man, si lo toca un fantasma se pierde una vida y si se queda sin vidas se termina el juego, se lo informa y ya no se puede seguir jugando; inicialmente Pac-Man tiene 3 vidas. Considerá que también habrá fantasmas aterradores que le quitarán dos vidas.

# Modelar las clases y mensajes necesarios para resolver esta situación.

class PacMan:
    def __init__(self):
        self.vidas = 3
        self.puntos = 0
        self.velocidad = 1

    def comer_bolitas(self,bolitas):
        self.puntos += bolitas
        self.velocidad +=bolitas
    
    def comer_fantasmas(self,fantasma):
        self.puntos += fantasma.morir() 
        self.velocidad += fantasma.morir() 

    def me_toco_un_fantasma(self,fantasma):
        if self.esta_vivo():
            self.vidas -= fantasma.quitar_vida()
        else:
            raise Exception ("Tu Pacman ha Muerto!")

    def esta_vivo(self):
        return self.vidas < 0

    def nuevas_habilidades(self):
        if self.puntos > 200: 
            self.vidas += 1
        else: pass
        

class Fantasmas:
    def __init__(self,puntos):
        self.puntos = puntos

    def morir(self):
        return self.puntos

    def quitar_vida(self):
        return 1

class FantasmasAterradores(Fantasmas):
    def quitar_vida(self):
        return 2


pacquito = PacMan()

fantasma_rosa = Fantasmas(8)
fantasma_verde = Fantasmas(6)
fantasma_naranja = Fantasmas(4)
fantasma_rojo = Fantasmas(2)
fantasma_multicolor = FantasmasAterradores(10)



print(pacquito.esta_vivo)
print(pacquito.vidas)
pacquito.me_toco_un_fantasma(fantasma_multicolor)
pacquito.me_toco_un_fantasma(fantasma_rosa)
print(pacquito.vivo)
print(pacquito.vidas)
pacquito.me_toco_un_fantasma(fantasma_rosa)
print(pacquito.vidas)

print(pacquito.esta_vivo)

# B) A medida que avanza el juego Pac-Man obtiene nuevas habilidades: sí llega a 200 puntos, gana una vida extra. Además, ahora gana más velocidad a medida que suma puntos de la forma: cada punto extra le da un 1% más de velocidad.