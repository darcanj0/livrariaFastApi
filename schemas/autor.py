from pydantic import BaseModel

class AutorSchema(BaseModel):
    id: int
    nome: str
    anoNascimento: int
    anoFalecimento: int