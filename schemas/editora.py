from pydantic import BaseModel

class EditoraSchema(BaseModel):
    id: int
    nome: str
    cepEndereco: int