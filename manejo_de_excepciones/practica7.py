#!/bin/python3

"https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/Python_intro/Practicas/Pr%C3%A1ctica_Manejo_de_excepciones.md" # --> GitHub

# Ejercicio 1 #
# Dado el siguiente bloque de código contestar:

lista_super = ["tomate", "fideos", "arvejas", "detergente", "jabón", "alcohol"]
try:
    lista_super + "arroz"
except TypeError: # le agregué el error
    print("No puedo agregar arroz porque no se puede sumar un string a una lista.")

# ¿Es correcto el uso del try...except? ¿Qué cosa/s le modificarías?

# Desde mi punto de vista, NO es correcto el uso del try...except, ya que no se está especificando el tipo de error que se quiere manejar. Se debería especificar el tipo de error que se quiere manejar, por ejemplo TypeError. Además, el print en el 'except' debe ser explicativo, es por eso que le agregamos un mensaje un poco más claro.

# Ejercicio 2 #
# Definir una función que tenga como parámetros una lista de números por un lado y un número por otro y devuelva una lista con la división de cada elemento por el número dado. Por ejemplo, si le paso ([2,4,6,8], 2), debería retornar [1,2,3,4]. Tomar las precauciones necesarias.

def division(lista, numero):
    try:
        return [elemento/numero for elemento in lista]
    except ZeroDivisionError:
        print("No se puede dividir por", numero)
    except TypeError:
        print("El", numero, "es un string")

print(division([2,4,6,8], 2))
print(division([2,4,6,8], 0))
print(division([2,4,6,8], "2"))

# Ejercicio 3 #
# Definir un procedimiento, que reciba una lista y un número, el cual tiene que agregar el número a la lista solo si el número es positivo. De lo contrario debería generar un error indicando que el número no es positivo.

def agregar(lista, numero):
    try:
        if numero > 0:
            lista.append(numero)
        else:
            raise ValueError("El número no es positivo")
    except ValueError as error:
        print(error)

lista = [1, 2, 3, 4, 5]
agregar(lista, 6)