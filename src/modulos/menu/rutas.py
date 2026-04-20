# src/modulos/menu/rutas.py
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from db import db, siguiente_id

router = APIRouter()

# ─── MODELOS DE DATOS (Pydantic) ───────────────────────
# Esto le dice a FastAPI qué datos debe exigir en un POST/PUT
# y se documenta automáticamente en Swagger UI.
class ProductoNuevo(BaseModel):
    nombre: str
    precio: float
    categoria: str

class DisponibilidadUpdate(BaseModel):
    disponible: bool
# ───────────────────────────────────────────────────────

# ⨯ NO IMPLEMENTADO
@router.post("/")
def registrar_producto(producto: ProductoNuevo):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 1: implementen registro de producto en Timebox 1",
        "pista": "Recuerden validar los datos antes de registrar el producto"
    })


# ⨯ NO IMPLEMENTADO — Timebox 1
@router.put("/{id}")
def editar_producto(id: int):
    # Nota como el id ya es int automáticamente
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 1: implementen este endpoint en el Timebox 1",
        "pista": "Usa db['productos'] para actualizar el producto."
    })

# ⨯ NO IMPLEMENTADO — Timebox 1
@router.delete("/{id}")
def eliminar_producto(id: int):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 1: implementen este endpoint en el Timebox 1"
    })

# ⨯ NO IMPLEMENTADO — Timebox 2
@router.patch("/{id}/disponibilidad")
def cambiar_disponibilidad(id: int):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 1: implementen este endpoint en el Timebox 2",
        "pista": "Recibe un JSON con {'disponible': true/false}"
    })

@router.get("/{id}")
def listar_por_categoria(categoria: Optional[str] = None):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 1: implementen este endpoint en el Timebox 2",
        "pista": "Si se recibe una categoría, filtra los productos por esa categoría"
    })

@router.post("/agregar-imagen/{id}")
def agregar_imagen(id: int):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 1: implementen este endpoint en el Timebox 3",
        "pista": "Recibe un archivo de imagen y guárdalo en el producto correspondiente"
    })

@router.get("/exportar-pdf")
def exportar_PDF_menu():
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 1: implementen este endpoint en el Timebox 3",
        "pista": "Genera un PDF del menu completo con los productos y sus detalles"
    })