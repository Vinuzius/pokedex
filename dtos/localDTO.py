# Local DTOs - used to ensure correct data in endpoints

from __future__ import annotations
from sqlmodel import SQLModel
from dtos.pokemonDTO import PokemonRead


class LocalRead(SQLModel):
    id: int
    rota: str


class LocalWithPokemonRead(LocalRead):
    pokemons: list[PokemonRead] = []
