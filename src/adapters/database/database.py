import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar las variables del archivo .env solo si estás en desarrollo
if os.getenv("ENV") != "production":
    load_dotenv()  # Cargar el archivo .env para el entorno local

DATABASE_URL = os.getenv("DB_HOST")

if not DATABASE_URL:
    raise ValueError("La variable de entorno 'DB_HOST' no está configurada correctamente.")

try:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        print("Conexión exitosa a la base de datos.")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")

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