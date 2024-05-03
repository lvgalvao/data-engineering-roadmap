## Aula 09 - Triggers (Gatilhos) e Projeto Prático II

Papars recomendados https://github.com/rxin/db-readings?tab=readme-ov-file

## O que sâo Triggers?

#### 1. O que são Triggers

* **Definição**: Triggers são procedimentos armazenados, que são automaticamente executados ou disparados quando eventos específicos ocorrem em uma tabela ou visão.
* **Funcionamento**: Eles são executados em resposta a eventos como INSERT, UPDATE ou DELETE.

#### 2. Por que usamos Triggers em projetos

* **Automatização de tarefas**: Para realizar ações automáticas que são necessárias após modificações na base de dados, como manutenção de logs ou atualização de tabelas relacionadas.
* **Integridade de dados**: Garantir a consistência e a validação de dados ao aplicar regras de negócio diretamente no banco de dados.

#### 3. Origem e finalidade da criação dos Triggers

* **História**: Os triggers foram criados para oferecer uma maneira de responder automaticamente a eventos de modificação em bancos de dados, permitindo a execução de procedimentos de forma automática e transparente.
* **Problemas resolvidos**: Antes dos triggers, muitas dessas tarefas precisavam ser controladas manualmente no código da aplicação, o que poderia levar a erros e inconsistências.

1. **Tabela Funcionario**:
    
    * Armazena os dados dos funcionários, incluindo ID, nome, salário e data de contratação.
2. **Tabela Funcionario_Auditoria**:
    
    * Armazena o histórico de alterações dos salários dos funcionários, incluindo o salário antigo, o novo salário e a data da modificação.

```sql
-- Criação da tabela Funcionario
CREATE TABLE Funcionario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    salario DECIMAL(10, 2),
    dtcontratacao DATE
);

-- Criação da tabela Funcionario_Auditoria
CREATE TABLE Funcionario_Auditoria (
    id INT,
    salario_antigo DECIMAL(10, 2),
    novo_salario DECIMAL(10, 2),
    data_de_modificacao_do_salario TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id) REFERENCES Funcionario(id)
);

-- Inserção de dados na tabela Funcionario
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('Maria', 5000.00, '2021-06-01');
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('João', 4500.00, '2021-07-15');
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('Ana', 4000.00, '2022-01-10');
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('Pedro', 5500.00, '2022-03-20');
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('Lucas', 4700.00, '2022-05-25');
```

### Criação do Trigger

O trigger `trg_salario_modificado` será disparado após uma atualização no salário na tabela `Funcionario`. Ele registrará os detalhes da modificação na tabela `Funcionario_Auditoria`.

```sql
-- Criação do Trigger para auditoria de alterações de salário
CREATE OR REPLACE FUNCTION registrar_auditoria_salario() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO Funcionario_Auditoria (id, salario_antigo, novo_salario)
    VALUES (OLD.id, OLD.salario, NEW.salario);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_salario_modificado
AFTER UPDATE OF salario ON Funcionario
FOR EACH ROW
EXECUTE FUNCTION registrar_auditoria_salario();
```

Esse exemplo cria uma infraestrutura completa para monitorar as alterações de salário, garantindo que qualquer ajuste seja devidamente registrado, oferecendo uma trilha de auditoria clara e útil para análises futuras.

Para verificar se o trigger está funcionando corretamente, podemos realizar um comando `UPDATE` no salário de um dos funcionários e, em seguida, consultar a tabela `Funcionario_Auditoria` para ver se a alteração foi registrada conforme esperado. Vamos fazer isso com o funcionário cujo nome é "Ana".

### Comando de Atualização do Salário

```sql
-- Atualiza o salário da Ana
UPDATE Funcionario SET salario = 4300.00 WHERE nome = 'Ana';
```

### Consulta à Tabela de Auditoria

Após realizar a atualização, podemos verificar a tabela `Funcionario_Auditoria` para garantir que o registro da mudança de salário foi feito.

```sql
-- Consulta à tabela Funcionario_Auditoria para verificar as mudanças
SELECT * FROM Funcionario_Auditoria WHERE id = (SELECT id FROM Funcionario WHERE nome = 'Ana');
```

Este comando SQL irá retornar os registros da tabela de auditoria que correspondem ao funcionário "Ana". Você deve ver uma linha com o salário antigo (4000.00), o novo salário (4300.00) e a data/hora da modificação, indicando que o trigger operou conforme o esperado.

## Exemplo com desafio de Estoque

Neste exercício, você irá implementar um sistema simples de gestão de estoque para uma loja que vende camisetas como Basica, Dados e Verao. A loja precisa garantir que as vendas sejam registradas apenas se houver estoque suficiente para atender os pedidos. Você será responsável por criar um trigger no banco de dados que previna a inserção de vendas que excedam a quantidade disponível dos produtos.

```sql
-- Criação da tabela Produto
CREATE TABLE Produto (
    cod_prod INT PRIMARY KEY,
    descricao VARCHAR(50) UNIQUE,
    qtde_disponivel INT NOT NULL DEFAULT 0
);

-- Inserção de produtos
INSERT INTO Produto VALUES (1, 'Basica', 10);
INSERT INTO Produto VALUES (2, 'Dados', 5);
INSERT INTO Produto VALUES (3, 'Verao', 15);

-- Criação da tabela RegistroVendas
CREATE TABLE RegistroVendas (
    cod_venda SERIAL PRIMARY KEY,
    cod_prod INT,
    qtde_vendida INT,
    FOREIGN KEY (cod_prod) REFERENCES Produto(cod_prod) ON DELETE CASCADE
);
```

```sql
-- Criação de um TRIGGER
CREATE OR REPLACE FUNCTION verifica_estoque() RETURNS TRIGGER AS $$
DECLARE
    qted_atual INTEGER;
BEGIN
    SELECT qtde_disponivel INTO qted_atual
    FROM Produto WHERE cod_prod = NEW.cod_prod;
    IF qted_atual < NEW.qtde_vendida THEN
        RAISE EXCEPTION 'Quantidade indisponivel em estoque'
    ELSE
        UPDATE Produto SET qtde_disponivel = qtde_disponivel - NEW.qtde_vendida
        WHERE cod_prod = NEW.cod_prod;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_verifica_estoque 
BEFORE INSERT ON RegistroVendas
FOR EACH ROW 
EXECUTE FUNCTION verifica_estoque();
```
    
```sql
-- Tentativa de venda de 5 unidades de Basico (deve ser bem-sucedida, pois há 10 unidades disponíveis)
INSERT INTO RegistroVendas (cod_prod, qtde_vendida) VALUES (1, 5);

-- Tentativa de venda de 6 unidades de Dados (deve ser bem-sucedida, pois há 5 unidades disponíveis e a quantidade vendida não excede o estoque)
INSERT INTO RegistroVendas (cod_prod, qtde_vendida) VALUES (2, 5);

-- Tentativa de venda de 16 unidades de Versao (deve falhar, pois só há 15 unidades disponíveis)
INSERT INTO RegistroVendas (cod_prod, qtde_vendida) VALUES (3, 16);
```
