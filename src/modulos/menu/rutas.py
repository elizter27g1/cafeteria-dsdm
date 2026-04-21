# src/modulos/menu/rutas.py
from pathlib import Path
import shutil
from uuid import uuid4

from fastapi import APIRouter, File, UploadFile
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
def cambiar_disponibilidad(id: int, data: DisponibilidadUpdate):
    producto = next((p for p in db["productos"] if p["id"] == id), None)

    if not producto:
        return JSONResponse(status_code=404, content={
            "error": "No encontrado",
            "mensaje": f"No existe un producto con id {id}"
        })

    producto["disponible"] = data.disponible

    return {
        "mensaje": "Disponibilidad actualizada",
        "producto": producto
    }

@router.get("/")
def listar_por_categoria(categoria: Optional[str] = None):
    productos = db["productos"]

    if categoria:
        categoria_normalizada = categoria.strip().lower()
        productos = [
            p for p in productos
            if p.get("categoria", "").strip().lower() == categoria_normalizada
        ]

    return {
        "total": len(productos),
        "categoria": categoria,
        "productos": productos
    }

@router.post("/agregar-imagen/{id}")
def agregar_imagen(id: int, imagen: UploadFile = File(...)):
    producto = next((p for p in db["productos"] if p["id"] == id), None)

    if not producto:
        return JSONResponse(status_code=404, content={
            "error": "No encontrado",
            "mensaje": f"No existe un producto con id {id}"
        })

    if not imagen.content_type or not imagen.content_type.startswith("image/"):
        return JSONResponse(status_code=400, content={
            "error": "Archivo inválido",
            "mensaje": "El archivo debe ser una imagen"
        })

    extension = Path(imagen.filename or "").suffix or ".jpg"
    nombre_archivo = f"producto_{id}_{uuid4().hex}{extension}"

    carpeta_uploads = Path(__file__).resolve().parents[2] / "uploads" / "productos"
    carpeta_uploads.mkdir(parents=True, exist_ok=True)

    ruta_destino = carpeta_uploads / nombre_archivo
    with ruta_destino.open("wb") as buffer:
        shutil.copyfileobj(imagen.file, buffer)

    producto["imagen"] = f"uploads/productos/{nombre_archivo}"

    return {
        "mensaje": "Imagen agregada correctamente",
        "producto": producto
    }
