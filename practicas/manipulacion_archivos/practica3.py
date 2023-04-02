#!/bin/python3

"https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/Python_intro/Practicas/Pr%C3%A1ctica_Manipulaci%C3%B3n_de_archivos.md"

## GUÍA 3: MANIPULACION DE ARCHIVOS ## 

import os, glob

# Ejercicio 1 #
# Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con una determinada letra 
# (por ejemplo que imprima cuántas líneas no empiezan con "P").

def empieza_con(letra, archivo):
    suma = 0
    with open (archivo, "r") as file:
        for line in file:
            if (line[0] != letra.lower() or line[0] != letra.upper()):
                suma += 1
    print ("Hay", suma, "archivos que no empiezan con", letra)

empieza_con('C', "tejer.txt")

# Ejercicio 2 #
# Escribí un programa que lea un archivo e imprima las primeras n líneas.

def leer_imprimir (archivo, primeras_lineas):
    linea = open("tejer.txt", "r").readlines()[: primeras_lineas]
    print(*linea)

leer_imprimir ("tejer.txt", 4)

# Ejercicio 3 # 
# Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

def leer_imprimir_ultimas (archivo, primeras_lineas):
    linea = open("tejer.txt", "r").readlines()[-primeras_lineas:] # Se utiliza para obtener las últimas líneas del archivo de texto
    print(linea) # Sin el asterico la impirme como una lista 

leer_imprimir_ultimas("tejer.txt", 4)

# Ejercicio 4 #
# Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def contar_palabras(archivo):
    file = open(archivo,'r')        #opern, read, split
    leer = file.read()
    dividir = leer.split()  # Use split para descomponer el string en palabras; se asume que los delimitadores son espacios de caracteres en blanco.
    print('El archivo tiene', len(dividir), 'palabras')
contar_palabras('tejer.txt')

# Ejercicio 5 #
# Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

# Ejercicio 6 #
# Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

# Ejercicio 7 #
# Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

# Ejercicio 8 #
# Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

# Ejercicio 9 #
# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

# Ejercicio 10 #
# Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, que a su vez se tiene que encontrar dentro de Carpeta1.