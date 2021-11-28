import os
from flask import Flask
from flask import redirect, session, render_template, request, flash
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv  

app=Flask(__name__)
# me falta la conexion de la base de datos

# Configurando la aplicacion
app.config["SESSION_FILE_DIR"]= mkdtemp()
app.config["SESSION_PERMANENT"]= False
app.config["SESSION_TYPE"]= "filesystem"




@app.route("/", methods= ["GET", "POST"])
# login required
def index():
    Nombre = ["Alejandro", "Hector", "Joshua"]
    return render_template("index.html", Nombre = Nombre)

