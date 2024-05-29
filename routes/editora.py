from fastapi import APIRouter
from entidades import conn
from entidades import editoras
from schemas.editora import EditoraSchema

editoraRouter = APIRouter()

editoraRouter.get("/")
async def read_all():
    return conn.execute(editoras.select()).fetchall()

editoraRouter.get("/{id}")
async def read_by_id(id: int):
    return conn.execute(editoras.select().where(editoras.c.id == id)).fetchall()

editoraRouter.post("/")
async def inseert(editora: EditoraSchema):
    return conn.execute(editoras.insert().values(
        nome=editora.nome,
        cepEndereco=editora.cepEndereco
    ))

editoraRouter.put("/{id}")
async def update(id: int, editora: EditoraSchema):
    return conn.execute(editoras.update()
    .values(
        nome=editora.nome,
        cepEndereco=editora.cepEndereco
    ).where(editoras.c.id == id)).fetchall()

editoraRouter.delete("/{id}")
async def delete(id: int):
    return conn.execute(editoras.delete().where(editoras.c.id == id)).fetchall()