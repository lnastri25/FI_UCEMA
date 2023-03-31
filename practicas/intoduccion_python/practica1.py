#!/bin/python3

"https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/Python_intro/Practicas/Pr%C3%A1ctica_de_introducci%C3%B3n_a_Python_Parte1.md"

## GUÍA 1: PRÁCTICA  DE INTRODUCCIÓN A PYTHON - PARTE 1 ## 

# Ejercicio 1 # 
# Escribir funciones que permitan obtener el anterior y el siguiente de un número.

def anterior(numero):
    return numero - 1

def siguiente(numero):
    return numero + 1

# Ejercicio 2 #
# Escribir una función que obtenga el doble de un número.

def doble(numero):
    return numero * 2 

# Ejercicio 3 #
# Escribir funciones que obtengan el doble del anterior y el doble del siguiente de un número.

def doble_del_anterior(numero):
    return (doble(anterior(numero))) 

def doble_del_siguiente(numero):
    return (doble(siguiente(numero))) 

# Ejercicio 4 # 
# Escribir una función llamada retirar_dinero, que tenga como parámetros el saldo y el monto a retirar y que devuelva cuánto saldo queda luego de la extracción. 
# Si retira más dinero que lo que tiene en el saldo debe devolver 0 (no se puede usar if).

def retirar_dinero(saldo, monto):
    return max(saldo-monto, 0)

# Ejercicio 5 #
# Escribir una función llamada dia_de_la_semana_favorito que tome como parámetro un día de la semana y devuelve True si el día es "Sábado" 
# o False si es cualquier otro (no se puede usar if).

def dia_de_la_semana_favorito(dia):
    return dia == "Sábado" or dia == "sábado" 

# Ejercicio 6 #
# Escribir una función que determine si una longitud de onda de una radio está dentro o fuera del rango de recepción de una antena. 
# La longitud de onda mínima que recibe la antena es 223.0 y la máxima es 586.8 (no se puede usar if).

def dentro_del_rango(longitud_onda):
    return longitud_onda >= min(223.0, 586.8) and longitud_onda <= max(223.0, 586.8)

# Ejercicio 7 #
# Reescribir la función del punto anterior considerando, además, 
# que la longitud de onda no puede ser 314.5 porque ya está ocupada por otra radio (no se puede usar if).

def dentro_del_rango(longitud_onda):
    return (longitud_onda >= min(223.0, 586.8) and longitud_onda <= max(223.0, 586.8)) and not longitud_onda == 314.5

# Ejercicio 8 #
# Escribir una función llamada tiene_descuento que tome como parámetro una edad y devuelva True en caso de que la edad sea menor o igual a 12 o mayor o igual a 60. 
# En caso contrario tiene que devolver False (no se puede usar if).

def tiene_descuento(edad):
    return edad <= 12 or edad >= 60

# NO HAY Ejercicio 9 #

# Ejercicio 10 #
# Escribir una función que reciba un nombre y un apellido y devuelva un saludo de bienvenida para esa persona.

def bienvenida(nombre, apellido):
    return "Bienvenido a la Universidad del CEMA" + " " + nombre + " " + apellido

# Ejercicio 11 #
# Escribir una función que tome como parámetro un string y que, si empieza con la letra "H", nos devuelva la longitud del string.

def empieza_con_H(palabra):
    if palabra[0] == "H":
        return len(palabra)
    else: 
        "La palabra no empieza con H"

# Ejercicio 12 #
# Escribir una función que reciba como parámetro un string y nos diga si el string empieza con "Buenos" o "Buenas".

def empieza_con_buenos(palabra):
    return palabra.startswith("Buenas") or palabra.startswith("Buenos")

# Ejercicio 13 #
# Escribir una función llamada es_multiplo que reciba dos números y diga si el segundo es múltiplo del primero

def es_multiplo(numero1, numero2):
    return numero2 % numero1 == 0

# Ejercicio 14 #
# Escribir una función que nos diga si un número es par, impar o cero.

def par_impar_cero(numero):
    if numero == 0:
        return "es cero"
    elif numero % 2 == 0:
        return "es par"
    else:
        return "es impar"

# Ejercicio 15 #
# Escribir una función que tome como parámetro una frase y nos diga cuántas "a" (o "A") hay en la frase, utilizando for.

def contar_las_a(frase):
    conteo = 0
    for letra in frase:
        if letra == 'a' or letra == 'A':
            conteo += 1
    return conteo

# Ejercicio 16 #
# Escribir una función que tome como valor una cantidad de dinero y nos diga por cuántos meses podemos subsistir con ese dinero,
# tomando en cuenta que se gastan 60000 pesos por mes.

def meses_de_subsistencia(dinero):
    meses = dinero / 60000
    return int(meses)