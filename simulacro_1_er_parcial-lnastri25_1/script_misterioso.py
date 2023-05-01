#!/bin/python3

# A) En la agencia SIDRA (Somos Inteligentes por Demás y Rara vez Alardeamos) tienen agentes secretos diseminados por el mundo. El medio de contacto con los agentes es por correo electrónico, mediante cuentas con identidades falsas. La agencia nos facilitó dos archivos secretos que contienen escondidas las cuentas de los agentes para que los ayudemos a construir un programa que lea los archivos .txt y extraiga todas las cuentas de gmail de los agentes secretos y las almacene en un único archivo base de datos.txt . Usá todo lo que sabes de las bibliotecas os, glob y re

import glob, re

def filtrar(archivo):
    lista_txt = glob.glob("*txt")

    with open(archivo, "a") as miarch1:
        for archivo in lista_txt:
            with open(archivo, "r") as archivo_secreto:
                texto = archivo_secreto.read()
                lista = re.findall("[\W]+[-_\.]*[\W]+@gmail.com", texto)
                for email in lista:
                    miarch1.write(email + "\n")

""""
gmail = r"\b[A-Za-z0-9._%+-]+@[gmail]+\.[A-Za-z]{2,}\b"

archivos_txt = glob.iglob("**/*.txt", recursive=True)

# Abre el archivo de base de datos en modo de escritura
with open("base_de_datos.txt", "w") as mi_arch1:
    # Recorre cada archivo .txt encontrado
    for ruta_archivo in archivos_txt:
        # Lee el contenido del archivo
        with open(ruta_archivo, "r") as mi_arch2:
            contenido = mi_arch2.read()
        # Busca todos los correos electrónicos en el contenido usando la expresión regular
        gmails = re.findall(gmail, contenido)
        # Escribe los correos electrónicos encontrados en el archivo de base de datos
        for gmail in gmails:
            mi_arch1.write(gmail + "\n")
"""

# El punto B no se resuelve.