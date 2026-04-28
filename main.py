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


# Retornar toda a lista
@app.get("/pokemon")
def get_pokemons(session: Session = Depends(get_session)):
    pokemons = session.exec(select(Pokemon)).all()
    return pokemons

# Retorna um pokemon específico por id
## id vai ser um query param, para  opcional necessita de ' int | None'
@app.get("/pokemons/{id}", response_model = PokemonComLocaisRead) # response vai especificar o que deve retornar
def get_single_pokemon(id: int, session: Session = Depends(get_session)):
    pokemon = session.get(Pokemon, id)
    
    if not pokemon: 
        raise HTTPException(status_code=404, detail="Pokemon not found")
    
    return pokemon



# @app.post("/locais", response_model= LocalPublic)
# def create_local(local: LocalCreate, session: Session = Depends(get_session)):
#     loc = Locais.model_validate(local)
#     session.add(loc)
#     session.commit()
#     session.refresh(loc)
#     return loc


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )
