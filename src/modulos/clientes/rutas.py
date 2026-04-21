from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from db import db, siguiente_id

router = APIRouter()

class ClienteNuevo(BaseModel):
    nombre: str
    telefono: str
    correo: EmailStr

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v):
        if not v or not v.strip():
            raise ValueError("El nombre no puede estar vacío")
        return v.strip()

    @field_validator("telefono")
    @classmethod
    def telefono_no_vacio(cls, v):
        if not v or not v.strip():
            raise ValueError("El teléfono no puede estar vacío")
        return v.strip()

class PuntosUpdate(BaseModel):
    puntos: int

@router.post("/")
def registrar_cliente(cliente: ClienteNuevo):
    nuevo = {
        "id": siguiente_id("clientes"),
        "nombre": cliente.nombre,
        "telefono": cliente.telefono,
        "correo": cliente.correo,
        "visitas": 0,
        "puntos": 0
    }
    db["clientes"].append(nuevo)
    return JSONResponse(status_code=201, content={
        "mensaje": "Cliente registrado exitosamente",
        "cliente": nuevo
    })

@router.get("/buscar")
def buscar_cliente(q: Optional[str] = None):
    if not q or not q.strip():
        return JSONResponse(status_code=400, content={
            "error": "Parámetro requerido",
            "mensaje": "Debes proporcionar un término de búsqueda con el parámetro 'q'"
        })

    termino = q.strip().lower()
    resultados = [
        c for c in db["clientes"]
        if termino in c["nombre"].lower() or termino in c["telefono"]
    ]

    if not resultados:
        return JSONResponse(status_code=404, content={
            "mensaje": f"No se encontraron clientes con '{q}'",
            "resultados": []
        })

    return JSONResponse(status_code=200, content={
        "total": len(resultados),
        "resultados": resultados
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