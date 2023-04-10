#!/bin/python3

import re

#🧗‍♀️ Desafío I: ¿Construí la expresión regular que obtenga al menos 4 dígitos?

"\d{4,} "

"\w{4, }" # Construyo una expresion regular que obtenga al menos 4 palabras.

#🧗‍♀️ Desafío II: ¿Construí la expresión regular que obtenga al entre 3 y 6 letras minúsculas?

"[a-z]{3,6}" 

#🧗‍♀️ Desafío III: ¿Construí la expresión regular que obtenga todas las apariciones del patrón ab en un string?

"ab+"

"""# ---------- #

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
print(re.search(patron, texto).group()) # Me junta el string del resultado que yo le pasé, del patron que encontró."""

# ---------- #

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Amet et amet."
patron = "ipsum(.*)sit" # el punto (.) para indicar que puede ser cualquier carácter, y el asterísco (*) para indicar que puede haber 0 o más de estos caracteres. De esta manera obtenemos como resultado lo que se encuentre entre las palabras "ipsum" y "sit".
print(re.search(patron, texto), "\n")
print(re.search(patron, texto).group())
print(re.search(patron, texto).group(0))
print(re.search(patron, texto).group(1)) # Solo el resultado de la busqueda sin incluir lo que yo busqué.
print(re.sub(patron, "###", texto)) # Reemplaza ipsum por ###

# ---------- #

## re.search(pattern, string, flags=0) ##
# Examina a través de la string («cadena») buscando el primer lugar donde el pattern («patrón») de la expresión regular produce una coincidencia, y retorna un objeto match correspondiente. Retorna None si ninguna posición en la cadena coincide con el patrón; notar que esto es diferente a encontrar una coincidencia de longitud cero en algún punto de la cadena.

## re.match(pattern, string, flags=0) ##
# Si cero o más caracteres al principio de la string («cadena») coinciden con el pattern («patrón») de la expresión regular, retorna un objeto match correspondiente. Retorna None si la cadena no coincide con el patrón; notar que esto es diferente de una coincidencia de longitud cero.

## re.split(pattern, string, maxsplit=0, flags=0) ##
# Divide la string («cadena») por el número de ocurrencias del pattern («patrón»). Si se utilizan paréntesis de captura en pattern, entonces el texto de todos los grupos en el patrón también se retornan como parte de la lista resultante. Si maxsplit (máxima divisibilidad) es distinta de cero, como mucho se producen maxsplit divisiones, y el resto de la cadena se retorna como elemento final de la lista.

## re.findall(pattern, string, flags=0) ##
# Retorna todas las coincidencias no superpuestas de pattern en string, como una lista de strings o tuplas. El string se escanea de izquierda a derecha y las coincidencias se retornan en el orden en que se encuentran. Las coincidencias vacías se incluyen en el resultado.

# El resultado depende del número de grupos detectados en el patrón. Si no hay grupos, retorna una lista de strings que coincidan con el patrón completo. Si existe exactamente un grupo, retorna una lista de strings que coincidan con ese grupo. Si hay varios grupos presentes, retorna una lista de tuplas de strings que coinciden con los grupos. Los grupos que no son detectados no afectan la forma del resultado.