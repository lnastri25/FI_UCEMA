#!/bin/python3

import re

# Obtener la lista de subsecuencias delimitadas por 'X' e 'Y', que incluyan la subsecuencia 'ab'. Por ejemplo para XbaaaYjXababYqbabbbaaYqXffeeY, hay que devolver ['abab', 'babbbaa'].

def subsecuencias(string):
    patron = "X(b*ab.*?)Y"
    return re.findall(patron,string)

print(subsecuencias("XbaaaYjXababYqbabbbaaYqXffeeY"))

""""
"X([^XY]*ab[^XY]*)Y" --> Otra manera de hacerlo.
"""

# Onomatopopih esta aprendiendo expresiones regulares y le pidieron construir una función que sea capaz de extraer la lista de substrings delimitadas por patrones 'ag' y 'cta' y no incluyan números. Revisa su código propuesto y marca con una x las opciones correctas. JUSTIFICA tus respuestas

# def funcionDeExpresiones_Regulares():
#   return re.findal('ag(\d.*?)cta')

# print(funcionDeExpresiones_Regulares('aabocaggaaactazu4lggaasag24gra1ndecta'))

# A) El nombre de la función de Onomatopopih respeta las convenciones de nombres de Python. --> FALSO. No hay error de código, solamente que en Python se suele usar snake_case y acá se puede observar que hay una mezcla entre camelCase y snake_case. Además, hace falta pasarle un parámetro a la misma y no tiene un nombre expresivo la misma. De hecho, ya sabemos que es una función porque retorna algo --> entonces no hay que ponerle "funcionede..." --> es super amplio.

# B) La función lanza NameError al ser ejecutada. --> FALSO. Un NameError ocurre cuando tratas de usar una variable o una funcion que no fue definida previamente. El error que ocurre es AtributeError porque findall está mal escrito (re.findal)

# C) La función lanza SyntaxError al ser ejecutada. --> FALSO. Un SyntaxError curre cuando el intérprete se encuentra con un error de sintaxis en el codigo. El error que ocurre es AtributeError porque findall está mal escrito (re.findal)

def delimitacion_de_patrones(string):
    return re.findall("ag(\D*?)cta",string)

print(delimitacion_de_patrones('aabocaggaaactazu4lggaasag24gra1ndecta'))

""""
"ag([^\d]*)cta" --> Otra manera de hacerlo.
"""

# D) Una vez corregida la función, cuando se la invoca usando el texto 'aabocaaggaaactazu4lgaaasad24gra1ndecta' devuelve ['gaaa'] --> VERDADERO. Cumple con lo que se pide en la consigna. La modificación '\ag(\D*?)cta' hace referencia a la no incluision de caracteres numericos.

# E) Una vez corregida la función, cuando se la invoca usando el texto 'aabocaaggaaaactazu4lgaaasad24gra1ndecta' devuelve ['23gra1nde'] --> FALSO. No cumplió lo que se pidió en el enunciado. Retorna lo que está entre 'ag' y 'cta' sin incluirlos, pero devuelve números también y en el enunciado pide que no se incluyan esos números.
