## Aula 07 - Stored Procedures

* **Stored Procedures vs Views**

As Views e Stored Procedures são ambos recursos poderosos em bancos de dados relacionais, mas têm propósitos e funcionalidades distintas.

**Views:**

* As Views são abstrações de consulta que permitem aos usuários definir consultas complexas e frequentemente usadas como uma única entidade.
* Elas são essencialmente consultas SQL pré-definidas que são armazenadas no banco de dados e tratadas como tabelas virtuais.
* As Views simplificam o acesso aos dados, ocultando a complexidade das consultas subjacentes e fornecendo uma interface consistente para os usuários.
* Elas são úteis para simplificar consultas frequentes, segmentar permissões de acesso aos dados e abstrair a complexidade do modelo de dados subjacente.

**Stored Procedures:**

* As Stored Procedures são abstrações de transações que consistem em um conjunto de instruções SQL pré-compiladas e armazenadas no banco de dados.
* Elas são usadas para encapsular operações de banco de dados mais complexas, como atualizações, inserções, exclusões e outras transações.
* As Stored Procedures podem aceitar parâmetros de entrada e retornar valores de saída, o que as torna altamente flexíveis e reutilizáveis em diferentes partes de um aplicativo.
* Elas oferecem maior controle sobre as operações de banco de dados e permitem a execução de lógica de negócios no lado do servidor.

## Criando um novo Banco de dados


Para ilustrar o processo, vamos estabelecer um novo banco de dados que simula um ambiente bancário convencional.

Começaremos criando um novo banco de dados. Em seguida, empregaremos os comandos `CREATE TABLE` e `INSERT INTO`.

```sql
CREATE TABLE IF NOT EXISTS clients (
    id SERIAL PRIMARY KEY NOT NULL,
    limite INTEGER NOT NULL,
    saldo INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY NOT NULL,
    tipo CHAR(1) NOT NULL,
    descricao VARCHAR(10) NOT NULL,
    valor INTEGER NOT NULL,
    cliente_id INTEGER NOT NULL,
    realizada_em TIMESTAMP NOT NULL DEFAULT NOW()
);
```

**CREATE TABLE:**

* O comando `CREATE TABLE` é usado para criar uma nova tabela no banco de dados.
* O `IF NOT EXISTS` é uma cláusula opcional que garante que a tabela só será criada se ainda não existir no banco de dados, evitando erros caso a tabela já exista.
* Em seguida, é especificada o nome da tabela (`clients` e `transactions` neste caso), seguido por uma lista de colunas e suas definições.
* Cada coluna é definida com um nome, um tipo de dado e opcionalmente outras restrições, como a definição de uma chave primária (`PRIMARY KEY`) e a obrigatoriedade de não ser nula (`NOT NULL`).

```sql
INSERT INTO clients (limite, saldo)
VALUES
    (10000, 0),
    (80000, 0),
    (1000000, 0),
    (10000000, 0),
    (500000, 0);
```

**INSERT INTO:**

* O comando `INSERT INTO` é usado para adicionar novos registros a uma tabela existente.
* Na cláusula `INSERT INTO`, é especificado o nome da tabela (`clients` neste caso) seguido da lista de colunas entre parênteses, se necessário.
* Em seguida, a cláusula `VALUES` é usada para especificar os valores a serem inseridos nas colunas correspondentes.
* Cada linha de valores corresponde a um novo registro a ser inserido na tabela, com os valores na mesma ordem que as colunas foram listadas.

Em resumo, esses comandos são fundamentais para definir a estrutura e inserir dados em tabelas no banco de dados, criando assim a base para armazenar e manipular informações de forma organizada e eficiente.

## Vamos agora simular uma transação bancaria

Para realizar a compra de um Carro, de 80 mil reais, no cliente 1.

Vamos realizar esse processo em 2 etapas.

A primeira será um comando de `INSERT INTO` e depois um comando de `UPDATE`

```sql
INSERT INTO transactions (tipo, descricao, valor, cliente_id)
VALUES ('d', 'Compra de carro', 80000, 1)
```

```sql
UPDATE clients
SET saldo = saldo + CASE WHEN 'd' = 'd' THEN -80000 ELSE 80000 END
WHERE id = 1; -- Substitua pelo ID do cliente desejado
```

* **Vamos olhar a situação do cliente 1 agora**

```sql
SELECT saldo, limite 
FROM clients
WHERE id = 1
```

## Vamos precisar corrigir isso

O comando `DELETE` é uma instrução do SQL usada para remover registros de uma tabela com base em uma condição específica. Ele permite que você exclua dados de uma tabela de banco de dados de forma controlada e precisa. Aqui estão alguns pontos-chave sobre o comando `DELETE`:

1. **Sintaxe Básica**: A sintaxe básica do comando `DELETE` é a seguinte:
    
    ```sql
    DELETE FROM nome_da_tabela
    WHERE condição;
    ```
    
2. **Cláusula WHERE**: A cláusula `WHERE` é opcional, mas geralmente é usada para especificar quais registros devem ser excluídos. Se não for especificada, todos os registros da tabela serão excluídos.
    
3. **Remoção Condicional**: Você pode usar a cláusula `WHERE` para definir uma condição para determinar quais registros serão excluídos. Apenas os registros que atendem a essa condição serão removidos.
    
4. **Impacto da Exclusão**: O comando `DELETE` remove permanentemente os registros da tabela, o que significa que os dados excluídos não podem ser recuperados.
    
5. **Uso Cauteloso**: É importante usar o comando `DELETE` com cuidado, especialmente sem uma cláusula `WHERE` específica, pois ele pode resultar na exclusão de todos os registros da tabela.
    
6. **Transações**: Assim como outros comandos SQL de modificação de dados, como `INSERT` e `UPDATE`, o comando `DELETE` pode ser usado dentro de transações para garantir a consistência e a integridade dos dados.
    

No exemplo que você forneceu:

```sql
DELETE FROM transactions
WHERE id = 1;
```

Este comando remove o registro da tabela `transactions` onde o `id` é igual a `1`. Isso resultará na exclusão permanente desse registro específico da tabela. Certifique-se sempre de usar o comando `DELETE` com cuidado e de verificar duas vezes a condição antes de executá-lo para evitar a exclusão acidental de dados importantes.

```sql
DELETE FROM transactions
WHERE id = 1;
```

Vamos precisar voltar também com o saldo atual do cliente, que era de 0.

```sql
UPDATE clients
SET saldo = 0
WHERE id = 1;
```

## Como evitar isso? Stored Procedures

Stored Procedures são rotinas armazenadas no banco de dados que contêm uma série de instruções SQL e podem ser executadas por aplicativos ou usuários conectados ao banco de dados. Elas oferecem várias vantagens, como:

1. **Reutilização de código:** As stored procedures permitem que blocos de código SQL sejam escritos uma vez e reutilizados em várias partes do aplicativo.
    
2. **Desempenho:** Por serem compiladas e armazenadas no banco de dados, as stored procedures podem ser executadas de forma mais eficiente do que várias consultas SQL enviadas separadamente pelo aplicativo.
    
3. **Segurança:** As stored procedures podem ajudar a proteger o banco de dados, pois os aplicativos só precisam de permissão para executar a stored procedure, não para acessar diretamente as tabelas.
    
4. **Abstração de dados:** Elas podem ser usadas para ocultar a complexidade do modelo de dados subjacente, fornecendo uma interface simplificada para os usuários ou aplicativos.
    
5. **Controle de transações:** As stored procedures podem incluir instruções de controle de transações para garantir a integridade dos dados durante operações complexas.

Vamos entender cada parte da stored procedure `realizar_transacao`:

1. **Criação da Procedure:**
    
    ```sql
    CREATE OR REPLACE PROCEDURE realizar_transacao(
        IN p_tipo CHAR(1),
        IN p_descricao VARCHAR(10),
        IN p_valor INTEGER,
        IN p_cliente_id INTEGER
    )
    ```
    
    * Esta declaração cria ou substitui uma stored procedure chamada `realizar_transacao`.
    * A procedure tem quatro parâmetros de entrada: `p_tipo`, `p_descricao`, `p_valor` e `p_cliente_id`, cada um com seu tipo de dado especificado.
2. **Definição da Linguagem:**
    
    ```sql
    LANGUAGE plpgsql
    ```
    
    * Define a linguagem da stored procedure como PL/pgSQL, que é uma linguagem procedural para o PostgreSQL.
3. **Corpo da Procedure:**
    
    ```sql
    AS $$
    DECLARE
        saldo_atual INTEGER;
        limite_cliente INTEGER;
    BEGIN
        -- Corpo da procedure...
    END;
    $$;
    ```
    
    * O corpo da stored procedure é definido entre `AS $$` e `$$;`.
    * Dentro do corpo, declaramos variáveis locais usando `DECLARE`.
    * A execução da procedure ocorre entre `BEGIN` e `END;`.
4. **Obtenção de Dados:**
    
    ```sql
    -- Obtém o saldo atual e o limite do cliente
    SELECT saldo, limite INTO saldo_atual, limite_cliente
    FROM clients
    WHERE id = p_cliente_id;
    ```
    
    * Esta parte do código executa uma consulta para obter o saldo atual e o limite do cliente com o ID fornecido.
5. **Verificação da Transação:**
    
    ```sql
    -- Verifica se a transação é válida com base no saldo e no limite
    IF p_tipo = 'd' AND saldo_atual - p_valor < -limite_cliente THEN
        RAISE EXCEPTION 'Saldo insuficiente para realizar a transação';
    END IF;
    ```
    
    * Aqui, é feita uma verificação para garantir que a transação seja válida com base no tipo de transação ('d' para débito) e se o saldo atual menos o valor da transação é menor que o limite de crédito do cliente. Se a condição for verdadeira, uma exceção é lançada.
6. **Atualização do Saldo:**
    
    ```sql
    -- Atualiza o saldo do cliente
    UPDATE clients
    SET saldo = saldo + CASE WHEN p_tipo = 'd' THEN -p_valor ELSE p_valor END
    WHERE id = p_cliente_id;
    ```
    
    * Nesta parte, o saldo do cliente é atualizado com base no tipo de transação. Se for um débito ('d'), o valor é subtraído do saldo atual; caso contrário, é adicionado.
7. **Inserção da Transação:**
    
    ```sql
    -- Insere uma nova transação
    INSERT INTO transactions (tipo, descricao, valor, cliente_id)
    VALUES (p_tipo, p_descricao, p_valor, p_cliente_id);
    ```
    
    * Por fim, uma nova transação é inserida na tabela `transactions` com os detalhes fornecidos.

Essa stored procedure encapsula todo o processo de realização de uma transação bancária, desde a validação do saldo e limite do cliente até a atualização do saldo e a inserção da transação. Ela oferece uma maneira conveniente e segura de executar essas operações de forma consistente e controlada.

Para chamar a stored procedure `realizar_transacao` com os parâmetros fornecidos, você pode executar o seguinte comando SQL no PostgreSQL:

```sql
CALL realizar_transacao('d', 'carro', 80000, 1);
```

Isso invocará a procedure `realizar_transacao` com os parâmetros fornecidos:

* `p_tipo`: 'd'
* `p_descricao`: 'carro'
* `p_valor`: 80000
* `p_cliente_id`: 1

Certifique-se de executar esse comando em um ambiente onde a stored procedure `realizar_transacao` esteja definida e acessível.

## Desafio

Criar uma stored procedure "ver_extrato" para fornecer uma visão detalhada do extrato bancário de um cliente, incluindo seu saldo atual e as informações das últimas 10 transações realizadas. Esta operação recebe como entrada o ID do cliente e retorna uma mensagem com o saldo atual do cliente e uma lista das últimas 10 transações, contendo o ID da transação, o tipo de transação (depósito ou retirada), uma breve descrição, o valor da transação e a data em que foi realizada.

**Explicação Detalhada:**

1. **Entrada de Parâmetros:**
    
    * A stored procedure recebe o ID do cliente como parâmetro de entrada.
2. **Obtenção do Saldo Atual:**
    
    * É realizada uma consulta na tabela "clients" para obter o saldo atual do cliente com base no ID fornecido.
3. **Exibição do Saldo Atual:**
    
    * O saldo atual do cliente é exibido por meio de uma mensagem de aviso.
4. **Obtenção das Últimas 10 Transações:**
    
    * É realizada uma consulta na tabela "transactions" para obter as últimas 10 transações do cliente, ordenadas pela data de realização em ordem decrescente.
5. **Exibição das Transações:**
    
    * Utilizando um loop `FOR`, cada transação é iterada e suas informações são exibidas por meio de mensagens de aviso.
    * Para cada transação, são exibidos o ID da transação, o tipo de transação (depósito ou retirada), uma breve descrição da transação, o valor da transação e a data em que foi realizada.
    * O loop é interrompido após exibir as informações das últimas 10 transações.

```sql
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
```