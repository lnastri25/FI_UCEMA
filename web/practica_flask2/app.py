from flask import Flask, render_template, request, redirect
from markupsafe import escape

# python3 -m flask run #

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("home.html") 
