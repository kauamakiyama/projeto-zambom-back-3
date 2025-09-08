from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class AulaCreate(BaseModel):
    nome: str = Field(..., example="Boxe")
    horario: datetime = Field(..., example="2025-09-10T19:00:00")
    limite_vagas: int = Field(..., example=20)

class AulaResponse(AulaCreate):
    id: str
    inscritos: List[str] = []
    presencas: List[str] = []

class Inscricao(BaseModel):
    usuario_id: str

class Presenca(BaseModel):
    usuario_id: str
