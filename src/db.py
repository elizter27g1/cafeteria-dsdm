# src/db.py

db = {
    "productos": [
        {"id": 1, "nombre": "Tacos de canasta", "precio": 15, "categoria": "comida", "disponible": True},
        {"id": 2, "nombre": "Agua fresca", "precio": 12, "categoria": "bebida", "disponible": True},
        {"id": 3, "nombre": "Sandwich mixto", "precio": 35, "categoria": "comida", "disponible": False},
    ],
    "ventas": [
        {
            "id": 1,
            "items": [{"productoId": 1, "nombre": "Tacos de canasta", "precio": 15, "cantidad": 2}],
            "total": 30,
            "metodoPago": "efectivo",
            "descuento": 0,
            "folio": None,
            "fecha": "2025-01-15T10:30:00"
        }
    ],
    "pedidos": [
        {
            "id": 1,
            "productos": [{"productoId": 2, "nombre": "Agua fresca", "cantidad": 1}],
            "estado": "pendiente",
            "mesa": None,
            "motivoCancelacion": None,
            "creadoEn": "2025-01-15T10:25:00"
        }
    ],
    "insumos": [
        {"id": 1, "nombre": "Tortillas", "unidad": "piezas", "cantidad": 200, "minimo": 50},
        {"id": 2, "nombre": "Azucar", "unidad": "kg", "cantidad": 5, "minimo": 10},
        {"id": 3, "nombre": "Cafe molido", "unidad": "kg", "cantidad": 2, "minimo": 1},
    ],
    "clientes": [
        {"id": 1, "nombre": "Maria Lopez", "telefono": "6561234567", "correo": "maria@mail.com", "visitas": 5, "puntos": 0}
    ],
    "empleados": [
        {"id": 1, "nombre": "Juan Perez", "rol": "cajero", "turno": "matutino", "activo": True}
    ],
    "reservaciones": [
        {"id": 1, "nombre": "Familia Ramirez", "fecha": "2025-01-16", "hora": "14:00", "personas": 4, "cancelada": False}
    ],
    "promociones": [
        {"id": 1, "nombre": "2x1 en bebidas", "tipo": "porcentaje", "descuento": 50, "vigenciaHasta": "2025-12-31T23:59:59", "activa": True, "codigoCupon": None}
    ],
    "_contadores": {
        "productos": 3, "ventas": 1, "pedidos": 1, "insumos": 3, 
        "clientes": 1, "empleados": 1, "reservaciones": 1, "promociones": 1
    }
}

def siguiente_id(coleccion):
    if coleccion not in db["_contadores"]:
        db["_contadores"][coleccion] = 0
    db["_contadores"][coleccion] += 1
    return db["_contadores"][coleccion]