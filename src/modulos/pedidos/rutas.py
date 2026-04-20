# src/modulos/pedidos/rutas.py
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from datetime import datetime
from db import db, siguiente_id

router = APIRouter()

ESTADOS_VALIDOS = ['pendiente', 'en_preparacion', 'listo', 'entregado']

# Modelos
class ProductoPedido(BaseModel):
    productoId: int
    nombre: str
    cantidad: int

class PedidoNuevo(BaseModel):
    productos: List[ProductoPedido]

class EstadoUpdate(BaseModel):
    estado: str

@router.post("/", status_code=501)
def crear_pedido(pedido: PedidoNuevo):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 3: implementen creación de pedido en Timebox 1",
        "pista": "Recuerden validar que cada producto exista y tenga stock suficiente"
    })

@router.get("/{id}")
def pedidos_pendientes():
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 3: implementen listado de pedidos pendientes en Timebox 1",
        "pista": "Solo deben devolver pedidos con estado 'pendiente' o 'en_preparacion'"
    })


@router.patch("/{id}/estado")
def actualizar_estado(id: int):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 3: ESTE ES SU MUST HAVE MAS IMPORTANTE",
        "estadosValidos": ESTADOS_VALIDOS
    })

@router.patch("/{id}/mesa")
def asignar_mesa(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", 
    "mensaje": "Equipo 3",
    "pista": "Recuerden validar que la mesa esté disponible"})

@router.patch("/{id}/cancelar")
def cancelar_pedido(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Equipo 3"})