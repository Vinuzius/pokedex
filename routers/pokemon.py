# Pokemon routes

from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select

from models import Pokemon, Local
from dtos.pokemon import PokemonRead, PokemonWithLocalRead, PokemonUpdate
from dependencies import get_session

router = APIRouter(prefix="/pokemon", tags=["pokemon"])


@router.get("", response_model=list[PokemonRead])
def get_pokemons(
    status: str | None = None,
    name: str | None = None,
    session: Session = Depends(get_session)
):
    """Get all pokemons or filter by status and/or name"""
    query = select(Pokemon)
    
    if status:
        query = query.where(Pokemon.status == status)
    if name:
        query = query.where(Pokemon.nome.ilike(f"%{name}%"))  # case-insensitive search
    
    pokemons = session.exec(query).all()
    return pokemons


@router.get("/{id}", response_model=PokemonWithLocalRead)
def get_single_pokemon(id: int, session: Session = Depends(get_session)):
    """Get a specific pokemon by ID"""
    pokemon = session.get(Pokemon, id)
    
    if not pokemon: 
        raise HTTPException(status_code=404, detail="Pokemon not found")
    
    return pokemon


@router.patch("/{id}", response_model=PokemonWithLocalRead)
def update_pokemon(id: int, pokemon_update: PokemonUpdate, session: Session = Depends(get_session)):
    """Update pokemon status and locais"""
    pokemon = session.get(Pokemon, id)

    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokemon not found")
    
    if pokemon_update.status:
        pokemon.status = pokemon_update.status
    
    if pokemon_update.locais is not None:
        for local_id in pokemon_update.locais:
            local = session.get(Local, local_id)
            if local and (local not in pokemon.locais):  # avoid duplicates
                pokemon.locais.append(local)
    
    session.add(pokemon)
    session.commit()
    session.refresh(pokemon)
    return pokemon
