#!/bin/python3

# Armar un script que lea el archivo "un_archivo.txt" y cree otro archivo "nuevo_arch.txt" con
# los 5 primeros caracteres del archivo que leímos


"""

Opción 1

"""
# with open("un_archivo.txt", "r") as mi_arch:
 #   with open("nuevo_archivo.txt", "a") as nuevo:
  #     nuevo.write(mi_arch.readline(5))


"""

Opción 2

"""

texto_leido = open("un_archivo.txt", "r").read()

with open("nuevo_archivo.txt", "a") as mi_arch:
    mi_arch.write(texto_leido[0:6])


