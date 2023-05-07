#!/bin/python3

def main():
    print("hola mundo")

if __name__ == "__main__":
  main()

# Script que ejecuta el codigo que está en otros archivos o justamente en esta funcion el 
# codigo que está más arriba. "El main script"

"""
1) Python:

  - Lenguaje de alto nivel con gran nivel de interpretación.
  - El intérprete es un software que se encarga de hacer la interfaz humano-computadora. Pueden operar en una consola/terminal.

2) Script:

  - Es un archivo con una extensión particular que va a determinar en que lenguaje va a estar escrito. En este caso, PY va a indicar que tipo de script estamos usando. Los scripts son generalmente un archivo en donde voy tirando código y particularmente se ejecutan contra el intérprete de Python (Git Bash).
  - Código de corrida rápida.

3) Prompt:

  - El prompt de Python es (>>>). Si no estoy corriendo nada ahí, es porque algo mal estoy haciendo.
  - Si quiero salir del prompt, tengo que escribir "exit()".

4) IDE: 

  - Entorno de programación interactivo. Editor de texto que me ayuda a programar.

5) Terminal:

  - Me va a decir dónde es que estoy parado con la computadora. Para ejecutar un script, tengo que estar en la carpeta del script. 

6) Biblioteca:

  - Es un directorio/carpeta que tiene scripts con funciones de Python con funciones útiles para ser usadas. Me instalo una biblioteca porque me permite trabajar/arreglar/manejar datos que son más complejos que un string, un bool o vincularse con el sistema operativo. Para hacer esto uso el gestor de paquetes llamado PIP. 

  “pip install ____”

  - Para verificar si una librería está instalada o no. “import pandas as pd”. Si corre y no me tira error es porque la tengo instalada.

7) Listado de comandos útiles para la terminal:
  - ls (lista los archivos que tengo dentro de un directorio; muestra los contenidos de un directorio)
  - cd (change directory)
  - pwd (path to working directory; donde estoy trabajando; muestra el directorio actual)
  - ls -a (lista los archivos ocultos tambien)

8) ADICIONALES:
  --> *Funciones*:
    Una función es un bloque de código que realiza una tarea específica y devuelve un valor. Las funciones pueden tener parámetros de entrada y un valor de retorno. Las funciones son autónomas y se pueden llamar desde cualquier parte del programa.

--> *Procedimientos*:
    Un procedimiento es similar a una función en que es un bloque de código que realiza una tarea específica. Sin embargo, a diferencia de las funciones, los procedimientos no tienen un valor de retorno. Los procedimientos pueden tener parámetros de entrada, pero su propósito principal es realizar una acción específica en lugar de devolver un valor.

--> *Diferencias entre snake_case y Camel_Case:*

    La razón técnica detrás de la utilización de convenciones de nomenclatura como camel case o snake case es que, al nombrar variables, funciones y otros elementos de código de manera consistente, se facilita la lectura y comprensión del código para otros programadores. Esto puede ser especialmente útil en proyectos grandes o en equipo, donde muchas personas trabajan en el mismo código.
    Además, seguir una convención de nomenclatura consistente puede ayudar a evitar errores y reducir el tiempo que se tarda en entender y modificar el código. Al utilizar una convención de nomenclatura clara y coherente, se hace más fácil identificar rápidamente qué hacen las variables y funciones, y cómo están relacionadas entre sí. En última instancia, esto puede ayudar a mejorar la calidad y eficiencia del código.


    --> *Convención de Nomenclatura Consistente*:
    La convención de nomenclatura consistente se refiere al conjunto de reglas y prácticas que se siguen para nombrar variables, funciones y otros elementos de código en un proyecto de programación. La idea es establecer una forma coherente y uniforme de nombrar los elementos del código para que sea más fácil de leer, entender y mantener por los desarrolladores que trabajan en el proyecto.

    Por ejemplo, una convención de nomenclatura consistente podría ser nombrar las variables en minúsculas con guiones bajos para separar las palabras, como "nombre_de_variable". Otra convención podría ser nombrar las funciones con verbos que reflejen su acción, como "calcular_suma". Siguiendo una convención de nomenclatura consistente, se puede mejorar la legibilidad y la calidad del código, y hacer que el proceso de programación sea más eficiente y efectivo.

---------------------------

--> *Estructura de codigo limpia:

    Legibilidad: Un código limpio es más fácil de leer y entender, no solo para uno mismo, sino también para otros programadores que puedan trabajar en el proyecto en el futuro. Si el código es difícil de entender, puede resultar en errores y problemas de mantenimiento.

    Mantenibilidad: Un código limpio y bien estructurado es más fácil de modificar y mantener a lo largo del tiempo. Si el código no está estructurado correctamente, puede ser difícil identificar dónde se encuentra un problema o cómo se relacionan diferentes partes del código.

    Eficiencia: Un código limpio y ordenado puede ser más eficiente en términos de rendimiento, ya que puede requerir menos recursos y tiempo para ejecutarse.

    Colaboración: Cuando se trabaja en un proyecto de equipo, seguir una estructura de código limpia y ordenada puede facilitar la colaboración y el trabajo en equipo. Todo el mundo puede entender rápidamente lo que está sucediendo en el proyecto y contribuir de manera efectiva.
"""