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
    ventas = [v for v in db["ventas"] if es_hoy(v["fecha"])]

    total = 0
    registros = []

    for i, v in enumerate(ventas, start=1):
        monto = v.get("total", 0)
        total += monto
        registros.append({
            "venta": i,
            "monto": monto
        })

    fecha_hoy = datetime.now().strftime("%Y-%m-%d")

    return {
        "titulo": "Reporte de Ventas",
        "fecha": fecha_hoy,
        "registros": registros,
        "total": total
    }


@router.get("/hoy/ventas")
def ventas_hoy():
    ventas = [v for v in db["ventas"] if es_hoy(v["fecha"])]

    registros = []

    for v in ventas:
        fecha_obj = datetime.fromisoformat(v["fecha"])

        fecha = fecha_obj.strftime("%Y-%m-%d")
        hora = fecha_obj.strftime("%H:%M")

        # sacar nombres de productos (pueden venir varios)
        productos = ", ".join([item["nombre"] for item in v.get("items", [])])

        registros.append({
            "producto": productos,
            "fecha": fecha,
            "hora": hora,
            "total": v.get("total", 0)
        })

    return {
        "titulo": "Lista de Ventas",
        "fecha": datetime.now().strftime("%Y-%m-%d"),
        "registros": registros
    }


# ⨯ NO IMPLEMENTADO — Timebox 1
@router.get("/hoy/top")
def top_hoy():
    # 1. Filtrar ventas de hoy
    ventas = [v for v in db["ventas"] if es_hoy(v["fecha"])]

    # 2. Acumular productos
    contador = {}

    for v in ventas:
        for item in v.get("items", []):
            nombre = item.get("nombre")
            cantidad = item.get("cantidad", 0)

            if nombre not in contador:
                contador[nombre] = 0

            contador[nombre] += cantidad

    # 3. Ordenar de mayor a menor
    top = sorted(contador.items(), key=lambda x: x[1], reverse=True)

    # 4. Formato de salida
    return {
        "titulo": "Mas vendidos",

        "top_productos": [
            {
                "producto": nombre,
                "cantidad_vendida": cantidad
            }
            for nombre, cantidad in top
        ]
    }

# ⨯ NO IMPLEMENTADO — Timebox 2
@router.get("/rango")
def ventas_rango(inicio: str, fin: str):
    # Nota como FastAPI te pedira ?inicio=X&fin=Y obligatoriamente
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Timebox 2"})

# ⨯ NO IMPLEMENTADO — Could Have
@router.get("/hoy/grafica")
def grafica_hoy():
    return JSONResponse(status_code=501, content={"error": "No implementado", "mensaje": "Could Have"})