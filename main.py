from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine,Base
#from middlewares.error_handler import Errorhandler

from routers.routes import pullutants_router

app = FastAPI()

app.title = "Mi app para un inventario con FastAPI"
app.version = "0.0.1"

app.include_router(pullutants_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return HTMLResponse ('<h1>Se mostrarán indicadores de medición de la calidad del aire</h1>')