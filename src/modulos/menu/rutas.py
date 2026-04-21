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
    disponible: bool

class DisponibilidadUpdate(BaseModel):
    disponible: bool
# ───────────────────────────────────────────────────────

# IMPLEMENTADO
@router.post("/", status_code=201)
def registrar_producto(producto: ProductoNuevo):
    nuevo_id = siguiente_id('productos')
    nuevo_producto = {
        'id': nuevo_id,
        'nombre': producto.nombre,
        'precio': producto.precio,
        'categoria': producto.categoria,
        'disponible': producto.disponible
    }
    db['productos'].append(nuevo_producto)
    return {
        'mensaje': 'Producto registrado exitosamente',
        'producto': nuevo_producto
    }


# IMPLEMENTADO
@router.put("/{id}", status_code=200)
def editar_producto(id: int, producto: ProductoNuevo):
    for p in db['productos']:
        if p['id'] == id:
            p['nombre'] = producto.nombre
            p['precio'] = producto.precio
            p['categoria'] = producto.categoria
            p['disponible'] = producto.disponible
            return {
                'mensaje': 'Producto editado exitosamente',
                'producto': p
            }
    return JSONResponse(status_code=404, content={
        'error': 'Producto no encontrado'
    })
    

# IMPLEMENTADO
@router.delete("/{id}", status_code=200)
def eliminar_producto(id: int):
    for p in db['productos']:
        if p['id'] == id:
            db['productos'].remove(p)
            return {
                'mensaje': 'Producto eliminado exitosamente'
            }
    return JSONResponse(status_code=404, content={
        'error': 'Producto no encontrado'
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