from typing import Generator

from sqlmodel import SQLModel, create_engine
import os
from dotenv import load_dotenv

# Pega a URL do ambiente, com um valor padrão caso não encontre
load_dotenv()
postgresURL = os.environ.get("DATABASE_URL", "postgresql://user:pass@host/db")
if postgresURL == "postgresql://user:pass@host/db":
    print("AVISO: Variável DATABASE_URL não encontrada, usando valor padrão.")

# connect_args para mudar o schema que vai ser utilizado
engine = create_engine(postgresURL, connect_args={"options": "-c search_path=api"}) # , echo= True

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
