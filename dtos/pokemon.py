# usado para garantir que vai ter os dados certos no ednpoint

from sqlmodel import Field, SQLModel

class PokemonCreate(SQLModel):
    nome: str = Field(max_length=255)
    endereco: str

class PokemonPublic(SQLModel):
    id: int
    nome: str = Field(max_length=255)
    endereco: str


class LocalRead(SQLModel):
    id: int
    rota: str

# Molde do Pokemon que avisa o FastAPI para incluir a lista de locais
class PokemonComLocaisRead(SQLModel):
    id: int
    numero_dex: int
    nome: str
    status: str
    locais: list[LocalRead] = [] # A mágica do aninhamento acontece aqui