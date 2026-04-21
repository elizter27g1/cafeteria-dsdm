# src/modulos/pedidos/rutas.py
from fastapi import APIRouter, HTTPException, HTTPException
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

@router.post("/", status_code=201)
def crear_pedido(pedido: PedidoNuevo):
    for prod_solicitado in pedido.productos:
        producto_db = next((p for p in db["productos"] if p["id"] == prod_solicitado.productoId), None)
        
        if not producto_db:
            raise HTTPException(status_code=404, detail=f"Producto ID {prod_solicitado.productoId} no encontrado")
        
        if not producto_db["disponible"]:
            raise HTTPException(status_code=400, detail=f"El producto '{producto_db['nombre']}' no está disponible actualmente")

    nuevo_id = siguiente_id("pedidos")
    nuevo_pedido = {
        "id": nuevo_id,
        "productos": [p.model_dump() for p in pedido.productos],
        "estado": "pendiente",
        "mesa": None,
        "motivoCancelacion": None,
        "creadoEn": datetime.now().isoformat() 
    }

    db["pedidos"].append(nuevo_pedido)

    return {
        "mensaje": "Pedido creado con éxito",
        "pedido": nuevo_pedido
    }

@router.get("/pendientes") 
def pedidos_pendientes():
    estados_activos = ['pendiente', 'en_preparacion']
    lista_pendientes = [p for p in db["pedidos"] if p["estado"] in estados_activos]

    lista_pendientes.sort(key=lambda x: x["creadoEn"])

    return lista_pendientes


@router.patch("/{id}/estado")
def actualizar_estado(id: int, update: EstadoUpdate):
    if update.estado not in ESTADOS_VALIDOS:
        raise HTTPException(
            status_code=400, 
            detail=f"Estado inválido. Use: {ESTADOS_VALIDOS}"
        )

    pedido = next((p for p in db["pedidos"] if p["id"] == id), None)
    
    if not pedido:
        raise HTTPException(status_code=404, detail=f"Pedido con ID {id} no encontrado")

    pedido["estado"] = update.estado

    return {
        "mensaje": f"Estado del pedido {id} actualizado a '{update.estado}'",
        "pedido": pedido
    }

@router.patch("/{id}/mesa")
def asignar_mesa(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", 
    "mensaje": "Equipo 3",
    "pista": "Recuerden validar que la mesa esté disponible"})

@router.patch("/{id}/cancelar")
def cancelar_pedido(id: int):
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Equipo 3"})