"https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/WEB_%26_HTTP/Practica/Requests_Ejercicios.md" # --> GitHub

## GUÍA 6: PRACTICA REQUESTS ##

# 🧗‍♀️ Desafío I En base al siguiente enlace "https://pokeapi.co/api/v2/pokemon/pikachu", realizar las siguientes actividades adjuntando los archivos resultantes y el código utilizado para la realización de cada paso:

"""
a) ¿Cuál es el dominio al que estamos consultando?

b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type? Obtené la información correspondiente al campo "forms".

c) Averigüá cuántos Pokemones almacena la API.

d) ¿Cómo esperás que sea la URL para obtener las habilidades de los Pokemons (abilities)? ¿y cómo será la url para obtener la información sobre la habilidad 2?

e) Guardar los datos correspondientes a Pikachu y Sylveon en un archivo de nombre "ficha_tecnica_pokemon.txt".

f) Describí la arquitectura cliente-servidor y los roles de cada parte
"""


# a) ¿Cuál es el dominio al que estamos consultando?
import requests
# pikachu = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
# datos = pikachu.json()
# print(datos)
# --> El dominio es "pokeapi.co"


# b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type? Obtené la información correspondiente al campo "forms".
# print(pikachu.status_code)
# print(pikachu.headers['Content-Type'])
# --> El status_code es 200 y el Content-Type es "application/json"
# pikachu.json().keys()
# print(datos["forms"])
# --> Los datos son:
# [{'name': 'pikachu', 'url': 'https://pokeapi.co/api/v2/pokemon-form/25/'}]


# c) Averigüá cuántos Pokemones almacena la API.
# pokemones = requests.get("https://pokeapi.co/api/v2/pokemon")
# print(pokemones.json()['count'])


# d) ¿Cómo esperás que sea la URL para obtener las habilidades de los Pokemons (abilities)? ¿y cómo será la url para obtener la información sobre la habilidad 2?
# --> La URL para obtener las habilidades de los Pokemons (abilities) será "https://pokeapi.co/api/v2/pokemon/abilities"
# --> La URL para obtener la información sobre la habilidad 2 será "https://pokeapi.co/api/v2/pokemon/abilities/2"


# e) Guardar los datos correspondientes a Pikachu y Sylveon en un archivo de nombre "ficha_tecnica_pokemon.txt".
"""
1era opción:

pikachu = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
pikachu = str(pikachu.json())
sylveon = requests.get("https://pokeapi.co/api/v2/pokemon/sylveon")
sylveon = str(sylveon.json())

with open("ficha_tecnica_pokemon.txt", "wb") as ficha:
    ficha.write(pikachu)
    ficha.write(b'\n')
    ficha.write(sylveon)
"""

"""
2da opción:

pikachu = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
sylveon = requests.get("https://pokeapi.co/api/v2/pokemon/sylveon")

with open("ficha_tecnica_pokemon.txt", "wb") as ficha:
    ficha.write(pikachu.content)
    ficha.write(b'\n')
    ficha.write(sylveon.content)
"""


# f) Describí la arquitectura cliente-servidor y los roles de cada parte.
# --> La arquitectura cliente-servidor es un modelo de comunicación entre dos partes: un cliente y un servidor. El cliente realiza una petición al servidor a través de una URL y el servidor responde a dicha petición. El cliente es el que realiza la petición y el servidor es el que responde a la petición.
# --> Los roles de cada parte son:
# --> Cliente: es el que realiza la petición.
# --> Servidor: es el que responde a la petición.


# 🧗‍♀️ Desafío II Dado el siguiente enlace "https://jsonplaceholder.typicode.com/todos", realizar las siguientes actividades adjuntando los archivos resultantes y el código utilizado para la realización de cada paso:

"""
a) ¿Cuál es el dominio al que estamos consultando?

b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type?

c) Agregar un contenido cuyo userId es 11 y su id es 2 con un nuevo título e indicando que está completo (completed).

d) En la arquitectura cliente-servidor ¿Qué características tiene el cliente?
"""


# a) ¿Cuál es el dominio al que estamos consultando?
import requests,json
todos = requests.get("https://jsonplaceholder.typicode.com/todos")
datos = todos.json()
# print(datos)
# --> El dominio es "jsonplaceholder.typicode.com"


# b) ¿Qué status_code devuelve el pedido a dicha URL? ¿Y qué Content-Type?
# print(todos.status_code)
# print(todos.headers['Content-Type'])
# --> El status_code es 200 y el Content-Type es "application/json; charset=utf-8".


# c) Agregar un contenido cuyo userId es 11 y su id es 2 con un nuevo título e indicando que está completo (completed).
# --> Primero, creo un diccionario con los datos que quiero agregar:
data = { 
    "userId": 11,
    "id": 2,
    "title": "Los que te conocen, saben",
    "completed": True
}

headers = {'Content-Type': 'aplication/json; charset=utf-8'}

a = requests.post("https://jsonplaceholder.typicode.com/todos", data = json.dumps(data), headers=headers)

a.json()

# El elemento se agrega, pero noe xactamente como nosotros le pedimos que le agregue. No podemos modificar el id --> cambia automáticamente.


# d) En la arquitectura cliente-servidor ¿Qué características tiene el cliente?
# --> El cliente es el que realiza la petición. En este caso, el cliente es el que realiza el pedido a la URL.
