from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão com SQLite estabelecida.")

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)

Base.metadata.create_all(engine)

print("Tabela Criada com SQLite estabelecida.")

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

print("Usuário inserido com sucesso.")

usuarios = session.query(Usuario).all()

for usuario in usuarios:
    print(f"ID: {usuario.id}, Nome: {usuario.nome}")