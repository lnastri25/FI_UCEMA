# Modificar el script para que tome el nombre de los archivos desde la terminal.
# os.path.exists(path)

import os

archivo1 = "hola2.txt"
archivo2 = "chau2.txt"

# Verifica si el archivo "hola2.txt" existe en el directorio actual. 
# Si el archivo no existe, se ejecuta el bloque de código siguiente.


# Muestra un mensaje de error indicando que el archivo "hola2.txt" no existe. 
# La letra "f" antes de la cadena de texto indica que es una cadena de formato, 
# lo cual permite interpolar variables dentro de la cadena usando llaves {}.

if not os.path.exists(archivo1):
    print(f"El archivo {archivo1} no existe.")
    exit(1)

# Verifica si el archivo "chau2.txt" existe en el directorio actual. 
# Si el archivo no existe, se ejecuta el bloque de código siguiente.

if not os.path.exists(archivo2):
    print(f"El archivo {archivo2} no existe.")
    exit(1)

os.rename(archivo1, "temporal")
os.rename(archivo2, archivo1)
os.rename("temporal", archivo2)
