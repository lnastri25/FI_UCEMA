import requests # request = pedido

respuesta = requests.get("https://api.github.com/users/ajvelezrueda/orgs") # get --> verbo HTTP asociado a las consultas.
datos = respuesta.json()
print(datos)

# http --> requests --> Python
# verbos HTTP --> disparan acciones particulares --> siempre hablando de apliaciones Rest