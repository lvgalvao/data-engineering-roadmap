CREATE TABLE vendas (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    data TIMESTAMP NOT NULL,
    valor NUMERIC(10, 2) NOT NULL CHECK (valor >= 0),
    quantidade INTEGER NOT NULL CHECK (quantidade >= 0),
    produto VARCHAR(255) NOT NULL,
    categoria VARCHAR(50) NOT NULL
);