import os
from flask import Flask
from flask import redirect, session, render_template, request, flash
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from dotenv import load_dotenv  
from flask.session import Session
from sqlalchemy.orn import scoped_session, sessionmaker
from sqlalchemy import create_engine


app=Flask(__name__)
# me falta la conexion de la base de datos

# Configurando la aplicacion
app.config["SESSION_FILE_DIR"]= mkdtemp()
app.config["SESSION_PERMANENT"]= False
app.config["SESSION_TYPE"]= "filesystem"

Session(app)

engine= create_engine(os.getenv("DATABASE_URL"))
db= scoped_session(sessionmaker(bind= engine))



@app.route("/", methods= ["GET", "POST"])
# login required
def index():
    Nombre = ["Alejandro", "Hector", "Joshua", "Jeffersson", "David"]
    return render_template("index.html", Nombre = Nombre)
