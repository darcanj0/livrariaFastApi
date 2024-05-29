from pydantic import BaseModel

class LivroSchema(BaseModel):
    id: int
    titulo: str
    anoPublicacao: int
    editoraId: int
    autorId: int