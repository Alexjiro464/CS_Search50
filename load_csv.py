import os
import csv
from dotenv import load_dotenv  
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

load_dotenv()

engine= create_engine(os.getenv("DATABASE_URL"))
db= scoped_session(sessionmaker(bind= engine))

consults = "create table books (id SERIAL PRIMARY KEY NOT NULL, isbn VARCHAR(10) NOT NULL, title VARCHAR NOT NULL, author VARCHAR, year VARCHAR(4))"

db.execute(consults)

# db.execute("drop table books")

db.commit()

print("tabla creada")

# 

f=open("books.csv")
reader =csv.reader(f)

algo = 1

# Itera dentro del csv y almacena en base de datos
for isbn,title,author,year in reader:
    if isbn == "isbn":
        # No hacer nada xd, es la linea de cabeceras
        print("Linea de cabeceras omitida")
    else:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
            {"isbn":isbn, "title":title, "author":author, "year":year})

        print(algo)
        algo += 1

print("Todo añadido a la base de datos...")

db.commit()
