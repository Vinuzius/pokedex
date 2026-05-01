# DTOs package
from dtos.pokemonDTO import PokemonRead, PokemonWithLocalRead, PokemonUpdate, StatusCaptura
from dtos.localDTO import LocalRead, LocalWithPokemonRead
from dtos.gameDTO import GameWithLocalRead
from dtos.encounterDTO import EncounterPost
from dtos.statisticsDTO import CompletionStats, StatusCount

__all__ = [
    "PokemonRead",
    "PokemonWithLocalRead",
    "PokemonUpdate",
    "StatusCaptura",
    "LocalRead",
    "LocalWithPokemonRead",
    "GameWithLocalRead",
    "EncounterPost",
    "CompletionStats",
    "StatusCount",
]
