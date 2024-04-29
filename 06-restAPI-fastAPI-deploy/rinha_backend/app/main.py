import time

from fastapi import FastAPI, HTTPException, Response
from fastapi.params import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from . import schemas
from .database import async_session_local
from .models import Cliente, Transacao

app = FastAPI()

async def get_session():
    async with async_session_local() as session:
        yield session


@app.post("/clientes/{cliente_id}/transacoes", response_model=schemas.ClienteResponse)
async def post_transacao(cliente_id: int, 
                         transacao: schemas.TransactionCreateRequest, 
                         session: AsyncSession = Depends(get_session)):
    
    result = await session.execute(select(Cliente).filter_by(id=cliente_id))
    cliente = result.scalars().one_or_none()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    if transacao.tipo == "d":
        if cliente.saldo - transacao.valor < -cliente.limite:
            raise HTTPException(status_code=422, detail="Saldo insuficiente")
        cliente.saldo -= transacao.valor
    else:  # ou seja do tipo == "c"
        cliente.saldo += transacao.valor

    nova_transacao = Transacao(**transacao.model_dump(), cliente_id=cliente_id)
    session.add(nova_transacao)
    await session.commit()
    await session.refresh(cliente)

    return cliente


@app.get("/clientes/{cliente_id}/extrato")
async def get_extrato(cliente_id: int, session: AsyncSession = Depends(get_session)):
    # Obtém o cliente de forma assíncrona usando select e scalars
    result = await session.execute(select(Cliente).filter_by(id=cliente_id))
    client = result.scalars().one_or_none()

    if not client:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    # Executa a consulta para obter as últimas transações de forma assíncrona
    transactions_result = await session.execute(
        select(Transacao)
        .where(Transacao.cliente_id == cliente_id)
        .order_by(Transacao.id.desc())
        .limit(10)
    )
    transactions = transactions_result.scalars().all()

    return {
        "saldo": {
            "total": client.saldo,
            "data_extrato": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()),
            "limite": client.limite
        },
        "ultimas_transacoes": [
            t for t in transactions
        ]
    }

@app.delete("/clientes/{cliente_id}", status_code=204)
async def delete_cliente(cliente_id: int, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Cliente).filter_by(id=cliente_id))
    cliente = result.scalars().one_or_none()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    await session.delete(cliente)
    await session.commit()
    return Response(status_code=204)

@app.put("/clientes/{cliente_id}", response_model=schemas.ClienteResponse)
async def update_cliente(cliente_id: int, update_data: schemas.ClientCreateRequest, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Cliente).filter_by(id=cliente_id))
    cliente = result.scalars().one_or_none()

    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")

    for var, value in update_data.model_dump(exclude_unset=True).items():
        setattr(cliente, var, value)

    await session.commit()
    await session.refresh(cliente)
    return cliente

@app.post("/clientes/", response_model=schemas.ClienteResponse, status_code=201)
async def create_cliente(cliente_data: schemas.ClientCreateRequest, 
                         session: AsyncSession = Depends(get_session)):
    
    novo_cliente = Cliente(
        saldo=cliente_data.saldo,
        limite=cliente_data.limite
    )
    session.add(novo_cliente)
    await session.commit()
    await session.refresh(novo_cliente)
    return novo_cliente