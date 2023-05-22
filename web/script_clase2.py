import requests

respuesta = requests.get('https://pokeapi.co/api/v2/ability/150/')
print(respuesta.json())