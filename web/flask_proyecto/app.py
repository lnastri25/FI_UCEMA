from flask import Flask, render_template
from markupsafe import escape # Me permite trabajar con seguridad para que no me hackeen la API con código de JavaScript.

prendas = [
    {"id": 1, "tipo": "pantalon", "talle": 42},
    {"id": 2, "tipo": "pantalon", "talle": 56}
]
app = Flask(__name__) # Me refiero a la aplicación por la palabra app. App va a ser el nombre que le voy a estar dando a mi servidor.

@app.get("/") # Decorador. Le estoy diciendo a mi servidor que cuando alguien entre a la ruta '/' (la ruta principal), ejecute la función que viene a continuación. 
def home(): # El método me va a definir qué verbo voy a tener que usar en el endpoint. 
    return render_template("home.html")

"""
* ENDPOINTS / RUTAS / RECURSOS *

/prendas:
# GET --> buscar las prendas.
# POST --> agregar una prenda nueva.

/prendas/<id>:
# GET --> busco una sola prenda de id == id.
# PATCH --> Modificar esa prenda.
"""

"""
# TAREA: Armar la ruta /prendas que muestre todos los items de prendas.
@app.get("/prendas")
def mostrar_prendas():
    muestra = ""
    for prenda in prendas:
        muestra += f"Prenda {prenda['id']}: Tipo {prenda['tipo']}, Talle {prenda['talle']}<br>"
    return muestra
"""

@app.get("/prendas")
def get_all_prendas():
    return f"<p>Mostrando todas las prendas</p>"

@app.get("/prendas/<id>")
def get_prenda(id):
    return f"<p>Mostrando la prenda {escape(id)}</p>"

