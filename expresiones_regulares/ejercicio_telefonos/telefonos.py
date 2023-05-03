#!bin/python3

import re, os, glob, sys

def encontrar_telefono(texto):

    with open("telefonos.txt", "r") as telefonos:
        tel = telefonos.read()
        lista = encontrar_telefono(tel)
        print(lista)
    patron = "(+5411)([0-9]{8})"
    return re.findall(patron, texto)