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
    nome = Column(String, nullable=True)
    idade = Column(Integer, nullable=True)

Base.metadata.create_all(engine)

print("Tabela Criada com SQLite estabelecida.")

from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import sessionmaker
# assumindo que engine já foi criado

Session = sessionmaker(bind=engine)
session = Session()

try:
    with Session() as session:
        novo_usuario = Usuario(cadeira=40)
        session.add(novo_usuario)
        # O commit é feito automaticamente aqui, se não houver exceções
        # O rollback é automaticamente chamado se uma exceção ocorrer
        # A sessão é fechada automaticamente ao sair do bloco with
except TypeError as e:
    print(e)