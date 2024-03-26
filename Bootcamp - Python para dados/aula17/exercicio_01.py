from sqlalchemy import create_engine

# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

## dialetos
## engine = create_engine("postgresql+psycopg2://scott:tiger@localhost:5432/mydatabase")


print("Conexão com SQLite estabelecida.")