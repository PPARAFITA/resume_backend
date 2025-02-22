from fastapi import FastAPI
from api.routers import user, work_experience_controller, education_controller
from database import init_db
from contextlib import asynccontextmanager

@contextmanager
def lifespan(app: FastAPI):
    # Código para el evento de inicio
    print("Application startup")
    init_db()  # Crear las tablas cuando la aplicación arranca
    yield
    # Código para el evento de cierre
    print("Application shutdown")

app_api = FastAPI(lifespan=lifespan)

app_api.include_router(user.router)
app_api.include_router(work_experience_controller.router) 
app_api.include_router(education_controller.router) 