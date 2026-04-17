from typing import Optional
from sqlmodel import SQLModel, Field

## Exemplo de ENUM
# class StatusEvento(StrEnum):
#     ongoing =  'em-andamento'
#     archived = 'arquivado'
#     receive = 'receber'

 

class Pokemon(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(max_length=255, unique=True)


    #### como fazer um enum, fk e relacionamento
    # status: StatusEvento = Field(
    #     sa_column=sa_Enum(StatusEvento, name="status_evento", create_type=False)
    # )
    # local_id: int = Field(foreign_key="locais.id")

    # local: "Locais" = Relationship(back_populates="eventoLocal")    
    # eventoMaterial: list["Evento_Materiais"] = Relationship(back_populates="evento")

