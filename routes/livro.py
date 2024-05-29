from fastapi import APIRouter
from entidades import conn
from entidades import livros
from schemas.livro import LivroSchema

livroRouter = APIRouter()

@livroRouter.get("/")
async def read_all():
    result = conn.execute(livros.select()).fetchall()
    return [dict(row._mapping) for row in result]

@livroRouter.get("/{id}")
async def read_by_id(id: int):
    result = conn.execute(livros.select().where(livros.c.id == id)).fetchone()
    if result:
        return dict(result._mapping)
    return {"error": "Livro nao encontrado"}

@livroRouter.post("/")
async def insert(livro: LivroSchema):
    return conn.execute(livros.insert().values(
        titulo=livro.titulo,
        anoPublicacao=livro.anoPublicacao,
        editoraId=livro.editoraId,
        autorId=livro.autorId
    ))

@livroRouter.put("/{id}")
async def update(id: int, livro: LivroSchema):
    result = conn.execute(livros.update()
    .values(
        titulo=livro.titulo,
        anoPublicacao=livro.anoPublicacao,
        editoraId=livro.editoraId,
        autorId=livro.autorId
    ).where(livros.c.id == id))
    if result.rowcount:
        return {"message": "Livro atualizado"}
    return {"error": "livro nao encontrado"}

@livroRouter.delete("/{id}")
async def delete(id: int):
    result = conn.execute(livros.delete().where(livros.c.id == id))
    if result.rowcount:
        return {"message": "livro excluido com sucesso"}
    return {"error": "livro nao encontrado"}