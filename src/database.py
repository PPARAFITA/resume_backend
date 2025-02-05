import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar las variables del archivo .env solo si estás en desarrollo
if os.getenv("FLASK_ENV") != "production":
    load_dotenv()  # Cargar el archivo .env para el entorno local

DATABASE_URL = os.getenv("DB_HOST")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()