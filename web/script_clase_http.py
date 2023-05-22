"""
1) Describir las partes de la url.
2) ¿Qué respuesta obtenés al hacer un get a esa url?
3) ¿Cuál es el content type de esa respuesta?
4) ¿Cuál es el status code de la respuesta?
5) ¿Cuántas habilidades ('abilities') tiene este Pokemon?
"""
import requests

respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")

datos = respuesta.json()

# 1)
# url --> https://pokeapi.co/api/v2/pokemon/ditto
# https --> protocolo
# pokeapi.co --> dominio principal
# /api/v2/pokemon/ditto --> ruta o path

# 2) 
# print(respuesta) # <Response [200]> --> 200 es el status code de la respuesta. 200 es que todo salió bien.

# 3)
# print(respuesta.headers['Content-Type']) # --> El content type de esta url es: application/json; charset=utf-8

# 4)
# print(respuesta.status_code) # --> El status code de esta url es: 200

# 5) 
# print(len(datos["abilities"])) # --> 2