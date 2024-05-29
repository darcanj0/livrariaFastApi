from pydantic import BaseModel

class LivroSchema(BaseModel):
    titulo: str
    anoPublicacao: int
    editoraId: int
    autorId: int