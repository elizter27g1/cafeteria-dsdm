from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from db import db, siguiente_id

router = APIRouter()

class EmpleadoNuevo(BaseModel):
    nombre: str
    rol: str
    turno: str

@router.post("/")
def registrar_empleado(empleado: EmpleadoNuevo):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 1"})

@router.get("/{id}")
def ver_empleado(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 1"})

@router.post("/{id}/entrada")
def registrar_entrada(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 1"})

@router.post("/{id}/salida")
def registrar_salida(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 1"})

@router.put("/{id}")
def editar_empleado(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 2"})

@router.patch("/{id}/desactivar")
def desactivar_empleado(id: int):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 7: Should Have — Timebox 2",
        "pista": "empleado['activo'] = False"
    })

@router.get("/{id}/asistencia")
def historial_asistencia(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Could Have"})

@router.get("/{id}/horas-trabajadas")
def horas_trabajadas(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Could Have"}) 