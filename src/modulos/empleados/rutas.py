from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from db import db, siguiente_id
from datetime import datetime

router = APIRouter()

registro_asistencia = {}

class EmpleadoNuevo(BaseModel):
    nombre: str
    rol: str
    turno: str

# Registrar empleado
@router.post("/")
def registrar_empleado(empleado: EmpleadoNuevo):
    nuevo = {
        "id": siguiente_id("empleados"),
        "nombre": empleado.nombre,
        "rol": empleado.rol,
        "turno": empleado.turno,
        "activo": True
    }
    db["empleados"].append(nuevo)
    return JSONResponse(status_code=201, content=nuevo)

# Ver lista de empleados activos
@router.get("/")
def listar_empleados():
    activos = [e for e in db["empleados"] if e["activo"]]
    return JSONResponse(status_code=200, content=activos)

# Registrar entrada del turno
@router.post("/{id}/entrada")
def registrar_entrada(id: int):
    for e in db["empleados"]:
        if e["id"] == id:
            ahora = datetime.now().isoformat()
            if id not in registro_asistencia:
                registro_asistencia[id] = []
            registro_asistencia[id].append({"entrada": ahora, "salida": None})
            return JSONResponse(status_code=200, content={
                "mensaje": "Entrada registrada",
                "empleadoId": id,
                "entrada": ahora
            })
    return JSONResponse(status_code=404, content={"error": "Empleado no encontrado"})

# Registrar salida del turno
@router.post("/{id}/salida")
def registrar_salida(id: int):
    for e in db["empleados"]:
        if e["id"] == id:
            turnos = registro_asistencia.get(id, [])
            for turno in reversed(turnos):
                if turno["salida"] is None:
                    turno["salida"] = datetime.now().isoformat()
                    return JSONResponse(status_code=200, content={
                        "mensaje": "Salida registrada",
                        "empleadoId": id,
                        "entrada": turno["entrada"],
                        "salida": turno["salida"]
                    })
            return JSONResponse(status_code=400, content={"error": "No hay entrada registrada"})
    return JSONResponse(status_code=404, content={"error": "Empleado no encontrado"})

# ── Sin implementar (otros timeboxes) ──

@router.get("/{id}")
def ver_empleado(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 1"})

@router.put("/{id}")
def editar_empleado(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 2"})

@router.patch("/{id}/desactivar")
def desactivar_empleado(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 2"})

@router.get("/{id}/asistencia")
def historial_asistencia(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Could Have"})

@router.get("/{id}/horas-trabajadas")
def horas_trabajadas(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Could Have"})