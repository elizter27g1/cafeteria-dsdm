# src/servidor.py
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

# Importar los blueprints (routers)
from modulos.menu.rutas import router as menu_router
from modulos.ventas.rutas import router as ventas_router
from modulos.pedidos.rutas import router as pedidos_router
from modulos.inventario.rutas import router as inventario_router
from modulos.clientes.rutas import router as clientes_router
from modulos.reportes.rutas import router as reportes_router
from modulos.empleados.rutas import router as empleados_router
from modulos.reservaciones.rutas import router as reservaciones_router
from modulos.promociones.rutas import router as promociones_router

app = FastAPI(
    title="Cafetería DSDM API",
    description="Proyecto académico DSDM. Completa los endpoints de tu equipo.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(menu_router, prefix="/api/menu", tags=["Equipo 1 - Menú"])
app.include_router(ventas_router, prefix="/api/ventas", tags=["Equipo 2 - Ventas"])
app.include_router(pedidos_router, prefix="/api/pedidos", tags=["Equipo 3 - Pedidos"])
app.include_router(inventario_router, prefix="/api/inventario", tags=["Equipo 4 - Inventario"])
app.include_router(clientes_router, prefix="/api/clientes", tags=["Equipo 5 - Clientes"])
app.include_router(reportes_router, prefix="/api/reportes", tags=["Equipo 6 - Reportes"])
app.include_router(empleados_router, prefix="/api/empleados", tags=["Equipo 7 - Empleados"])
app.include_router(reservaciones_router, prefix="/api/reservaciones", tags=["Equipo 8 - Reservaciones"])
app.include_router(promociones_router, prefix="/api/promociones", tags=["Equipo 9 - Promociones"])

# Ruta raiz
@app.get("/", tags=["Estado del Sistema"])
def index():
    return {
        "sistema": "Cafeteria DSDM",
        "version": "1.0.0-base (FastAPI)",
        "estado": "funcionando (incompleto)",
        "nota": "Ve a /docs para probar los endpoints interactivos."
    }

if __name__ == "__main__":
    print("\n✅ Servidor FastAPI corriendo en http://localhost:3000")
    print("📖 Swagger UI (Pruebas) disponible en http://localhost:3000/docs\n")
    uvicorn.run("servidor:app", host="0.0.0.0", port=3000, reload=True)