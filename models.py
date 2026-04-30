from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from enum import StrEnum
from sqlalchemy import Enum as sa_Enum

class StatusCaptura(StrEnum):
    coletado = "coletado"
    nao_coletado = "nao coletado"
    trocar = "trocar"
    evoluir = "evoluir"
    breed = "breed"
 

class PokemonLocal(SQLModel, table=True):
    id_local: Optional[int] = Field(default=None, foreign_key="local.id", primary_key=True)
    id_pokemon: Optional[int] = Field(default=None, foreign_key="pokemon.id", primary_key=True)
    descricao: str = Field(max_length=255)


class Pokemon(SQLModel, table=True):
    model_config = {"from_attributes": True}
    id: Optional[int] = Field(default=None, primary_key=True)
    numero_dex: int
    nome: str = Field(max_length=255, unique= True)
    status: StatusCaptura = Field(
        sa_column=sa_Enum(StatusCaptura, name="status_evento", create_type=False)
    )

    locais: list["Local"] = Relationship(back_populates="pokemons", link_model=PokemonLocal)


class Game(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(max_length=100, unique= True)
    geracao: int

    locais: list["Local"] = Relationship(back_populates="game")


class Local(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    id_game: int | None = Field(foreign_key="game.id")
    rota: str = Field(max_length=100)

    game: Game | None = Relationship(back_populates="locais")
    pokemons: list[Pokemon] = Relationship(back_populates="locais", link_model=PokemonLocal)




class LocalRead(SQLModel):
    id: int
    rota: str

class PokemonWithLocalRead(SQLModel):
    id: int
    numero_dex: int
    nome: str
    status: str
    locais: list[LocalRead] = [] # A mágica do aninhamento acontece aqui

class PokemonUpdate(SQLModel):
    status: StatusCaptura | None = None
    locais: list[int] | None = None  # list of local IDs

class GameWithLocalRead(SQLModel):
    id: int
    nome: str
    geracao: int
    locais: list[LocalRead] = []

