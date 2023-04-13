#!/bin/python3

import os
import sys
from datetime import datetime # para transformar fechas

archivo = sys.argv[1] # el primer parámetro se corresponde con la posición 1,
                      # dado que la posición 0 contiene al nombre del script

print("Obteniendo información del archivo", archivo)

estadisticas = os.stat(archivo)
print("Pesa:", estadisticas.st_size, "bytes")
print("Modificado por última vez:", datetime.utcfromtimestamp(estadisticas.st_atime).strftime('%Y-%m-%d %H:%M:%S'))