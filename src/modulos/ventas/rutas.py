from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from db import db, siguiente_id

router = APIRouter()

# Modelos
class ItemVenta(BaseModel):
    productoId: int
    nombre: str
    precio: float
    cantidad: int = 1

class VentaNueva(BaseModel):
    items: List[ItemVenta]
    metodoPago: str = Field(..., description='Debe ser "efectivo" o "tarjeta"')

class DescuentoUpdate(BaseModel):
    porcentaje: float

# ✓ IMPLEMENTADO (Must Have)
@router.get("/")
def seleccionar_para_ticket():
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 2: implementen productos para un ticket de venta en Timebox 1",
        "pista": "Devolver el nombre, precio y cantidad de cada producto seleccionado"
    })


# ✓ IMPLEMENTADO (Must Have)
@router.post("/{id}/calcular-total")
def calcular_total(id: int, venta: VentaNueva):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 2: implementen registro de venta en Timebox 1",
        "pista": "Recuerden calcular el total sumando precio * cantidad de cada item"
    })


@router.post("/{id}/metodo-pago")
def registrar_metodo_pago(id: int, metodo_pago: str):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 2: implementen actualización de método de pago en Timebox 1",
        "pista": "Recuerden validar que el método de pago sea 'efectivo' o 'tarjeta'"
    })

# ⨯ NO IMPLEMENTADO — Timebox 2
@router.patch("/{id}/descuento")
def aplicar_descuento(id: int):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 2: implementen descuento en Timebox 2",
        "pista": "Ojo: guarda el total original antes de descontarlo, o no podras revertirlo"
    })

# ⨯ NO IMPLEMENTADO — Could Have
@router.patch("/{id}/folio")
def generar_folio(id: int):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 2: implementen generación de folio en Timebox 3",
        "pista": 'Folio sugerido: f"F-{venta_id:04d}"'
    })