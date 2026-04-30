from fastapi import FastAPI

from config import settings
from database import create_db_and_tables
from routers import pokemon, local, game

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


# Include routers
app.include_router(pokemon.router)
app.include_router(local.router)
app.include_router(game.router)


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
    )
