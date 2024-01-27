-- Exemplo com dados valido

INSERT INTO vendas (email, data, valor, produto, quantidade, categoria)
VALUES (
    'comprador@example.com', 
    '2023-09-15 12:00:00',  -- Substitua pela data atual formatada como string
    100.50, 
    'Produto X', 
    3, 
    'categoria3'
);

-- Exemplo com dado invalido

INSERT INTO vendas (email, data, valor, produto, quantidade, categoria)
VALUES (
    'comprador', 
    '2023-09-15 12:00:00',  -- Substitua pela data atual formatada como string
    100.50, 
    'Produto X', 
    3, 
    'categoria3'
);