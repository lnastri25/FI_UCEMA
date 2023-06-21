from flask import Flask, render_template, request, redirect
from markupsafe import escape

# python3 -m flask run #

app = Flask(__name__)

productos = {
    1: {"nombre": "Shampoo sólido", "Stock": 5, "precio": 1000},
    2: {"nombre": "Crema de manos", "Stock": 6, "precio": 2000},
}

@app.get("/")
def home():
    return render_template("home.html") 

@app.get("/productos/")
def get_all_productos():
    return render_template("productos.html", productos=productos.items())

@app.get("/productos/<int:id>/")
def get_producto(aidi):
    if aidi in productos:
        producto = productos[aidi]
        return render_template('producto.html', id=aidi, producto=producto)
    else:
        return ("No hay producto", 404)
