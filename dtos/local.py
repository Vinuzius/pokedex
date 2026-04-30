# Local DTOs - used to ensure correct data in endpoints

from sqlmodel import SQLModel
from dtos.pokemon import PokemonRead


class LocalRead(SQLModel):
    id: int
    rota: str


class LocalWithPokemonRead(LocalRead):
    pokemons: list[PokemonRead] = []
