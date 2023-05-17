"""
__TIPOS _DE_ERRORES__

## ERROR DE SINTAXIS ##

1) SyntaxError:

    - Ocurre cuando Python encuentra un error de sintaxis. Es decir, cuando encuentra una instrucción que no sigue las reglas de sintaxis del lenguaje.
    
    - Ejemplo:
>>> print(Hola mundo')
  File "<stdin>", line 1
    print(Hola mundo')
               ^
SyntaxError: invalid syntax

## EXCEPCIONES ## 

2) NameError:

    - Ocurre cuando Python encuentra un nombre que no puede asociar con ningún objeto.

    - Ejemplo:
>>> print(divisor)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

NameError: name 'divisor' is not defined

3) TypeError:

    - Ocurre cuando Python encuentra un operador o función que se aplica a un objeto de tipo inadecuado.

    - Ejemplo:
>>> 0 + "2"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'

4) ZeroDivisionError:

    - Ocurre cuando se intenta dividir un número por cero.

    - Ejemplo:
>>> 3 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

ZeroDivisionError: division by zero

## PREVEER EXCEPCIONES PARA QUE NO SE INTERRUMPA LA EJECUCUÓN ## 

Bueno, para el manejo de excepciones Python nos provee palabras reservadas, que nos permiten manejar las excepciones que puedan surgir y tomar acciones que evitan la interrupción del programa o permitan especificar información adicional antes de interrumpir el programa. Una de las palabras reservadas es try, esta nos permite "encapsular" un bloque de código para interceptar e identificar excepciones. Si se produce un error dentro de la declaración try-except, se omite una excepción y se ejecuta el bloque de código que maneja la excepción.

try:
    # aquí ponemos el código que puede lanzar excepciones
except:
    # entrará aquí en caso que se haya producido una excepción
"""

# 🧗‍♀️Desafio II: Creá una función denominada eneavo que tenga como argumento un número e imprima el resultado de la división de 1 por ese número
# Para pensar 🤔: ¿Qué crees que ocurrirá cuando ingresas un 9 como parámetro? ¿Y con un 0?

def eneavo(numero):
    try:
        print(1/numero)
    except ZeroDivisionError:
        print("No se puede dividir por", numero)
    except TypeError:
        print("El", numero, "es un string")
        
    print(numero)

eneavo("9")
eneavo(0)

"""
## EXCEPCIONES PERSONALIZADAS ##

En algunos casos, puede ser necesario crear excepciones personalizadas o forzar que ocurra una excepción específica dado un contexto. La sentencia raise, se puede indicar el tipo de excepción que deseamos lanzar y el mensaje de que queremos brindarle al usuario:

def check_int_type():
  if type(x)  != int:
    raise TypeError("Only integers are allowed")
"""