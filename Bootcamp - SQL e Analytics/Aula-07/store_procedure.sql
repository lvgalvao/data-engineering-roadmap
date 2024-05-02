CREATE OR REPLACE PROCEDURE ver_extrato(
    IN p_cliente_id INTEGER
)
LANGUAGE plpgsql
AS $$
DECLARE
    saldo_atual INTEGER;
    transacao RECORD;
    contador INTEGER := 0;
BEGIN
    -- Obtém o saldo atual do cliente
    SELECT saldo INTO saldo_atual
    FROM clients
    WHERE id = p_cliente_id;

    -- Retorna o saldo atual do cliente
    RAISE NOTICE 'Saldo atual do cliente: %', saldo_atual;

    -- Retorna as 10 últimas transações do cliente
    RAISE NOTICE 'Últimas 10 transações do cliente:';
    FOR transacao IN
        SELECT *
        FROM transactions
        WHERE cliente_id = p_cliente_id
        ORDER BY realizada_em DESC
        LIMIT 10
    LOOP
        contador := contador + 1;
        RAISE NOTICE 'ID: %, Tipo: %, Descrição: %, Valor: %, Data: %', transacao.id, transacao.tipo, transacao.descricao, transacao.valor, transacao.realizada_em;
        EXIT WHEN contador >= 10;
    END LOOP;
END;
$$;
