import os
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

engine= create_engine(os.getenv("DATABASE_URL"))
db= scoped_session(sessionmaker(bind= engine))  

# consults = "create table users (id serial primary key not null, username varchar not null, hash varchar not null)"
# db.execute(consults)
db.execute(f"INSERT INTO users (username,hash) values('Alejandro','{1234}')")   
db.commit()


