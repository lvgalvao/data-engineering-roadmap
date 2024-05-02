CREATE OR REPLACE PROCEDURE realizar_transacao(
    IN p_tipo CHAR(1),
    IN p_descricao VARCHAR(10),
    IN p_valor INTEGER,
    IN p_cliente_id INTEGER
)
LANGUAGE plpgsql
AS $$
DECLARE
    saldo_atual INTEGER;
    limite_cliente INTEGER;
BEGIN
    -- Obtém o saldo atual e o limite do cliente
    SELECT saldo, limite INTO saldo_atual, limite_cliente
    FROM clients
    WHERE id = p_cliente_id;

    -- Verifica se a transação é válida com base no saldo e no limite
    IF p_tipo = 'd' AND saldo_atual - p_valor < -limite_cliente THEN
        RAISE EXCEPTION 'Saldo insuficiente para realizar a transação';
    END IF;

    -- Atualiza o saldo do cliente
    UPDATE clients
    SET saldo = saldo + CASE WHEN p_tipo = 'd' THEN -p_valor ELSE p_valor END
    WHERE id = p_cliente_id;

    -- Insere uma nova transação
    INSERT INTO transactions (tipo, descricao, valor, cliente_id)
    VALUES (p_tipo, p_descricao, p_valor, p_cliente_id);
END;
$$;