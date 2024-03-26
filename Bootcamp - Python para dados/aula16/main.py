from typing import Optional

from sqlmodel import Field, Session, SQLModel, create_engine

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

engine = create_engine("sqlite:///database.db", echo=True)

SQLModel.metadata.create_all(engine)

hero_1 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_2 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.commit()