# Cafeteria DSDM — Proyecto Base

> **Proyecto académico** para práctica de DSDM con MoSCoW, Timeboxes y entrega incremental.
> Este proyecto está **incompleto intencionalmente**. Los equipos deben completarlo durante la práctica.

---
## EQUIPOS
1. MARCOS
2. ALAN ALEJANDRO
3. VILLEDO
4. EDWIN
5. UBALDO
6. JESUS ANDRE
7. JESUS ALEJANDRO
8. ERICK
9. GABRIEL

## Instrucciones de ejecución

### Requisitos previos
- Python versión 3.10 o superior
- Administrador de paquetes pip

### Pasos para correr el proyecto

```bash
# 1. Entrar a la carpeta del proyecto
cd cafeteria-dsdm

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Iniciar el servidor
python src/servidor.py
```

Si `requirements.txt.` no logra instalar las dependencias puedes utilizar los comandos:

```bash
pip install fastapi

```

El servidor estará disponible en: http://localhost:3000

La documentación interactiva (Swagger UI) está en: http://localhost:3000/docs


## 📁 Estructura del proyecto

```
cafeteria-dsdm/
│
├── requirements.txt         ← Dependencias (FastAPI, Uvicorn, Pydantic)
├── src/
│   ├── servidor.py          ← Servidor principal y registro de rutas
│   ├── db.py                ← Base de datos en memoria (datos compartidos)
│   │
│   └── modulos/
│       ├── menu/            ← Equipo 1 — Menú y Productos (parcial)
│       ├── ventas/          ← Equipo 2 — Punto de Venta (parcial)
│       ├── pedidos/         ← Equipo 3 — Gestión de Pedidos (parcial)
│       ├── inventario/      ← Equipo 4 — Inventario (parcial)
│       ├── clientes/        ← Equipo 5 — Clientes (parcial)
│       ├── reportes/        ← Equipo 6 — Reportes (parcial)
│       ├── empleados/       ← Equipo 7 — Empleados (parcial)
│       ├── reservaciones/   ← Equipo 8 — Reservaciones (parcial)
│       └── promociones/     ← Equipo 9 — Promociones (parcial)
```

---

## 📋 Estado de endpoints por módulo

Cada módulo utiliza Pydantic para la validación automática de datos. Si un endpoint responde 501, significa que el equipo debe implementarlo siguiendo las pistas en el código.

## 🧪 Cómo probar los endpoints

### Opción 1 — Desde el navegador (solo GET)
Entra a http://localhost:3000/docs. Podrás ver todos los esquemas de datos (Pydantic) y probar cada método directamente con el botón "Try it out".

### Opción 2 — Con curl (terminal)
```bash
# Ver productos
curl http://localhost:3000/api/menu/

# Crear producto (La validación es automática)
curl -X POST http://localhost:3000/api/menu/ \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Cafe americano","precio":20,"categoria":"bebida"}'
```

## ⚠️ Notas importantes para los estudiantes

1. **Los datos se reinician** los datos viven en db.py y se reinician al detener el servidor.
2. **Validación** FastAPI validará que envíes los tipos de datos correctos (ej. precio como número). Si falta un campo obligatorio, recibirás un error 422.
3. **Tu módulo** Trabaja exclusivamente en `src/modulos/TU_MODULO/rutas.py.`.
