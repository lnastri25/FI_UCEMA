import requests # request = pedido

respuesta = requests.get("https://api.github.com/users/ajvelezrueda/orgs")
datos = respuesta.json()
# 1) En cuantas organizaciones está involucrado el usuario:
print(len(datos))
# 2) En login sacamos la información del nombre del usuario:
print(datos[0]["login"])
# 3) Lista de nombres de las organizaciones en la que está involucrado ['TAREA']:

print(respuesta)
print(respuesta.headers) # --> Me da una información sobre el propio pedido. ¿Cuándo se hizo pedido?, ¿A qué servidor se hizo el pedido?