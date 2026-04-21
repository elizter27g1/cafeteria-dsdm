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
    nuevo_id = siguiente_id("promociones")
    
    # Extraemos los datos del modelo
    datos = promo.model_dump() if hasattr(promo, 'model_dump') else promo.dict()
    

    nueva_promo = {
        "id": nuevo_id,
        "nombre": datos["nombre"],
        "tipo": datos["tipo"],
        "descuento": datos["descuento"],
        "vigenciaHasta": datos["vigenciaHasta"],
        "activa": True,
        "codigoCupon": None,
        "usos": 0 
    }
    
    db["promociones"].append(nueva_promo)
    respuesta = nueva_promo.copy()
    respuesta["estado"] = esta_activa(respuesta)
    
    return JSONResponse(status_code=201, content=respuesta)

@router.post("/{id}/aplicar")
def aplicar_promocion(id: int, venta: VentaAplicar):
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 9: Must Have mas logico — Timebox 1 o 2",
        "pista": "Usa venta.totalVenta para calcular el descuento"
    })


@router.get("/lista_promociones")
def listar_promociones():
    lista_final = []
    
    for promo in db["promociones"]:
        # Reconstruimos el diccionario para forzar el orden visual en todos los registros
        promo_ordenada = {
            "id": promo.get("id"),
            "nombre": promo.get("nombre"),
            "tipo": promo.get("tipo"),
            "descuento": promo.get("descuento"),
            "vigenciaHasta": promo.get("vigenciaHasta"),
            "activa": promo.get("activa"),
            "codigoCupon": promo.get("codigoCupon")
        }
        
        promo_ordenada["estado"] = esta_activa(promo_ordenada)
        
        lista_final.append(promo_ordenada)
        
    return JSONResponse(status_code=200, content=lista_final)

@router.patch("/{id}/desactivar")
def desactivar_promocion(id: int):
    for promo in db["promociones"]:
        if promo.get("id") == id:
            promo["activa"] = False
            
            respuesta = {
                "id": promo.get("id"),
                "nombre": promo.get("nombre"),
                "tipo": promo.get("tipo"),
                "descuento": promo.get("descuento"),
                "vigenciaHasta": promo.get("vigenciaHasta"),
                "activa": promo.get("activa"),
                "codigoCupon": promo.get("codigoCupon"),
                "estado": esta_activa(promo)
            }
            return {"mensaje": "Promocion desactivada con exito", "promocion": respuesta}
            
    return JSONResponse(status_code=404, content={"error": "Promocion no encontrada"})

@router.get("/analisis_promociones")
def analisis_promociones():
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 9: Could Have — análisis de efectividad de promociones"
    })