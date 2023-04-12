#!/bin/python3

"https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/Python_intro/Practicas/Pr%C3%A1ctica_Expresiones_regulares.md"

## GUÍA 4: EXPRESIONES REGULARES ## 

import re

# Ejercicio 1 #
# Escribí una funcion que verifique si un string tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9.

def caracteres_permitidos(string):
    return bool(re.search("[a-zA-Z0-9]",string)) # Ponemos 'return bool' porque sino devuelve "None" por default.

print(caracteres_permitidos("ABCDEaaa1234"))

# Ejercicio 2 #
# Escribí un programa que verifique si un string tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9.

def caracteres_permitidos(string):
    return not bool(re.search("[^a-zA-Z0-9.9]",string)) # Ponemos 'return not bool' para que devuelva lo contrario. 'True' --> 'False'
                                                        # ^ : Me da true cuando tengo los caracteres permitidos, entonces lo que hago es negar esos resultados.

print(caracteres_permitidos("ABCDEaaa1234"))

# Ejercicio 3 #
# Creá un programa que verifique las siguientes condiciones:

# si un string dado tiene una h seguida de ninguna o más e.

def encontrar_patron(string):
    patron = "he*" # Que sea una 'h' seguida de una 'e' y eso (la letra 'e') puede estar cero o más veces.
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"
    
print(encontrar_patron("a"))
print(encontrar_patron("h"))
print(encontrar_patron("he"))
print(encontrar_patron("heeeeee"))

# si un string dado tiene una h seguida de una o más e.

def encontrar_patron(string):
    patron = "he+" # Que sea una 'h' seguida de una 'e' y eso (la letra 'e') tiene que estar sí o sí una vez.
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"
    
print(encontrar_patron("a")) # No se va a encontrar el patrón porque estoy buscando una h que tenga 1 'e' o más.
print(encontrar_patron("h")) # No se va a encontrar el patrón porque estoy buscando una h que tenga 1 'e' o más.
print(encontrar_patron("he"))
print(encontrar_patron("heeeeee"))

# si un string dado tiene una h seguida de una o más e.

def encontrar_patron(string):
    patron = "he?" # Que sea una 'h' seguida de una 'e' y ahi (la letra 'e') se va a ver si tiene 0 o 1 'e' y después lo que sea (por eso el último ejemplo va a cumplir con la donción).
                    # Si ponemos "he?^e" solamente van a cumplir el 2do ejemplo "h" y el 3ero "he".
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"
    
print(encontrar_patron("a"))
print(encontrar_patron("h")) 
print(encontrar_patron("he"))
print(encontrar_patron("heeeeee"))

# si un string dado tiene una h seguida de dos o tres e.

def encontrar_patron(string):
    patron = "he{2,3}" # Que sea una 'h' seguida de una 'e' y eso (la letra 'e') va a estar entre 2 y 3 veces.
    if re.search(patron, string) is not None:
        return "Se encontró el patrón"
    else:
        return "No se encontró el patrón"
    
print(encontrar_patron("he")) 
print(encontrar_patron("hheeeeey")) # Va a encontrarlo porque Python lo que está después no lo ve. 
                                    # Si nosotros queremos que después no haya más lo tenemos que aclarar.

# Ejercicio 4 #
# Realizá un programa que encuentre una palabra unida a otra con un guión bajo en un string dado (el string no debe contener espacios).

def palabras_unidas(string):
    patron = "^[a-z]+_[a-z]+$" # ^: inicio de línea // $: fin de línea.
    if re.search(patron, string) is not None:
        return "Patrón encontrado"
    else:
        return "Patrón no encontrado"
    
# Ejercicio 5 #
# Escribí un programa que diga si un string empieza con un número específico.

# Ejercicio 6 #
# Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

# Ejercicio 7 #
# Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

def revisar_texto(string):
    patron = "^[a-zA-Z0-9\s]*$"
    if re.search(patron, string) is not None:
        return "El string cumple las condiciones"
    else:
        return "El string no cumple las condiciones"
    
print(revisar_texto("La perra corre por todo el parque a la tarde 123"))

# Ejercicio 8 #
# Escribí un programa que separe y devuelva los caracteres númericos de un string.

def extraer_numeros(string):
    resultado = re.split("\D+", string) # Podes usar + o * porque buscamos un caracter que no sea numérico 1 o más veces, 
                                        # entonces cada vez que encuentra algo, se fija si esta 1 o más veces.
    for elemento in resultado:
        print(elemento)

string = "Hoy movimos 10 cajas de lugar, en 3 edificios distintos para llevar a 12 casas"

extraer_numeros(string)

# Ejercicio 9 #
# Escribí un programa que extraiga los caracteres que estén entre guiones en un string.

def entre_guiones(string):
    return re.findall(r"-(.*?)-", string) # r: raw string // ? (después de un modificador): favorece los matches internos // .*: cualquier caracter 0 o más veces // ?: no guarda el grupo //

string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"

print(entre_guiones(string))

# Ejercicio 10 #
# Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres @ o &.

def get_substr(string):
    return re.findall("[@|&](.*?)[@|&]", string)

string = "sdaf@dsfa&fasdf& sdf @    dsf dfds@sdaf@sdfasd ewr"

lista_substr = get_substr("sdaf@dsfa&fasdf& sdf @    dsf dfds@sdaf@sdfasd ewr")

resultado = {}

# Ejercicio 11 #
# Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima.

def dos_P(lista):
    for elemento in lista:
        resultado = re.match("(P\w*)\W(P\w*)", elemento)
        if resultado is not None:
            print(resultado.group())

lista = ["Práctica Python", "Práctica C++", "Práctica Fortran"]
dos_P(lista)

# Ejercicio 12 #
# Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (|).

# Ejercicio 13 #
# Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

# Ejercicio 14 #
# Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.

# Ejercicio 15 #
# Realizá un programa que validar si una cuenta de mail está escrita correctamente.