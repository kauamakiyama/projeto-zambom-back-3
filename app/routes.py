from fastapi import APIRouter, HTTPException
from .crud import criar_aula, listar_aulas, inscrever_usuario, registrar_presenca
from .schemas import AulaCreate, AulaResponse, Inscricao, Presenca

router = APIRouter()

@router.post("/aulas/", response_model=AulaResponse)
async def create_aula(aula: AulaCreate):
    aula_dict = aula.dict()
    aula_dict["inscritos"] = []
    aula_dict["presencas"] = []
    aula_id = await criar_aula(aula_dict)
    return AulaResponse(id=aula_id, **aula_dict)

@router.get("/aulas/", response_model=list[AulaResponse])
async def get_aulas():
    return await listar_aulas()

@router.post("/aulas/{aula_id}/inscrever")
async def inscrever(aula_id: str, inscricao: Inscricao):
    sucesso = await inscrever_usuario(aula_id, inscricao.usuario_id)
    if not sucesso:
        raise HTTPException(status_code=400, detail="Turma cheia ou não encontrada")
    return {"msg": "Usuário inscrito"}

@router.post("/aulas/{aula_id}/presenca")
async def presenca(aula_id: str, presenca: Presenca):
    await registrar_presenca(aula_id, presenca.usuario_id)
    return {"msg": "Presença registrada"}
