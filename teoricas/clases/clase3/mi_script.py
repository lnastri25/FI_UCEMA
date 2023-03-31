#!/bin/python3

import os # me permite mover y dialogar archivos con el sistema operativo
import sys # me permite tomar parametros desde la terminal


usuario = sys.argv[1] # el primer parámetro se corresponde con la posición 1,
                      # dado que la posición 0 contiene al nombre del script
                      # sys.arg toma los argumentos que le pasamos al script por consola
                      # [1] significa que siempre voy a tomar el primero
                      # es decir leo solo la primer palabra que escriben en la terminal

def saludador(nombre):
   return "Hola " + nombre

if __name__ == "__main__":
    print(saludador(usuario))
