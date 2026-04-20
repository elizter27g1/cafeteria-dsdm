from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from db import db, siguiente_id

router = APIRouter()

# Modelos
class InsumoNuevo(BaseModel):
    nombre: str
    unidad: str
    cantidad: float
    minimo: float = 0

class AjusteInventario(BaseModel):
    cantidad: float
    motivo: str = None

@router.post("/", status_code=501)
def registrar_insumo(insumo: InsumoNuevo):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 4: implementen registro de insumo en Timebox 1"
    })

# ⨯ NO IMPLEMENTADO — Timebox 1
@router.patch("/{id}/descontar")
def descontar_insumo(id: int):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 4: implementar en Timebox 1 manualmente el descuento de insumo",
        "pista": "Valida que la cantidad a descontar no sea mayor a la cantidad actual"
    })

@router.get("/{id}/alerta_bajo_stock")
def alerta_bajo_stock(id: int):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 4: implementen alerta de bajo stock"
    })

# ⨯ NO IMPLEMENTADO — Timebox 2
@router.post("/{id}/entrada")
def entrada_insumo(id: int):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 4: Should Have — implementar en Timebox 2",
        "pista": "Similar al descontar pero sumando en vez de restar"
    })

# ⨯ NO IMPLEMENTADO — Could Have
@router.get("/{id}/historial")
def historial_insumo(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Could Have"})

@router.get("/compra_automatica")
def compra_automatica():
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Orden de compra automatica por bajo stock."})