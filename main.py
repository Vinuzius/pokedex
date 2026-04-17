from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import Session, select

from config import settings
from database import create_db_and_tables, get_session, engine
from models import Pokemon, PokemonCreate, PokemonUpdate, PokemonRead

# Create FastAPI app
app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION,
    debug=settings.DEBUG,
)


@app.on_event("startup")
def on_startup():
    """Create database tables on application startup"""
    create_db_and_tables()


# Health check endpoint
@app.get("/health", tags=["Health"])
def health_check():
    """Check API health status"""
    return {"status": "ok"}


# CRUD operations for Pokémon

@app.post("/pokemon", response_model=PokemonRead, tags=["Pokémon"])
def create_pokemon(
    pokemon: PokemonCreate,
    session: Session = Depends(get_session),
):
    """Create a new Pokémon"""
    db_pokemon = Pokemon.from_orm(pokemon)
    session.add(db_pokemon)
    session.commit()
    session.refresh(db_pokemon)
    return db_pokemon


@app.get("/pokemon", response_model=list[PokemonRead], tags=["Pokémon"])
def read_pokemon(
    skip: int = 0,
    limit: int = 10,
    session: Session = Depends(get_session),
):
    """Get all Pokémon with pagination"""
    pokemon = session.exec(
        select(Pokemon).offset(skip).limit(limit)
    ).all()
    return pokemon


@app.get("/pokemon/{pokemon_id}", response_model=PokemonRead, tags=["Pokémon"])
def read_pokemon_by_id(
    pokemon_id: int,
    session: Session = Depends(get_session),
):
    """Get a Pokémon by ID"""
    pokemon = session.get(Pokemon, pokemon_id)
    if not pokemon:
        raise HTTPException(
            status_code=404,
            detail=f"Pokémon with id {pokemon_id} not found",
        )
    return pokemon


@app.put("/pokemon/{pokemon_id}", response_model=PokemonRead, tags=["Pokémon"])
def update_pokemon(
    pokemon_id: int,
    pokemon_update: PokemonUpdate,
    session: Session = Depends(get_session),
):
    """Update a Pokémon by ID"""
    db_pokemon = session.get(Pokemon, pokemon_id)
    if not db_pokemon:
        raise HTTPException(
            status_code=404,
            detail=f"Pokémon with id {pokemon_id} not found",
        )
    
    pokemon_data = pokemon_update.dict(exclude_unset=True)
    db_pokemon.sqlmodel_update(pokemon_data)
    session.add(db_pokemon)
    session.commit()
    session.refresh(db_pokemon)
    return db_pokemon


@app.delete("/pokemon/{pokemon_id}", tags=["Pokémon"])
def delete_pokemon(
    pokemon_id: int,
    session: Session = Depends(get_session),
):
    """Delete a Pokémon by ID"""
    db_pokemon = session.get(Pokemon, pokemon_id)
    if not db_pokemon:
        raise HTTPException(
            status_code=404,
            detail=f"Pokémon with id {pokemon_id} not found",
        )
    
    session.delete(db_pokemon)
    session.commit()
    return {"deleted": True}


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )
