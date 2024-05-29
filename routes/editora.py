from fastapi import APIRouter
from entidades import conn
from entidades import editoras
from schemas.editora import EditoraSchema

editoraRouter = APIRouter()

@editoraRouter.get("/")
async def read_all():
    result = conn.execute(editoras.select()).fetchall()
    return [dict(row._mapping) for row in result]

@editoraRouter.get("/{id}")
async def read_by_id(id: int):
    result = conn.execute(editoras.select().where(editoras.c.id == id)).fetchone()
    if result:
        return dict(result._mapping)
    return {"error": "Editora nao encontrada"}

@editoraRouter.post("/")
async def insert(editora: EditoraSchema):
    return conn.execute(editoras.insert().values(
        nome=editora.nome,
        cepEndereco=editora.cepEndereco
    ))

@editoraRouter.put("/{id}")
async def update(id: int, editora: EditoraSchema):
    result = conn.execute(editoras.update()
    .values(
        nome=editora.nome,
        cepEndereco=editora.cepEndereco
    ).where(editoras.c.id == id))
    if result.rowcount:
        return {"message": "Editora atualizada"}
    return {"error": "editora nao encontrada"}

@editoraRouter.delete("/{id}")
async def delete(id: int):
    result = conn.execute(editoras.delete().where(editoras.c.id == id))
    if result.rowcount:
        return {"message": "editora excluida com sucesso"}
    return {"error": "editora nao encontrada"}