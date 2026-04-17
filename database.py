from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session
from typing import Generator

from config import settings

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # Set to True to see SQL queries
    future=True,
)


def create_db_and_tables():
    """Create database tables"""
    SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
    """Get database session for dependency injection"""
    with Session(engine) as session:
        yield session
