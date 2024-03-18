CREATE TABLE produtos_bronze_email (
    id_produto SERIAL PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    quantidade INT NOT NULL,
    preco FLOAT NOT NULL,
    categoria VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);
