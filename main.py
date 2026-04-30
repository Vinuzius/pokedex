from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select

from config import settings
from database import create_db_and_tables, engine
from models import *
from dtos import pokemon

# Create FastAPI app
app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    debug=settings.DEBUG,
)

def get_session():
    with Session(engine) as session:
        yield session
        pass


@app.on_event("startup")
def on_startup():
    """Create database tables on application startup"""
    create_db_and_tables()


# Retornar toda a lista de pokemons ou com filtro
@app.get("/pokemon")
def get_pokemons(
    status: str | None = None,
    name: str | None = None,
    session: Session = Depends(get_session)
):
    query = select(Pokemon)
    
    if status:
        query = query.where(Pokemon.status == status)
    if name:
        query = query.where(Pokemon.name.ilike(f"%{name}%"))  # case-insensitive search
    
    pokemons = session.exec(query).all()
    return pokemons

# Retorna um pokemon específico por id
## id vai ser um query param, para  opcional necessita de ' type | None'
@app.get("/pokemon/{id}", response_model = PokemonWithLocalRead) # response vai especificar o que deve retornar
def get_single_pokemon(id: int, session: Session = Depends(get_session)):
    pokemon = session.get(Pokemon, id)
    
    if not pokemon: 
        raise HTTPException(status_code=404, detail="Pokemon not found")
    
    return pokemon


#Atualizar status e local
@app.patch("/pokemon/{id}")
def update_pokemon(id: int, pokemon_update: PokemonUpdate, session: Session = Depends(get_session)):
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


# Listar todos os jogos 
@app.get("/game")
def get_game(session: Session = Depends(get_session)):
    game = session.exec(select(Game)).all()
    return game

# Listar todos detalhes de um jogo especifico
@app.get("/game/{id}", response_model=GameWithLocalRead)
def get_single_game(id: int, session: Session = Depends(get_session)):
    
    game = session.get(Game, id)

    if not game: 
        raise HTTPException(status_code=404, detail="Jogo não encontrado")

    return game

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )
