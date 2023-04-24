#!/bin/python3

# Tenemos una archivo 'emails.txt' y tenemos que extraer todos los mails que corresponden a Yahoo y reemplazarlos por Gmail.

import re, os

archivo_origen = "emails.txt"
archivo_destino = "emails_gmail.txt"

if os.path.exists(archivo_origen):
    print(f"El archivo {archivo_origen} existe.")
else:
    print(f"El archivo {archivo_origen} no existe.")

if os.path.isfile(archivo_origen):
    print(f"{archivo_origen} es un archivo.")
else:
    print(f"{archivo_origen} no es un archivo.")

patron = r"([A-Za-z0-9._%+-]+)@(yahoo|hotmail)\.com\b"
reemplazo = r"\1@gmail.com" # se mantiene la primer parte del correo electrónico como es.

with open(archivo_origen, "r") as mi_arch1:
    contenido = mi_arch1.read()

nuevo_contenido = re.sub(patron, reemplazo, contenido)

with open(archivo_destino, "w") as archivo_destino:
    archivo_destino.write(nuevo_contenido)

print("Se ha creado el archivo con los correos electrónicos reemplazados exitosamente.")
