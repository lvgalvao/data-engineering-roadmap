@app.post("/clientes/{cliente_id}/transacoes", response_model=schemas.ClienteResponse)
async def post_transacao(cliente_id: int, 
                         transacao: schemas.TransactionCreateRequest, 
                         session: AsyncSession = Depends(get_session)):
    
    result = await session.execute(" CALL realizar_transacao(transacao.type, transacao.description, transacao.value, cliente_id)")

    return cliente