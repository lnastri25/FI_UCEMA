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

def reemplazar(texto):
    return re.sub(r'[\s_:]', '|', texto)

texto = "Este_es un:ejemplo de texto con espacios_ guiones_bajos:y dos:puntos"

texto_reemplazado = reemplazar(texto)

print(texto_reemplazado)

# Ejercicio 13 #
# Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

def reemplazar_dos(string):
    reemplazado = re.sub(r'[\W]','_',string, 2)
    print(reemplazado)
reemplazar_dos('$$Lorenzo')

# Ejercicio 14 #
# Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.

def reemplazar_espacios(string):
    return re.sub(r'[ \t]+', ';', string) # "sub" se utiliza para reemplazar todas las ocurrencias de una expresión regular 
                                          # específica en una cadena de texto con un valor determinado.

texto = "Hola        Lorenzo. ¿Cómo;     estás?"
texto_sin_espacios_tabs = reemplazar_espacios(texto)

print(texto_sin_espacios_tabs)

# [ \t]+: representa uno o más espacios o tabulaciones seguidas. 
# Este patrón se utilizará para encontrar todas las ocurrencias de este tipo de caracteres en la cadena de texto.

# ; : es el valor que se utilizará para reemplazar todas las ocurrencias de la expresión regular en la cadena de texto. 
# En este caso, el valor utilizado es ";", lo que significa que todas las ocurrencias de espacios o tabulaciones en la cadena de texto serán reemplazadas por puntos y comas.

# Ejercicio 15 #
# Realizá un programa que validar si una cuenta de mail está escrita correctamente.

def validar_email(email):
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(patron, email):
        return "El mail está correctamente escrito"
    else:
        return "No está correctamente escrito"

print(validar_email('lorenzonastri@gmail.com'))

def mail_correcto(string):
    return bool(re.search("^\w+[.-]?\w*@[a-z]+[.][a-z]+[.]?[a-z]?$", string))
print(mail_correcto("lorenzo-nastri@gmail.com"))
print(mail_correcto("lorenzo-&nastri@gmail.com"))


# r: significa que cualquier carácter especial contenido en la cadena se interpreta literalmente. (raw string)

# ^: indica el inicio de línea

# [a-zA-Z0-9._%+-]+: representa el nombre del usuario de la dirección de correo electrónico, 
# el cual debe estar conformado por uno o más caracteres alfanuméricos, puntos, guiones bajos, porcentajes, más y guiones.

# @: se utiliza para separar el nombre del usuario de la dirección de correo electrónico del dominio.

# [a-zA-Z0-9.-]+: especifica el dominio del correo electrónico, puede estar conformado por uno o más caracteres alfanuméricos, puntos y guiones.

# \.: indica que debe haber un punto.

# [a-zA-Z]{2,}: especifica la extensión de la dirección de correo electrónico, la cual debe estar conformada por dos o más caracteres alfabéticos.