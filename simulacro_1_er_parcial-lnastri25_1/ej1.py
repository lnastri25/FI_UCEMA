#!/bin/python3

import re

# Obtener la lista de subsecuencias delimitadas por 'X' e 'Y', que incluyan la subsecuencia 'ab'. Por ejemplo para XbaaaYjXababYqbabbbaaYqXffeeY, hay que devolver ['abab', 'babbbaa'].


def obtener_subsecuencias(string):
    coincidencias = re.findall('X(.*?)Y', string) 
    resultado = []
    for coincidencia in coincidencias:
        if 'ab' in coincidencia:
            resultado.append(re.findall('(ab.*?)($|X|Y)', coincidencia)[0][0])
    return resultado

print(obtener_subsecuencias("XbaaaYjXababYqbabbbaaYqXffeeY"))


# Onomatopopih esta aprendiendo expresiones regulares y le pidieron construir una función que sea capaz de extraer la lista de substrings delimitadas por patrones 'ag' y 'cta' y no incluyan números. Revisa su código propuesto y marca con una x las opciones correctas. JUSTIFICA tus respuestas

def funcionDeExpresiones_Regulares(string):
    return re.findall('ag(\D.*?)cta',string)

print(funcionDeExpresiones_Regulares('aabocaggaaactazu4lggaasag24gra1ndecta'))

# A) El nombre de la función de Onomatopopih respeta las convenciones de nombres de Python. --> FALSO. No hay error de código, solamente que en Python se suele usar snake case.

# B) La función lanza NameError al ser ejecutada. --> FALSO. Ocurre cuando tratas de usar una variable o una funcion que no fue definida previamente.

# C) La función lanza SyntaxError al ser ejecutada. --> FALSO. Ocurre cuando el intérprete se encuentra con un error de sintaxis en el codigo.

# D) Una vez corregida la función, cuando se la invoca usando el texto 'aabocaaggaaactazu4lgaaasad24gra1ndecta' devuelve ['gaaa'] --> VERDADERO. Cumple con lo que se pide en la consigna. La modificación '\D' hace referencia a la no incluision de caracteres numericos.

# E) Una vez corregida la función, cuando se la invoca usando el texto 'aabocaaggaaaactazu4lgaaasad24gra1ndecta' devuelve ['23gra1nde'] --> FALSO. No cumplió lo que se pidió en el enunciado. Retorna lo que está entre 'ag' y 'cta' sin incluirlos, pero devuelve números también y en el enunciado pide que no se incluyan esos números.
