import uvicorn
from fastapi import FastAPI
from modulos.clientes.rutas import router as clientes_router
from db import db

app = FastAPI()

app.include_router(clientes_router, prefix="/api/clientes", tags=["Clientes"])

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3000)