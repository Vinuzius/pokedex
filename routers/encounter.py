# Encounter routes

from fastapi import APIRouter, HTTPException, Depends, Response
from sqlmodel import Session

from models import Pokemon, Local, PokemonLocal
from dtos.encounterDTO import *
from dependencies import get_session

router = APIRouter(prefix="/encounter", tags=["encounter"])


@router.post("", response_model=EncounterPost)
def link_encounter(
    encounter_in: EncounterPost,
    session: Session = Depends(get_session)
):
    """Link a pokemon to a location (create an encounter)"""
    # Validate if local and pokemon exist
    pokemon_existe = session.get(Pokemon, encounter_in.id_pokemon)
    local_existe = session.get(Local, encounter_in.id_local)
    
    if not pokemon_existe or not local_existe:
        raise HTTPException(
            status_code=404, 
            detail="Pokémon ou Local não encontrado."
        )
    
    # Verify if this encounter already exists
    encontro_existe = session.get(PokemonLocal, (encounter_in.id_local, encounter_in.id_pokemon))
    if encontro_existe:
        raise HTTPException(
            status_code=409,
            detail="Este Pokémon já está registrado neste Local."
        )
    
    # Create new encounter
    new_encounter = PokemonLocal(
        id_pokemon=encounter_in.id_pokemon,
        id_local=encounter_in.id_local,
        descricao=encounter_in.descricao
    )
    
    session.add(new_encounter)
    session.commit()
    session.refresh(new_encounter)
    
    return new_encounter


@router.delete("/{id_local}/{id_pokemon}")
def delete_encounter(
    id_pokemon: int,
    id_local: int,
    session: Session = Depends(get_session)):
    """Delete an encounter between a pokemon and a location"""
    enc = session.get(PokemonLocal, (id_local, id_pokemon))
    if not enc:
        raise HTTPException(status_code=404, detail="Este encontro não existe")
    
    session.delete(enc)
    session.commit()
    return Response(status_code=204)
