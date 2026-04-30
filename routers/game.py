# Game routes

from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select

from models import Game
from dtos.game import GameWithLocalRead
from dependencies import get_session

router = APIRouter(prefix="/game", tags=["game"])


@router.get("", response_model=list[Game])
def get_game(session: Session = Depends(get_session)):
    """List all games"""
    game = session.exec(select(Game)).all()
    return game


@router.get("/{id}", response_model=GameWithLocalRead)
def get_single_game(id: int, session: Session = Depends(get_session)):
    """Get details of a specific game"""
    game = session.get(Game, id)

    if not game: 
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    return game
