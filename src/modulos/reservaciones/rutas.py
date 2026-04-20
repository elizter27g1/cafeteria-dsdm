from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime
from db import db, siguiente_id

router = APIRouter()

class ReservacionNueva(BaseModel):
    nombre: str
    fecha: str
    hora: str
    personas: int

@router.post("/", status_code=501)
def registrar_reservacion(reserva: ReservacionNueva):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 1"})

@router.get("/hoy")
def reservaciones_hoy():
    hoy = datetime.now().strftime('%Y-%m-%d')
    reservas = [r for r in db["reservaciones"] if r["fecha"] == hoy and not r["cancelada"]]
    return sorted(reservas, key=lambda r: r["hora"])

@router.delete("/{id}")
def cancelar_reservacion(id: int):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 8: Must Have — implementar en Timebox 1",
        "pista": "Puedes marcar r['cancelada'] = True."
    })

@router.get("/disponibilidad")
def verificar_disponibilidad(fecha: str, hora: str):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 8: Should Have — implementar en Timebox 2"
    })

@router.get("/google-calendar")
def integracion_google_calendar():
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 8: Could Have — integración con Google Calendar"
    })