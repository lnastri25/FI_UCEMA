#!/bin/python3

import re

#🧗‍♀️ Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?

"\d{4,} "

"\w{4, }" # Construyo una expresion regular que obtenga al menos 4 palabras.

#🧗‍♀️ Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?

"[a-z]{3,6}" 

#🧗‍♀️ Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?

"ab+"

"""
# ---------- #

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet" 
print(re.search(patron,texto)) 
print(texto[22:26]) 

# ---------- #

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.match(patron,texto))

# El función match() de re busca el patrón y devuelve la primera aparición y solo al principio de la cadena. 
# Si se encuentra una coincidencia en la primera línea, devuelve el objeto de coincidencia. 
# Pero, si se encuentra una coincidencia en alguna otra línea, devulve un valor nulo.

# ---------- #

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.findall(patron, texto)) # El resultado da una lista con todas las apariciones del patron especifico de expresion regular que yo le especifiqué.

# ---------- #

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "amet"
print(re.search(patron, texto).group()) # Me junta el string del resultado que yo le pasé, del patron que encontró.
"""

# ---------- #

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "ipsum(.*)sit" # el punto (.) para indicar que puede ser cualquier carácter, y el asterísco (*) para indicar que puede haber 0 o más de estos caracteres. De esta manera obtenemos como resultado lo que se encuentre entre las palabras "ipsum" y "sit".
print(re.search(patron, texto), "\n")
print(re.search(patron, texto).group())
print(re.search(patron, texto).group(0))
print(re.search(patron, texto).group(1)) # Solo el resultado de la busqueda sin incluir lo que yo busqué.
print(re.sub(patron, "###", texto)) # Reemplaza ipsum por ###

# ---------- #

"""
    Las expresiones regulares se usan para poder hacer búsquedas masivas de texto con patrones en particular sin saber en la fuente en la que estoy buscando, qué es lo que me voy a encontrar. Se que quiero, pero no sé qué hay.
        - En desarrollo web → se usa para validación de cosas. (por ejemplo para saber si un mail o una tarjeta, es válido o no)
        - Si te queres bajar algo de un link, podes delimitar la información que te podes bajar con expresiones regulares

    Sirven para:
    a) Validaciones (log in, tarjetas)
    b) Web scraping
    c) Ver si alguien se copió en algun examen.

    - Para la computadora todo lo que veo se puede traducir a un carácter.


1) re.search(pattern, string, flags=0)

    - Examina a través de la string («cadena») buscando el primer lugar donde el pattern («patrón») de la expresión regular produce una coincidencia, y retorna un objeto match correspondiente. Retorna None si ninguna posición en la cadena coincide con el patrón; notar que esto es diferente a encontrar una coincidencia de longitud cero en algún punto de la cadena.
    - De por sí no devuelve nada. Devuelve 'None' y por eso usamos bool.

2) re.match(pattern, string, flags=0) 

    - Si cero o más caracteres al principio de la string («cadena») coinciden con el pattern («patrón») de la expresión regular, retorna un objeto match correspondiente. Retorna None si la cadena no coincide con el patrón; notar que esto es diferente de una coincidencia de longitud cero.

3) re.split(pattern, string, maxsplit=0, flags=0)

    - Divide la string («cadena») por el número de ocurrencias del pattern («patrón»). Si se utilizan paréntesis de captura en pattern, entonces el texto de todos los grupos en el patrón también se retornan como parte de la lista resultante. Si maxsplit (máxima divisibilidad) es distinta de cero, como mucho se producen maxsplit divisiones, y el resto de la cadena se retorna como elemento final de la lista.

4) re.findall(pattern, string, flags=0)

    - Retorna todas las coincidencias no superpuestas de pattern en string, como una lista de strings o tuplas. El string se escanea de izquierda a derecha y las coincidencias se retornan en el orden en que se encuentran. Las coincidencias vacías se incluyen en el resultado.
    
    - El resultado depende del número de grupos detectados en el patrón. Si no hay grupos, retorna una lista de strings que coincidan con el patrón completo. Si existe exactamente un grupo, retorna una lista de strings que coincidan con ese grupo. Si hay varios grupos presentes, retorna una lista de tuplas de strings que coinciden con los grupos. Los grupos que no son detectados no afectan la forma del resultado.


# Para hacer un patrón que queremos que lea más de una letra --> hay que usar *^, etc porque sino los matches van a ser de solamente un caracter. 

"""

# [a-z] --> lorenzo.nastri --> me trae l
# [a-z]* --> lorenzo.nastri --> me trae lorenzo.nastri
# [a-z]+ --> lorenzo.nastri --> me trae lorenzo.nastri
# [a-z]+[.] --> lorenzo.nastri --> me trae lorenzo.

# Ejercicio MAIL: #
# r: significa que cualquier carácter especial contenido en la cadena se interpreta literalmente. (raw string)

# ^: indica el inicio de línea

# [a-zA-Z0-9._%+-]+: representa el nombre del usuario de la dirección de correo electrónico, 
# el cual debe estar conformado por uno o más caracteres alfanuméricos, puntos, guiones bajos, porcentajes, más y guiones.

# @: se utiliza para separar el nombre del usuario de la dirección de correo electrónico del dominio.

# [a-zA-Z0-9.-]+: especifica el dominio del correo electrónico, puede estar conformado por uno o más caracteres alfanuméricos, puntos y guiones.

# \.: indica que debe haber un punto.

# [a-zA-Z]{2,}: especifica la extensión de la dirección de correo electrónico, la cual debe estar conformada por dos o más caracteres alfabéticos.


"""
1) Listado de caracteres para biblioteca RE:

\n --> salto de linea.
\t --> tab o cambio de pestaña.
\s --> espacio.
\s+ --> que tenga un espacio o más.
\S --> que no tenga un espacio.
' --> comillas simples.
" --> comillas dobles.
^ --> inicio de línea.
$ --> fin de línea.
\A --> incio de texto.
\Z --> fin de texto.
. --> coincide con cualquier caracter en una línea dada. (todo lo que tengo acá)
* --> cero o más veces.
+ --> una o más veces.
? --> cero o una vez. (puede estar o no estar)
{n} --> exactamente n veces.
{n,m} --> por lo menos n pero no más de m veces.
\w --> caracter alfanumerico. (buscame palabras)
\W --> caracter no alfanumerico.
\d --> caracter numerico. (buscame numeros)
\D --> caracter no numerico.
\b --> borde de palabra.
\B --> no borde de palabra.

2) Los rangos [] se escriben entre corchetes y le dicen a la herramienta entre que buscar.
[a-z] --> busca entre a y z.
[A-Z] --> busca entre A y Z.
[0-9] --> busca entre 0 y 9.
[a-zA-Z0-9] --> busca entre a y z, A y Z y 0 y 9.

3) raw string

    - A causa de que las expresiones regulares a menudo utilizan caracteres de escape (como por ejemplo la barra invertida ), es necesario indicar que las mismas no se interpreten como tales sino como parte de la expresión regular propiamente dicha. La forma más simple de hacerlo es comenzar la cadena con una letra r para indicar que la misma debe tomarse literalmente. En Python, esto se denomina un raw string.
"""