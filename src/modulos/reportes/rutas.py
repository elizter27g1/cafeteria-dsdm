from fastapi import APIRouter
from fastapi.responses import JSONResponse
from datetime import datetime
from typing import Optional
from db import db

router = APIRouter()

def es_hoy(fecha_str):
    try:
        fecha_obj = datetime.fromisoformat(fecha_str.replace('Z', '+00:00'))
        return fecha_obj.date() == datetime.now().date()
    except Exception:
        return False

# ✓ IMPLEMENTADO (Must Have)
@router.get("/hoy/total")
def total_hoy():
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 6: implementen total de ventas de hoy en Timebox 1",
        "pista": "Filtra db['ventas'] con la funcion es_hoy(v['fecha']) que ya esta definida, luego suma el total de cada venta"
    })

# ⨯ NO IMPLEMENTADO — Timebox 1
@router.get("/hoy/ventas")
def ventas_hoy():
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 6: Must Have — implementar en Timebox 1",
        "pista": "Filtra db['ventas'] con la funcion es_hoy(v['fecha']) que ya esta definida"
    })

# ⨯ NO IMPLEMENTADO — Timebox 1
@router.get("/hoy/top")
def top_hoy():
    return JSONResponse(status_code=501, content={
        "error": "No implementado",
        "mensaje": "Equipo 6: Must Have",
        "algoritmo": ["1. Filtrar ventas de hoy", "2. Recorrer items", "3. Acumular", "4. Ordenar"]
    })

# ⨯ NO IMPLEMENTADO — Timebox 2
@router.get("/rango")
def ventas_rango(inicio: str, fin: str):
    # Nota como FastAPI te pedira ?inicio=X&fin=Y obligatoriamente
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 2"})

# ⨯ NO IMPLEMENTADO — Could Have
@router.get("/hoy/grafica")
def grafica_hoy():
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Could Have"})