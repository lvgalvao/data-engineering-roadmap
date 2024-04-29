## Aula 06 - CTE vs Subqueries vs Views vs Temporary Tables vs Materialized Views

1. **CTE (Common Table Expressions):**
    
    * **Onde usar:** As CTEs são úteis quando você precisa dividir uma consulta em partes mais gerenciáveis ou quando deseja reutilizar uma subconsulta várias vezes na mesma consulta principal.
    * **Vantagens:**
        * Permitem escrever consultas mais legíveis e organizadas, dividindo a lógica em partes distintas.
        * Podem ser referenciadas várias vezes na mesma consulta.
    * **Desvantagens:**
        * Podem não ser tão eficientes quanto outras técnicas, especialmente se a CTE for referenciada várias vezes ou se a consulta for muito complexa.

    ```sql
    WITH TotalRevenues AS (
        SELECT 
            customers.company_name, 
            SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) AS total
        FROM customers
        INNER JOIN orders ON customers.customer_id = orders.customer_id
        INNER JOIN order_details ON order_details.order_id = orders.order_id
        GROUP BY customers.company_name
    )
    SELECT * FROM TotalRevenues;
    ```

2. **Subqueries:**
    
    * **Onde usar:** Subqueries são úteis quando você precisa de resultados intermediários para filtrar ou agregar dados em uma consulta principal.
    * **Vantagens:**
        * São simples de escrever e entender, especialmente para consultas simples.
        * Podem ser aninhadas dentro de outras subqueries ou consultas principais.
    * **Desvantagens:**
        * Pode tornar consultas complexas difíceis de entender e manter.
        * Em algumas situações, podem não ser tão eficientes quanto outras técnicas, especialmente se as subqueries forem executadas várias vezes.

    ```sql
    SELECT 
        company_name, 
        (
            SELECT SUM(unit_price * quantity * (1.0 - discount))
            FROM order_details
            WHERE order_id IN (
                SELECT order_id FROM orders WHERE orders.customer_id = customers.customer_id
            )
        ) AS total
    FROM customers;
    ```

3. **Views:**
    
    * **Onde usar:** As views são úteis quando você precisa reutilizar uma consulta em várias consultas ou quando deseja simplificar consultas complexas dividindo-as em partes menores.
    * **Vantagens:**
        * Permitem abstrair a lógica de consulta complexa em um objeto de banco de dados reutilizável.
        * Facilitam a segurança, pois você pode conceder permissões de acesso à view em vez das tabelas subjacentes.
    * **Desvantagens:**
        * As views não armazenam dados fisicamente, então elas precisam ser reavaliadas sempre que são consultadas, o que pode impactar o desempenho.
        * Se uma view depende de outras views ou tabelas, a complexidade pode aumentar.

    ```sql
    CREATE VIEW TotalRevenues AS
    SELECT 
        customers.company_name, 
        SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) AS total
    FROM customers
    INNER JOIN orders ON customers.customer_id = orders.customer_id
    INNER JOIN order_details ON order_details.order_id = orders.order_id
    GROUP BY customers.company_name;
    
    SELECT * FROM TotalRevenues;
    ```

    ```sql
    GRANT SELECT ON TotalRevenues TO user1;
    ```

4. **Temporary Tables:**
    
    * **Onde usar:** Tabelas temporárias são úteis quando você precisa armazenar dados temporários para uso em uma sessão de banco de dados ou em uma consulta específica.
    * **Vantagens:**
        * Permitem armazenar resultados intermediários de uma consulta complexa para reutilização posterior.
        * Podem ser indexadas para melhorar o desempenho em consultas subsequentes.
    * **Desvantagens:**
        * Podem consumir recursos do banco de dados, especialmente se forem grandes.
        * Exigem gerenciamento explícito para limpar os dados após o uso.

    ```sql
    CREATE TEMP TABLE TempTotalRevenues AS
    SELECT 
        customers.company_name, 
        SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) AS total
    FROM customers
    INNER JOIN orders ON customers.customer_id = orders.customer_id
    INNER JOIN order_details ON order_details.order_id = orders.order_id
    GROUP BY customers.company_name;
    
    SELECT * FROM TempTotalRevenues;
    ```

5. **Materialized Views:**
    
    * **Onde usar:** Materialized views são úteis quando você precisa pré-calcular e armazenar resultados de consultas complexas para consultas frequentes ou análises de desempenho.
    * **Vantagens:**
        * Permitem armazenar fisicamente os resultados de uma consulta, melhorando significativamente o desempenho em consultas subsequentes.
        * Reduzem a carga no banco de dados, já que os resultados são pré-calculados e armazenados.
    * **Desvantagens:**
        * Precisam ser atualizadas regularmente para manter os dados atualizados, o que pode consumir recursos do sistema.
        * A introdução de dados redundantes pode aumentar os requisitos de armazenamento.

    ```sql
    CREATE MATERIALIZED VIEW MaterializedTotalRevenues AS
    SELECT 
        customers.company_name, 
        SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) AS total
    FROM customers
    INNER JOIN orders ON customers.customer_id = orders.customer_id
    INNER JOIN order_details ON order_details.order_id = orders.order_id
    GROUP BY customers.company_name;
    
    SELECT * FROM MaterializedTotalRevenues;
    ```

    ```sql
    REFRESH MATERIALIZED VIEW MaterializedTotalRevenues;
    ```

    ```sql
    REFRESH MATERIALIZED VIEW CONCURRENTLY MaterializedTotalRevenues
    ```

* **Performance**

```sql
WITH TotalRevenues AS (
    SELECT 
        customers.company_name, 
        SUM(order_details.unit_price * order_details.quantity * (1.0 - order_details.discount)) AS total
    FROM customers
    INNER JOIN orders ON customers.customer_id = orders.customer_id
    INNER JOIN order_details ON order_details.order_id = orders.order_id
    CROSS JOIN products -- Junção cruzada com a tabela de produtos para aumentar a carga da consulta
    GROUP BY customers.company_name
)
SELECT * FROM TotalRevenues;
```

```sql
-- Criação da tabela temporária
CREATE TEMP TABLE TotalRevenues AS
SELECT 
    *
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id
INNER JOIN order_details ON order_details.order_id = orders.order_id
CROSS JOIN products; -- Junção cruzada com a tabela de produtos para aumentar a carga da consulta

-- Consulta na tabela temporária
SELECT * FROM TotalRevenues;
```


Em resumo, cada técnica tem seu lugar e uso apropriado, dependendo dos requisitos específicos de cada situação. As CTEs e subqueries são úteis para consultas simples ou interações temporárias com os dados, enquanto as views e as tabelas temporárias são mais adequadas para consultas e manipulações de dados mais complexas. As materialized views são ideais para consultas frequentes ou análises de desempenho, onde o desempenho é crucial e os dados podem ser pré-calculados e armazenados fisicamente.

* **Materialized view vs Table**

1. Armazenamento de Dados:
    
    * Tabela Normal: Armazena dados fisicamente no banco de dados.
    * Materialized View: Armazena os resultados de uma consulta como uma tabela física.
2. Atualização Automática:
    
    * Tabela Normal: Os dados são atualizados manual ou automaticamente através de operações de inserção, atualização e exclusão.
    * Materialized View: Os dados não são atualizados automaticamente. Eles precisam ser atualizados manualmente usando o comando `REFRESH MATERIALIZED VIEW`.
3. Desempenho:
    
    * Tabela Normal: As consultas são executadas diretamente nos dados armazenados na tabela.
    * Materialized View: As consultas são executadas nos dados armazenados na materialized view, o que pode melhorar o desempenho de consultas complexas ou frequentemente usadas.
4. Uso de Espaço em Disco:
    
    * Tabela Normal: Pode ocupar mais espaço em disco devido ao armazenamento físico de dados.
    * Materialized View: Pode ocupar menos espaço em disco, pois armazena apenas os resultados da consulta, não os dados brutos.
5. Flexibilidade:
    
    * Tabela Normal: Os dados são atualizados em tempo real e podem ser manipulados diretamente.
    * Materialized View: Os resultados da consulta são estáticos e precisam ser atualizados manualmente. Eles são usados principalmente para armazenar resultados de consultas complexas que não mudam com frequência.