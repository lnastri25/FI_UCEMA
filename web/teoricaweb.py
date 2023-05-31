import requests # request = pedido

respuesta = requests.get("https://api.github.com/users/ajvelezrueda/orgs")
datos = respuesta.json()
print(datos)
# 1) En cuantas organizaciones está involucrado el usuario:
# print(len(datos))
# 2) En login sacamos la información del nombre del usuario:
# print(datos[0]["login"])
# 3) Lista de nombres de las organizaciones en la que está involucrado ['TAREA']:
for organizacion in datos:
    print(organizacion["login"])

# --> Como los nombres de las organizaciones están en 'login', le digo que me traiga el diccionario pero con los nombres de las organizaciones ('login)

# print(respuesta)
# print(respuesta.headers) # --> Me da una información sobre el propio request. ¿Cuándo se hizo request?, ¿A qué servidor se hizo el request?
# print(respuesta.status_code) # --> El status_code de esta operación fue 403 --> me dice como funcionó esa conexión. https://http.cat/