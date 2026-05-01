# Pokemon DTOs - used to ensure correct data in endpoints

from sqlmodel import Field, SQLModel
from models import StatusCaptura


class LocalRead(SQLModel):
    id: int
    rota: str


class PokemonRead(SQLModel):
    id: int
    numero_dex: int
    nome: str
    status: str


class PokemonWithLocalRead(SQLModel):
    id: int
    numero_dex: int
    nome: str
    status: str
    locais: list[LocalRead] = []


class PokemonUpdate(SQLModel):
    status: StatusCaptura | None = None
    locais: list[int] | None = None  # list of local IDs
