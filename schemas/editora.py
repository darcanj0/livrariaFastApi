from pydantic import BaseModel

class EditoraSchema(BaseModel):
    nome: str
    cepEndereco: int