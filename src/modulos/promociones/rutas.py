from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime
from db import db, siguiente_id

router = APIRouter()

class PromocionNueva(BaseModel):
    nombre: str
    tipo: str  # "porcentaje" o "monto_fijo"
    descuento: float
    vigenciaHasta: str

class VentaAplicar(BaseModel):
    totalVenta: float

def esta_activa(promo):
    if not promo.get("activa"):
        return False
    try:
        vigencia = datetime.fromisoformat(promo["vigenciaHasta"].replace('Z', '+00:00'))
        return vigencia >= datetime.now()
    except Exception:
        return False


@router.post("/")
def crear_promocion(promo: PromocionNueva):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 1"})

@router.post("/{id}/aplicar")
def aplicar_promocion(id: int, venta: VentaAplicar):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 9: Must Have mas logico — Timebox 1 o 2",
        "pista": "Usa venta.totalVenta para calcular el descuento"
    })

@router.get("/lista_promociones")
def listar_promociones():
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 9: primer Must Have — Timebox 1",
        "pista": "Agrega un campo 'estado' a cada diccionario usando la funcion esta_activa()"
    })

@router.post("/{id}/cupon")
def generar_cupon(id: int):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 9: Should Have — Timebox 2",
        "pista": "Genera un string random alfanumerico (libreria string y random de Python)"
    })

@router.patch("/{id}/desactivar")
def desactivar_promocion(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 2"})

@router.get("/analisis_promociones")
def analisis_promociones():
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 9: Could Have — análisis de efectividad de promociones"
    })