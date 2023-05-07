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

"""
email --> "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

--> [a-zA-Z0-9._%+-]+ 
    coincide con una o más letras, números o caracteres especiales que se permiten en una dirección de correo electrónico, como puntos (.), guiones (-), porcentajes (%) o signos más (+).
--> @ 
    coincide con el carácter de arroba que separa el nombre de usuario del dominio en una dirección de correo electrónico.
--> [a-zA-Z0-9.-]+ 
    coincide con una o más letras, números, guiones o puntos en el dominio.
--> \. 
    coincide con un punto literal en la dirección de correo electrónico.
--> [a-zA-Z]{2,} 
    coincide con dos o más letras en la parte del dominio de nivel superior (TLD) de la dirección de correo electrónico. Por ejemplo, .com, .org, .edu.

gmail --> "[a-zA-Z0-9._%+-]+@gmail\.com"
"""