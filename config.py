import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # Database settings
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/pokedex"
    
    # API settings
    API_TITLE: str = "Pokédex API"
    API_VERSION: str = "1.0.0"
    DEBUG: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
