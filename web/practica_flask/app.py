from flask import Flask, render_template, request, redirect
from markupsafe import escape

# python3 -m flask run #

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html") 

@app.get("/resultados/")
def get_resultados():
    return render_template("resultados.html") 

@app.get("/plan_2023/")
def get_conclusiones():
    return render_template("conclusiones.html") 