from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, String, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List, Optional
import os
import databases

# Definición del modelo de datos
DATABASE_URL = "sqlite:///./usuarios.db"
database = databases.Database(DATABASE_URL)
metadata = MetaData()

# Definir la tabla de usuarios
usuarios = Table(
    "usuarios",
    metadata,
    Column("dni", String, primary_key=True),
    Column("nombre", String),
)

# Modelo Pydantic para la validación de datos
class Usuario(BaseModel):
    dni: str
    nombre: str

class UsuarioResponse(BaseModel):
    dni: str
    nombre: str

# Configuración de la base de datos SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata.create_all(engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Inicialización de la aplicación FastAPI
app = FastAPI(title="API de Usuarios")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Endpoints
@app.post("/usuarios/", response_model=UsuarioResponse)
async def crear_usuario(usuario: Usuario):
    # Verificar si el usuario ya existe
    query = usuarios.select().where(usuarios.c.dni == usuario.dni)
    existing_user = await database.fetch_one(query)
    
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario con este DNI ya existe")
    
    # Insertar nuevo usuario
    query = usuarios.insert().values(dni=usuario.dni, nombre=usuario.nombre)
    await database.execute(query)
    return usuario

@app.get("/usuarios/", response_model=List[UsuarioResponse])
async def listar_usuarios():
    query = usuarios.select()
    return await database.fetch_all(query)

@app.get("/usuarios/{dni}", response_model=UsuarioResponse)
async def obtener_usuario(dni: str):
    query = usuarios.select().where(usuarios.c.dni == dni)
    usuario = await database.fetch_one(query)
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    return usuario

# Para ejecutar la aplicación con uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
