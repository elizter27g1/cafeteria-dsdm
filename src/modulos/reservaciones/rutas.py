import json

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

@router.post("/")
def registrar_reservacion(reserva: ReservacionNueva):
    try:

        nuevo_id = siguiente_id("reservaciones")

        nueva_entrada = {
            "id": nuevo_id,
            "nombre": reserva.nombre,
            "fecha": reserva.fecha,
            "hora": reserva.hora,
            "personas": reserva.personas,
            "cancelada": False
        }
        
        db["reservaciones"].append(nueva_entrada)
        
        return {
            "status": "éxito", 
            "mensaje": "La reserva se guardó correctamente.",
            "total": len(db["reservaciones"])
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": "Error interno", "detalle": str(e)})

@router.get("/hoy")
def reservaciones_hoy():
    hoy = datetime.now().strftime('%Y-%m-%d')
    reservas = [r for r in db["reservaciones"] if r["fecha"] == hoy and not r["cancelada"]]
    return sorted(reservas, key=lambda r: r["hora"])

@router.patch("/{id}")
def cancelar_reservacion(id: int):
    try:
        for r in db["reservaciones"]:
            if r["id"] == id:                
                if r["cancelada"]:
                    return {"mensaje": f"La reservación {id} ya había sido cancelada previamente."}                
                r["cancelada"] = True
                
                return {
                    "status": "éxito",
                    "mensaje": f"La reservación de {r['nombre']} (ID: {id}) ha sido cancelada."
                }                
        return JSONResponse(status_code=404, content={"error": "No encontrada"})

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": "Error interno", "detalle": str(e)})

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
        "mensaje": "Equipo 8: Could Have — integración con Google Calendar  "
    })