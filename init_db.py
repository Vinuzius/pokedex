# init_db.py
from sqlmodel import SQLModel
from database import engine  # Importa o engine que você configurou acima
# IMPORTANTE: Precisamos importar os modelos para que o SQLModel os registre no metadata
from models import Users, Locais, Materiais, Eventos, Evento_Materiais

def init_db():
    print("⏳ Criando tabelas no banco de dados (schema 'sh')...")
    SQLModel.metadata.create_all(engine)
    print("✅ Tabelas criadas com sucesso!")

if __name__ == "__main__":
    init_db()