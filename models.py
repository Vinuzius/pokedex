from typing import Optional
from sqlmodel import SQLModel, Field


class PokemonBase(SQLModel):
    """Base Pokémon model with shared fields"""
    name: str = Field(index=True)
    type: str
    hp: int
    attack: int
    defense: int


class Pokemon(PokemonBase, table=True):
    """Pokémon model for database"""
    __tablename__ = "pokemon"
    
    id: Optional[int] = Field(default=None, primary_key=True)


class PokemonCreate(PokemonBase):
    """Schema for creating a Pokémon"""
    pass


class PokemonUpdate(SQLModel):
    """Schema for updating a Pokémon"""
    name: Optional[str] = None
    type: Optional[str] = None
    hp: Optional[int] = None
    attack: Optional[int] = None
    defense: Optional[int] = None


class PokemonRead(PokemonBase):
    """Schema for reading a Pokémon"""
    id: int
