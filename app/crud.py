from .database import db

async def criar_aula(aula: dict):
    result = await db.aulas.insert_one(aula)
    return str(result.inserted_id)

async def listar_aulas():
    aulas = await db.aulas.find().to_list(100)
    for aula in aulas:
        aula["id"] = str(aula["_id"])
        del aula["_id"]
    return aulas

async def inscrever_usuario(aula_id: str, usuario_id: str):
    aula = await db.aulas.find_one({"_id": aula_id})
    if aula and len(aula["inscritos"]) < aula["limite_vagas"]:
        await db.aulas.update_one(
            {"_id": aula_id},
            {"$addToSet": {"inscritos": usuario_id}}
        )
        return True
    return False

async def registrar_presenca(aula_id: str, usuario_id: str):
    await db.aulas.update_one(
        {"_id": aula_id},
        {"$addToSet": {"presencas": usuario_id}}
    )
