from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from db import db, siguiente_id

router = APIRouter()

class ClienteNuevo(BaseModel):
    nombre: str
    telefono: str
    correo: str

class PuntosUpdate(BaseModel):
    puntos: int

@router.post("/")
def registrar_cliente(cliente: ClienteNuevo):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 1"})

@router.get("/buscar")
def buscar_cliente(q: Optional[str] = None):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 5: Must Have — implementar en Timebox 1",
        "pista": "Usa el parametro 'q' que FastAPI ya extrajo por ti para filtrar la lista"
    })

@router.get("/{id}")
def ver_cliente(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 1"})

@router.patch("/{id}/puntos")
def agregar_puntos(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 2"})

@router.put("/{id}")
def editar_cliente(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 2"})

@router.delete("/{id}")
def eliminar_cliente(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 2"})

@router.post("/{id}/enviar-promociones")
def enviar_correo_promociones(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Equipo 5"})

