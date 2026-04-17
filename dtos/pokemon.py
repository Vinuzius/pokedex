# usado para garantir que vai ter os dados certos no ednpoint

from sqlmodel import Field, SQLModel

class PokemonCreate(SQLModel):
    nome: str = Field(max_length=255)
    endereco: str

class PokemonPublic(SQLModel):
    id: int
    nome: str = Field(max_length=255)
    endereco: str