#!/bin/python3

"https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/Python_intro/Practicas/Pr%C3%A1ctica_de_introducci%C3%B3n_a_Python_Parte1.md"

# Ejercicio 1 # 
def anterior(numero):
    return numero - 1

def siguiente(numero):
    return numero + 1

# Ejercicio 2 #
def doble(numero):
    return numero * 2 

# Ejercicio 3 #
def doble_del_anterior(numero):
    return (doble(anterior(numero))) 

def doble_del_siguiente(numero):
    return (doble(siguiente(numero))) 

# Ejercicio 4 # 
def retirar_dinero(saldo, monto):
    return max(saldo-monto, 0)

# Ejercicio 5 #
def dia_de_la_semana_favorito(dia):
    return dia == "Sábado" or dia == "sábado" 

# Ejercicio 6 #
def dentro_del_rango(longitud_onda):
    return longitud_onda >= min(223.0, 586.8) and longitud_onda <= max(223.0, 586.8)

# Ejercicio 7 #
def dentro_del_rango(longitud_onda):
    return (longitud_onda >= min(223.0, 586.8) and longitud_onda <= max(223.0, 586.8)) and not longitud_onda == 314.5

# Ejercicio 8 #
def tiene_descuento(edad):
    return edad <= 12 or edad >= 60

# NO HAY Ejercicio 9 #

# Ejercicio 10 #
def bienvenida(nombre, apellido):
    return "Bienvenido a la Universidad del CEMA" + " " + nombre + " " + apellido

# Ejercicio 11 #
def empieza_con_H(palabra):
    if palabra[0] == "H":
        return len(palabra)
    else: 
        "La palabra no empieza con H"

# Ejercicio 12 #
def empieza_con_buenos(palabra):
    return palabra.startswith("Buenas") or palabra.startswith("Buenos")

# Ejercicio 13 #
def es_multiplo(numero1, numero2):
    return numero2 % numero1 == 0

# Ejercicio 14 #
def par_impar_cero(numero):
    if numero == 0:
        return "es cero"
    elif numero % 2 == 0:
        return "es par"
    else:
        return "es impar"

# Ejercicio 15 #
def contar_las_a(frase):
    conteo = 0
    for letra in frase:
        if letra == 'a' or letra == 'A':
            conteo += 1
    return conteo

# Ejercicio 16 #
def meses_de_subsistencia(dinero):
    meses = dinero / 60000
    return int(meses)