from pydantic import BaseModel

class AutorSchema(BaseModel):
    nome: str
    anoNascimento: int
    anoFalecimento: int