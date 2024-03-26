from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional

class Livro(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    titulo: str
    autor: str
    ano_publicacao: int
    disponivel: bool = True

# Conexão com o banco de dados (SQLite para simplicidade)
engine = create_engine("sqlite:///biblioteca.db")

# Criação da tabela
SQLModel.metadata.create_all(engine)

def adicionar_livro(livro: Livro):
    with Session(engine) as session:
        session.add(livro)
        session.commit()

def buscar_livros_por_autor(autor: str):
    with Session(engine) as session:
        livros = session.exec(select(Livro).where(Livro.autor == autor)).all()
        return livros

def atualizar_disponibilidade_livro(id_livro: int, disponivel: bool):
    with Session(engine) as session:
        livro = session.get(Livro, id_livro)
        livro.disponivel = disponivel
        session.add(livro)
        session.commit()

def remover_livro(id_livro: int):
    with Session(engine) as session:
        livro = session.get(Livro, id_livro)
        session.delete(livro)
        session.commit()

# Demonstração
if __name__ == "__main__":
    adicionar_livro(Livro(titulo="Dom Casmurro", autor="Machado de Assis", ano_publicacao=1899))
    adicionar_livro(Livro(titulo="O Pequeno Príncipe", autor="Antoine de Saint-Exupéry", ano_publicacao=1943))

    print("Livros de Machado de Assis:", buscar_livros_por_autor("Machado de Assis"))
    atualizar_disponibilidade_livro(1, False)  # Supondo que o ID do "Dom Casmurro" seja 1
    remover_livro(2)  # Supondo que o ID de "O Pequeno Príncipe" seja 2
