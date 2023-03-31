#!/bin/python3

"https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/Python_intro/Practicas/Pr%C3%A1ctica_de_introducci%C3%B3n_a_Python_Parte2.md"

## GUÍA 1: PRÁCTICA  DE INTRODUCCIÓN A PYTHON - PARTE 2 ## 

# Ejercicio 1 # 
# Definir un procedimiento que tome como parámetro una lista, verifique si tiene el elemento "control" y le agregue el string "revisado" y le quite el elemento "control".

def revisar_lista(lista):
    if "control" in lista:
        lista.append("revisado")
        lista.remove("control")

# Ejercicio 2 #
# Definir un procedimiento que tome una lista como parámetro y elimine el primer elemento de la lista. Hacer las verificaciones que sean necesarias.

def eliminacion_primer_elemento(lista):
    lista.pop(0)

# Ejercicio 3 #
# Definir una función que dada una lista y un elemento devuelva la posición de este elemento en la lista.

def posicion_en_lista(lista, elemento):
    if elemento in lista:
        return lista.index(elemento)
    else:
        return "No se ha encontrado el elemento en dicha lista"

# Ejercicio 4 #
# Definir un procedimiento que tome como parámetros dos listas y un elemento, en la que se debe eliminar el elemento de una lista y agregarlo a la otra. 

def eliminacion_agregacion(lista1, lista2, elemento):
    if elemento in lista1:
        lista1.remove(elemento)
        lista2.append(elemento)

# Realizar dos versiones del ejercicio, usando un método distinto para eliminar el elemento en cada versión. ¿Qué problema/s tiene este procedimiento?

# Ejercicio 5 #
# Escribir una función que tome como parámetro una lista de enteros y devuelva una lista con valores booleanos que indique si cada elemento es par o impar. 
# Por ejemplo, para la lista [2, 45, 108, 12, 7], la función debería retornar [True, False, True, True, False]. Utilizar la función realizada en la práctica anterior.

def es_par(numero):
    return numero % 2 == 0

def lista_enteros_booleanos(lista_enteros):
    lista_booleanos = []
    for elemento in lista_enteros:
        lista_booleanos.append(es_par(elemento))
    return lista_booleanos

# Ejercicio 6 #
# Escribir una función que lea un string y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena (considerar que las mayúsculas difieren de las minúsculas, por lo que, si el string es "Agua", el carácter "A" tiene 1 aparición y el carácter "a" también tiene 1).

def recorriendo_el_string(palabra):
    cantidad_de_apariciones = {}
    for letra in palabra:
        if letra in cantidad_de_apariciones:
            cantidad_de_apariciones[letra] += 1
        else:
            cantidad_de_apariciones[letra] = 1
    return cantidad_de_apariciones

# Si el carácter ya está en el diccionario, incrementamos su valor en 1. Si no está, lo agregamos al diccionario con un valor de 1. Al finalizar el bucle, retornamos el diccionario con la cantidad de apariciones de cada carácter.


# Ejercicio 7 #
# Modificá la función anterior para que además imprima los caracteres que no aparecen en la cadena, pero con el valor 0.

def recorriendo_el_string(palabra):
    cantidad_de_apariciones = {}
    for letra in palabra:
        if letra in cantidad_de_apariciones:
            cantidad_de_apariciones[letra] += 1
        else:
            cantidad_de_apariciones[letra] = 1

    for letra in set(palabra):
        if letra not in cantidad_de_apariciones:
            cantidad_de_apariciones[letra] = 0
    return cantidad_de_apariciones

# Ejercicio 8 #
# Definir una función que dada una palabra, nos diga si el palíndromo o no.

def es_palindromo(palabra):
    palabra = palabra.lower()  # Transofrmamos la palabra a minúsculas
    palabra_invertida = palabra[::-1]  # Sacamos la versión invertida de la palabra
    return palabra == palabra_invertida

# Ejercicio 9 #
# Definir una función llamada productoria que toma como parámetro una lista de números y los multiplica a todos.

def productoria(lista):
    resultado = 1
    for numero in lista:
        resultado *= numero
    return resultado

# Ejercicio 10 #
# Creá un programa para gestionar datos de los socios de un club, el cual permita:

# PARTE 1) Cargar la información de los socios en un diccionario, al cual poder acceder por número de socio. Los datos que se deben almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al dia (s/n). El programa debe iniciar con los datos de los socios fundadores ya cargados, los cuales son:

# Socio número 1, Florencia Ocampo, ingresó el 14/09/2001, cuota al día

# Socio número 2, David Estévez, ingresó el 14/09/2001, cuota al día

# Socio número 3, Sofía Cáceres, ingresó el 14/09/2001, cuota al día

# PARTE 2) Informar la cantidad de socios que tiene el club.

# PARTE 3) Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas.

# PARTE 4) Modificar la fecha de ingreso de todos los socios ingresados el 21/10/2017, indicando que en realidad ingresaron el 22/10/2017.

# PARTE 5) Solicitar el nombre y apellido d eun socio y darlo de baja (eliminarlo del listado).

# PARTE 6) Imprimir el listado de socios completos.

# Definir las funciones y/o procedimientos que creas necesarios.


# PARTE 1 
socios = {
    1: {"nombre": "Florencia", "apellido": "Ocampo", "fecha_ingreso": "14092001", "cuota_al_dia": True},
    2: {"nombre": "David", "apellido": "Estévez", "fecha_ingreso": "14092001", "cuota_al_dia": True},
    3: {"nombre": "Sofía", "apellido": "Cáceres", "fecha_ingreso": "14092001", "cuota_al_dia": True}
}

# PARTE 2
def cantidad_socios():
    return len(socios)

# PARTE 3 
def pago_de_cuotas(numero):
    if numero in socios:
        socios[numero]["cuota_al_dia"] = True
        print("Se registró el pago de todas las cuotas del socio número", numero)
    else:
        print("No se encontró un socio con ese número")

# PARTE 4
def corregir_fecha():
    for numero, datos in socios.items():
        if datos["fecha_ingreso"] == "21102017":
            datos["fecha_ingreso"] = "22102017"
            print("Se corrigió la fecha de ingreso del socio número", numero)

# PARTE 5
def dar_de_baja(nombre, apellido):
    encontrado = False
    for numero, datos in socios.items():
        if datos["nombre"] == nombre and datos["apellido"] == apellido:
            del socios[numero]
            encontrado = True
            print("Se dio de baja al socio", nombre, apellido)
            break
    if not encontrado:
        print("No se encontró un socio con ese nombre y apellido")

# PARTE 6 
def imprimir_socios():
    print("Listado de socios:")
    for numero, datos in socios.items():
        print("Socio número", numero, "- Nombre completo:", datos["nombre"], datos["apellido"], "- Fecha de ingreso:", datos["fecha_ingreso"], "- Cuota al día:", datos["cuota_al_dia"])

# Ejemplo de uso de las funciones
print("Cantidad de socios:", cantidad_socios())
pago_de_cuotas(1)
corregir_fecha()
dar_de_baja("David", "Estévez")
imprimir_socios()
