from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Serviço de Agendamento e Presença")

app.include_router(router)
