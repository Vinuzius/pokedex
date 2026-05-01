# Game DTOs - used to ensure correct data in endpoints

from sqlmodel import SQLModel
from dtos.localDTO import LocalRead


class GameWithLocalRead(SQLModel):
    id: int
    nome: str
    geracao: int
    locais: list[LocalRead] = []
