from flask import Flask, render_template, request, redirect
from markupsafe import escape

# python3 -m flask run #

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html") 

"""
🧗‍♀️ Desafío I: Estamos construyendo una aplicación Web para un biblioteca, en la cuál podrá:

consultar y cargar o borrar información sobre libros

consultar y cargar o borrar revistas y audio libros disponibles

a) Escribí las posibles rutas indicando sus métodos HTTP correspondientes.
"""

@app.get("/libros")
def libros():
    return render_template("libros.html")

@app.get("/libros/<id>")
def libros_id(id):
    return render_template("libros_id.html", id=id)

@app.post('/borraLibro')
def borraLibro():
    return redirect("/libros")

@app.get("/revistas")
def revistas():
    return render_template("revistas.html")

@app.get("/revistas/<id>")
def revistas_id(id):
    return render_template("revistas_id.html", id=id)

@app.post('/borraRevista')
def borraRevista():
    return redirect("/revistas")

if __name__ == "__main__":
    app.run(debug=True)
