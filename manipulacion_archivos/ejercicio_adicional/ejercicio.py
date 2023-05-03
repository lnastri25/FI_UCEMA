#!/bin/python3

# Definir un procedimiento que lea los archivos .txt que están en la carpeta Marzo, y copie la primera línea de cada uno en un archivo dentro de la carpeta resultados (que debe estar dentro de new).

"""
Pasos:
1) Nos movemos a Marzo
2) Extramos los archivos .txt
3) Leemos las primeras líneas
4) Hacemos carpeta de salida ('Resultado')
5) Hacer archivo
6) Poner las líneas en el archivo nuevo
"""
import os, glob, sys

def primeras_lineas(path_a_txt, path_resultado, salida):
    os.chdir(path_a_txt)
    textos = glob.glob("*txt")
    primer_linea = []
    for txt in textos:
        with open(txt, "r") as texto:
            primer_linea.append(texto.readline())

    os.chdir("../../")
    os.mkdir(path_resultado)
    os.chdir(path_resultado)
    with open(salida, "a") as final_txt:
        for linea in primer_linea:
            final_txt.write(linea)

primeras_lineas("datos/marzo", "resultado", "salida.txt")
