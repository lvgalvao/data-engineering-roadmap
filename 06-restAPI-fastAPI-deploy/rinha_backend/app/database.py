from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# URL de conexão assíncrona para PostgreSQL, ajuste conforme necessário
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://admin:123@db/rinha"

# Criar um engine assíncrono
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

# Configurar sessionmaker para criar sessões assíncronas
async_session_local = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession  # Isso especifica que a sessão deve ser assíncrona
)

Base = declarative_base()
