from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .database import Base

# Models represent the tables in the database

class Cliente(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    limite = Column(Integer)
    saldo = Column(Integer)

    transacoes = relationship("Transacao", back_populates="cliente")

class Transacao(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer, ForeignKey("clients.id"))
    valor = Column(Integer)
    tipo = Column(String)
    descricao = Column(String)
    realizada_em = Column(DateTime, default=datetime.now())

    cliente = relationship("Cliente", back_populates="transacoes")