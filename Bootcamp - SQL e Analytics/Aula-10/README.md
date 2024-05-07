## Transação

### O que é uma transação?

- Uma coleção de "queries"
- Uma unidade de trabalho
Muitas vezes precisamos mais de uma "querie" para querer o que queremos
ex: para fazer uma transação financeira, precisamos selecionar uma conta e verificar se ela possui o dnheiro (SELECT), fazer a remoção do dinheiro da conta que irá transferir o dinheiro (UPDATE) e fazer o incremento do dinheiro na conta alvo (UPDATE). Tudo isso precisa estar dentro da mesma transação.
- Toda transação inicia com um BEGIN
- Toda transação finaliza com um COMMIT (em memória)
- Toda transação, pode falhar, precisa de um ROLLBACK 
- Normalmente transações são usadas para MODIFICAR dados, mas é possível ter uma transação com somente leitura , exemplo: você quer gerar um relatório e quer que esses dados sejam confiáveis e ter uma SNAPSHOT daquela cenário

## Atomicidade

- Uma transação tem que ser "indivisivel"
- Ou seja, todas as "queries" em uma transação precisam ter sucesso
- Exemplo: se não existir a segunda pessoa, se você não tiver 100 reais, se cair a luz no meio dessa transação, etc. Ela volta para o estado anterior e nada acontece.

```sql
-- Criar tabela
CREATE TABLE exemplo (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50)
);

-- Inserir dados
INSERT INTO exemplo (nome) VALUES ('A'), ('B'), ('C');

SELECT * FROM exemplo
```

Read comitted:
```

exemplo 1 t1
```
BEGIN;
SELECT nome, count(nome) FROM exemplo
GROUP by nome

exemplo 1 t2
```
BEGIN;
INSERT INTO exemplo (nome) VALUES ('A');
COMMIT;
```

exemplo 1 t1
```sql
SELECT nome FROM exemplo;
```


Como evitar isso?

exemplo 1 t1
```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN;
SELECT nome, count(nome) FROM exemplo
GROUP by nome;
SELECT * FROM exemplo;
COMMIT;
```

exemplo 2 t2
```
BEGIN;
INSERT INTO exemplo (nome) VALUES ('A');
COMMIT;
```

-- Configuração para Serializable
```sql
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
SELECT * FROM exemplo;

-- Configuração para Serializable
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN;
SELECT * FROM exemplo;

-- Voltar pro T1
INSERT INTO exemplo (nome) VALUES ('A');
COMMIT;

-- Voltar pro T2
INSERT INTO exemplo (nome) VALUES ('A');
COMMIT;