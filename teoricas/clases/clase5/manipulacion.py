# Escribir un script en el cual debemos movernos a la carpeta Informes y obtener los archivos *.txt que hayan allí. 
# Por cada archivo hay que obtener, por un lado, cuántas veces aparece la palabra "estado" y por otro lado la cantidad de líneas. 
# Por último, hay que crear una carpeta que se llame Apellidos, donde hay que crear un archivo llamado Lista.txt que 
# contenga en cada línea la primer línea de cada archivo .txt obtenidos anteriormente.

#!/bin/python3

import os, glob, sys

def ejercicio_rutas():
    os.chdir("Informes")
    txt = glob.glob("*.txt") # Lo guardo en una variable para poder tener la lista después
    cantidad_estado = []
    cantidad_lineas = []
    for archivo in txt:
        with open(archivo, "r") as file:
            file_completa = file.read() 
            cantidad_estado.append(file_completa.count("estado"))
            cantidad_lineas.append(file_completa.count("\n"))

    os.mkdir("Apellidos")
    with open("Apellidos/Lista.txt", "w") as salida:
        for archivo in txt:
            with open(archivo, "r") as file:
                # primera_linea = file.readline()
                # salida.write(primer_linea)
                salida.write(file.readline())
    return cantidad_estado, cantidad_lineas

c1, c2 = ejercicio_rutas()