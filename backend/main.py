from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Veterinaria API")

# Configuración de CORS para permitir peticiones desde el frontend (React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Puerto por defecto de Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LoginData(BaseModel):
    email: str
    password: str

@app.post("/api/login")
def login(data: LoginData):
    # Simulación sencilla de validación
    if data.email == "admin@veterinaria.com" and data.password == "123456":
        return {
            "status": "success",
            "message": "¡Bienvenido al sistema de gestión!",
            "token": "fake-jwt-token-12345"
        }
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")