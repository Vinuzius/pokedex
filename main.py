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

def get_session():
    with Session(engine) as session:
        yield session
        pass


@app.on_event("startup")
def on_startup():
    """Create database tables on application startup"""
    create_db_and_tables()



### exemplos pra se basear
# @app.get("/materiais")
# def get_materiais(session: Session = Depends(get_session)):
#     materiais = session.exec(select(Materiais)).all()
#     return materiais

# @app.post("/materiais", response_model= Materiais) # response vai falar o que deve retornar
# def create_material(material: Materiais, Session: Session = Depends(get_session)):
#     Session.add(material)
#     Session.commit()
#     Session.refresh(material)
#     return material

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
