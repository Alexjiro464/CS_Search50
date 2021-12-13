import os
from dotenv import load_dotenv  
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine

load_dotenv()

engine= create_engine(os.getenv("DATABASE_URL"))
db= scoped_session(sessionmaker(bind= engine))

