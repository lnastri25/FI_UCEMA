from flask import Flask

app = Flask(__name__) # Me refiero a la aplicación por la palabra app. App va a ser el nombre que le voy a estar dando a mi servidor.

@app.get("/") # Decorador. Le estoy diciendo a mi servidor que cuando alguien entre a la ruta '/' (la ruta principal), ejecute la función que viene a continuación.
def home():
    return "<p>Te damos la bienvenida a MacoWins</p>"