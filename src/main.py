from fastapi import FastAPI
from src.adapters.routers import user, work_experience_controller, education_controller, resume_controller
from src.adapters.database.database import init_db
from contextlib import asynccontextmanager  
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Código para el evento de inicio
    print("Application startup")
    init_db()  # Crear las tablas cuando la aplicación arranca
    yield
    # Código para el evento de cierre
    print("Application shutdown")

app_api = FastAPI(lifespan=lifespan)

# 🔹 Agregar CORS Middleware
app_api.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir solo tu frontend en local
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

app_api.include_router(user.router)
app_api.include_router(work_experience_controller.router) 
app_api.include_router(education_controller.router) 
app_api.include_router(resume_controller.router) 