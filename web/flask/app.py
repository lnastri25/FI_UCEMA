from flask import Flask

prendas = [
    {"id": 1, "tipo": "pantalon", "talle": 42},
    {"id": 2, "tipo": "pantalon", "talle": 56}
]

app = Flask(__name__) # Me refiero a la aplicación por la palabra app. App va a ser el nombre que le voy a estar dando a mi servidor.

@app.get("/") # Decorador. Le estoy diciendo a mi servidor que cuando alguien entre a la ruta '/' (la ruta principal), ejecute la función que viene a continuación.
def home():
    return "<p>Te damos la bienvenida a MacoWins</p>"

# TAREA: Armar la ruta /prendas que muestre todos los items de prendas. OPCIONAL: ESCRIBIR O AGREGAR UN ELEMENTO.
