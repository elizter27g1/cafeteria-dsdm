import os
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime, timedelta
from db import db, siguiente_id

# Importaciones de Google API
from google.oauth2 import service_account
from googleapiclient.discovery import build

router = APIRouter()

# Configuración de Google Calendar
SCOPES = ['https://www.googleapis.com/auth/calendar.events']
SERVICE_ACCOUNT_FILE = 'credentials.json'
CALENDAR_ID = 'dsdm-practica'

class ReservacionNueva(BaseModel):
    nombre: str
    fecha: str
    hora: str
    personas: int

# TIMEBOX 1
@router.post("/")
def registrar_reservacion(reserva: ReservacionNueva):
    nuevo_id = siguiente_id()
    nueva_reserva = {
        "id": nuevo_id,
        "nombre": reserva.nombre,
        "fecha": reserva.fecha,
        "hora": reserva.hora,
        "personas": reserva.personas,
        "cancelada": False,
        "link_calendario": None,
    }
    
    # Integración con Google Calendar
    enlace_evento = crear_evento_google(reserva, nuevo_id)
    if enlace_evento and not enlace_evento.startswith("Falta") and not "Error" in str(enlace_evento):
        nueva_reserva["link_calendario"] = enlace_evento

    db["reservaciones"].append(nueva_reserva)
    
    return {
        "mensaje": "Reservación registrada exitosamente",
        "reserva": nueva_reserva
    }

# TIMEBOX 2
@router.get("/hoy")
def reservaciones_hoy():
    hoy = datetime.now().strftime('%Y-%m-%d')
    reservas = [r for r in db["reservaciones"] if r["fecha"] == hoy and not r["cancelada"]]
    return sorted(reservas, key=lambda r: r["hora"])

# TIMEBOX 1
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

# TIMEBOX 2
@router.get("/disponibilidad")
def verificar_disponibilidad(fecha: str, hora: str):
    capacidad_maxima = 20 # Es la capacidad máxima de personas en el restaurante para esa fecha y hora
    reservas = [r for r in db["reservaciones"] if r["fecha"] == fecha and r["hora"] == hora and not r["cancelada"]]
    personas_reservadas = sum(r["personas"] for r in reservas)
    disponible = personas_reservadas < capacidad_maxima
    return {
        "disponible": disponible,
        "personas_reservadas": personas_reservadas,
        "capacidad_maxima": capacidad_maxima
    }

# TIMEBOX 3
def obtener_servicio_calendario():
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        return None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    return build('calendar', 'v3', credentials=creds)

# TIMEBOX 3
class ReservacionNueva(BaseModel):
    nombre: str
    fecha: str # Formato esperado: YYYY-MM-DD
    hora: str  # Formato esperado: HH:MM
    personas: int

# TIMEBOX 3
def crear_evento_google(reserva: ReservacionNueva, id_reserva: int):
    servicio = obtener_servicio_calendario()
    if not servicio:
        return "Falta el archivo credentials.json"

    # Preparar fechas y horas 
    inicio_str = f"{reserva.fecha}T{reserva.hora}:00"
    inicio_dt = datetime.strptime(inicio_str, "%Y-%m-%dT%H:%M:%S")
    fin_dt = inicio_dt + timedelta(hours=1)
    
    evento = {
        'summary': f'Reservación: {reserva.nombre}',
        'description': f'Mesa para {reserva.personas} personas. ID Reservación local: {id_reserva}',
        'start': {
            'dateTime': inicio_dt.isoformat(),
            'timeZone': 'America/Chihuahua', 
        },
        'end': {
            'dateTime': fin_dt.isoformat(),
            'timeZone': 'America/Chihuahua',
        },
    }

    try:
        evento_creado = servicio.events().insert(calendarId=CALENDAR_ID, body=evento).execute()
        return evento_creado.get('htmlLink')
    except Exception as e:
        return str(e)

# TIMEBOX 3    
@router.get("/google-calendar")
def integracion_google_calendar():
    servicio = obtener_servicio_calendario()
    if servicio:
        return {"estado": "Conectado", "mensaje": "La integración con Google Calendar está activa y configurada."}
    else:
        return JSONResponse(status_code=503, content={
            "estado": "Desconectado", 
            "error": "Archivo credentials.json no encontrado. Verifica la configuración de la Cuenta de Servicio."
        })