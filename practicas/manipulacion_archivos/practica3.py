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
    file = open(archivo,'r')        #open, read, split
    leer = file.read()
    dividir = leer.split()  # Use split para descomponer el string en palabras; se asume que los delimitadores son espacios de caracteres en blanco.
    print('El archivo tiene', len(dividir), 'palabras')
contar_palabras('tejer.txt')

# Ejercicio 5 #
# Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

def reemplazar(entrada, salida, letra):
    with open(entrada, 'r') as file, open(salida, 'w') as file2:
        for line in file:
            file2.write(line.replace(letra, letra + '\n'))  #Reemplazo y lo escribo en el nuevo archivo
    reemplazar('texto1.txt', 'texto2.txt', 'n')
    
# Ejercicio 6 #
# Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.

def sin_saltos(entrada, salida):
    with open(entrada, 'r') as file, open(salida, 'w') as file2:
        for letra in file.read():
            if letra == '\n':
                pass
            else:
                file2.write(letra)
sin_saltos('texto1.txt', 'texto2.txt')

# Ejercicio 7 #
# Escribí un porgrama que lea un archivo e identifique la palabra más larga, la cual debe imprimir y decir cuantos caracteres tiene.

def palabra_larga(archivo):
    file = open(archivo,'r') # abro
    leer = file.read()       # leo
    dividir = leer.split()   # separa en palabras
    larga = ''               # El espacio es 1 caracter
    for palabra in dividir:
        if len(palabra) > len(larga):
            larga = palabra
    print('La palabra mas larga es', larga, 'con', len(larga), 'letras')

palabra_larga('tejer.txt')

# Ejercicio 8 #
# Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.

def unir_archivos(archivo1, archivo2, archivo3):
    with open(archivo1, 'r') as mi_arch1, open(archivo2, 'r') as mi_arch2, open(archivo3, 'w') as mi_arch3:
        mi_arch3.write(mi_arch1.read() + mi_arch2.read())
unir_archivos('texto1.txt', 'texto2.txt', 'texto3.txt')  

# Ejercicio 9 #
# Realizá un programa que lea un archivo y obtenga la frecuencia de cada palabra que hay en el archivo. 
# Recordá que la frecuencia es la relación entre número de veces que aparece la palabra en cuestión con respecto a la cantidad total de palabras.

def frecuencia_palabras(archivo):
    file = open(archivo,'r') # abro
    leer = file.read()       # leo
    dividir = leer.split()   # separa en palabras
    diccionario = {}
    for palabra in dividir:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    print(diccionario)
frecuencia_palabras('tejer.txt')

# Ejercicio 10 #
# Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, 
# que a su vez se tiene que encontrar dentro de Carpeta1.

def unir_txt(Carpeta1, nombre):
    os.chdir(Carpeta1)               # Cambiamos de directorio a la Carpeta 1
    textos = glob.glob('*.txt')      # Busco todos los txt y armo una lista automatica
    os.mkdir('Resuelto')            # Creo un directorio en la capeta donde estoy
    with open('Resuelto/' + nombre, 'a') as salida: # Tengo que poner resuelto/ para que se dirija hacia alla.
        for archivo in textos:
            with open(archivo, 'r') as texto:
                salida.write(texto.read() + '\n')
unir_txt('Carpeta1', 'archivo2.txt')