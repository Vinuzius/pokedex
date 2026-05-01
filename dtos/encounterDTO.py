# Encounter DTOs

from sqlmodel import SQLModel


class EncounterPost(SQLModel):
    id_pokemon: int
    id_local: int
    descricao: str | None = None
