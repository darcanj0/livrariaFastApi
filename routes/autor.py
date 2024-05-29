from fastapi import APIRouter
from entidades import conn
from entidades import autores
from schemas.autor import AutorSchema

autorRouter = APIRouter()

@autorRouter.get("/")
async def read_all():
    result = conn.execute(autores.select()).fetchall()
    return [dict(row._mapping) for row in result]

@autorRouter.get("/{id}")
async def read_by_id(id: int):
    result = conn.execute(autores.select().where(autores.c.id == id)).fetchone()
    if result:
        return dict(result._mapping)
    return {"error": "Autor nao encontrado"}

@autorRouter.post("/")
async def insert(autor: AutorSchema):
    return conn.execute(autores.insert().values(
        nome=autor.nome,
        anoNascimento=autor.anoNascimento,
        anoFalecimento=autor.anoFalecimento
    ))

@autorRouter.put("/{id}")
async def update(id: int, autor: AutorSchema):
    result = conn.execute(autores.update()
    .values(
        nome=autor.nome,
        anoNascimento=autor.anoNascimento,
        anoFalecimento=autor.anoFalecimento
    ).where(autores.c.id == id))
    if result.rowcount:
        return {"message": "Autor atualizado"}
    return {"error": "autor nao encontrado"}

@autorRouter.delete("/{id}")
async def delete(id: int):
    result = conn.execute(autores.delete().where(autores.c.id == id))
    if result.rowcount:
        return {"message": "autor excluido com sucesso"}
    return {"error": "autor nao encontrado"}