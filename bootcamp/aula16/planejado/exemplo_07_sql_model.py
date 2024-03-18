from datetime import date
from sqlalchemy import create_engine, Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, EmailStr
from typing import List

# Definição do modelo SQLAlchemy
Base = declarative_base()

class VendaModel(Base):
    __tablename__ = 'vendas'
    id = Column(Integer, primary_key=True)
    produto = Column(String)
    valor = Column(Float)
    quantidade = Column(Integer)
    data = Column(Date)
    email_comprador = Column(String)

# Configuração do banco de dados SQLAlchemy
engine = create_engine('sqlite:///vendas.db', echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Modelos Pydantic
class VendaBase(BaseModel):
    produto: str
    valor: int  # Garante que o valor seja maior que 0
    quantidade: int
    data: date
    email_comprador: EmailStr

class VendaCreate(VendaBase):
    pass

class Venda(VendaBase):
    id: int

    class Config:
        from_attributes=True

# Funções para interagir com o banco de dados
def create_venda(db: Session, venda: VendaCreate) -> VendaModel:
    db_venda = VendaModel(**venda.model_dump())
    db.add(db_venda)
    db.commit()
    db.refresh(db_venda)
    return db_venda

def get_vendas(db: Session, skip: int = 0, limit: int = 100) -> List[VendaModel]:
    return db.query(VendaModel).offset(skip).limit(limit).all()

# Uso dos modelos e interação com o banco de dados
if __name__ == "__main__":
    db = SessionLocal()

    # Criando uma nova venda
    # venda_data = {
    #     "produto": "Notebook Ultra",
    #     "valor": 4500.00,
    #     "quantidade": 1,
    #     "data": date.today(),
    #     "email_comprador": "comprador@example.com"
    # }
    # nova_venda = VendaCreate(**venda_data)
    # venda_criada = create_venda(db=db, venda=nova_venda)
    # print(f"Venda criada: {venda_criada}")

    # Recuperando vendas
    vendas = get_vendas(db=db)
    print("Vendas recuperadas:")
    for venda_model in vendas:
        # Deserializando para o modelo Pydantic
        venda_pydantic = Venda.from_orm(venda_model)
        print(venda_pydantic)