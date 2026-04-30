# Local routes

from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select

from models import Local
from dtos.local import LocalRead, LocalWithPokemonRead
from dependencies import get_session

router = APIRouter(tags=["local"])


@router.get("/local/", response_model=list[LocalRead])
def get_local(
    game_id: int | None = None,
    session: Session = Depends(get_session)
):
    """Get all locais or filter by game_id"""
    query = select(Local)

    if game_id:
        query = query.where(Local.id_game == game_id)

    locais = session.exec(query).all()
    return locais


@router.post("/local/", response_model=LocalRead)
def create_local(new_local: Local, session: Session = Depends(get_session)):
    """Create a new local in a game"""
    # Verify if local already exists
    query_verificacao = select(Local).where(
        Local.id_game == new_local.id_game,
        Local.rota == new_local.rota
    )
    local_existente = session.exec(query_verificacao).first()
    if local_existente:
        raise HTTPException(
            status_code=409,
            detail=f"A '{new_local.rota}' já está cadastrada para o jogo de ID {new_local.id_game}."
        )
    
    # If it doesn't exist, can be added
    session.add(new_local)
    session.commit()
    session.refresh(new_local)
    
    return new_local


@router.get("/locations/{local_id}/pokemons", response_model=LocalWithPokemonRead)
def show_local_pokemon(local_id: int, session: Session = Depends(get_session)):
    """Show all pokemons in a specific location"""
    local = session.get(Local, local_id)
    
    if not local: 
        raise HTTPException(status_code=404, detail="Local not found")

    return local
