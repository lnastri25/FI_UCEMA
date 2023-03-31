#!/bin/python3

import os

archivo1 = "hola.txt"
archivo2 = "chau.txt"

os.rename(archivo1, "temporal")
os.rename(archivo2, archivo1)
os.rename("temporal", archivo2)



# Imprime un mensaje de éxito
print("Los nombres de los archivos se han intercambiado exitosamente.")


# Modificar el script para que tome el nombre de los archivos desde la terminal.
# os.path.exists(path)
