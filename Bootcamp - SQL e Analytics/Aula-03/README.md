# Aula 03 - SQL para Analytics: Join and Having in SQL

## Introdução aos Joins em SQL

Joins em SQL são fundamentais para combinar registros de duas ou mais tabelas em um banco de dados com base em uma condição comum, geralmente uma chave estrangeira. Essa técnica permite que dados relacionados, que são armazenados em tabelas separadas, sejam consultados juntos de forma eficiente e coerente. 

Os joins são essenciais para consultar dados complexos e para aplicações em que a normalização do banco de dados resulta em distribuição de informações por diversas tabelas.

Existem vários tipos de joins, cada um com seu uso específico dependendo das necessidades da consulta:

1. **Inner Join**: Retorna registros que têm correspondência em ambas as tabelas.
2. **Left Join (ou Left Outer Join)**: Retorna todos os registros da tabela esquerda e os registros correspondentes da tabela direita. Se não houver correspondência, os resultados da tabela direita terão valores `NULL`.
3. **Right Join (ou Right Outer Join)**: Retorna todos os registros da tabela direita e os registros correspondentes da tabela esquerda. Se não houver correspondência, os resultados da tabela esquerda terão valores `NULL`.
4. **Full Join (ou Full Outer Join)**: Retorna registros quando há uma correspondência em uma das tabelas. Se não houver correspondência, ainda assim, o resultado aparecerá com `NULL` nos campos da tabela sem correspondência.

### 1. Criar um relatório para todos os pedidos de 1996 e seus clientes

**Inner Join**

**Uso**: Utilizado quando você precisa de registros que têm correspondência exata em ambas as tabelas. 

**Exemplo Prático**: Se quisermos encontrar todos os pedidos de 1996 e os detalhes dos clientes que fizeram esses pedidos, usamos um Inner Join. Isso garante que só obteremos os pedidos que possuem um cliente correspondente e que foram feitos em 1996.

```sql
-- Cria um relatório para todos os pedidos de 1996 e seus clientes (152 linhas)
SELECT *
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id
WHERE EXTRACT(YEAR FROM o.order_date) = 1996;
```

### 2. Criar um relatório que mostra o número de funcionários e clientes de cada cidade que tem funcionários

**Left Join**

**Uso**: Usado quando você quer todos os registros da primeira (esquerda) tabela, com os correspondentes da segunda (direita) tabela. Se não houver correspondência, a segunda tabela terá campos `NULL`. 

**Exemplo Prático**: Se precisarmos listar todas as cidades onde temos funcionários, e também queremos saber quantos clientes temos nessas cidades, mesmo que não haja clientes, usamos um Left Join.

```sql
-- Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem funcionários (5 linhas)
SELECT e.city AS cidade, 
       COUNT(DISTINCT e.employee_id) AS numero_de_funcionarios, 
       COUNT(DISTINCT c.customer_id) AS numero_de_clientes
FROM employees e 
LEFT JOIN customers c ON e.city = c.city
GROUP BY e.city
ORDER BY cidade;
```

### 3. Criar um relatório que mostra o número de funcionários e clientes de cada cidade que tem clientes

**Right Join**

**Uso**: É o inverso do Left Join e é menos comum. Usado quando queremos todos os registros da segunda (direita) tabela e os correspondentes da primeira (esquerda) tabela. 

**Exemplo Prático**: Para listar todas as cidades onde temos clientes, e também contar quantos funcionários temos nessas cidades, usamos um Right Join.

```sql
-- Cria um relatório que mostra o número de funcionários e clientes de cada cidade que tem clientes (69 linhas)
SELECT c.city AS cidade, 
       COUNT(DISTINCT c.customer_id) AS numero_de_clientes, 
       COUNT(DISTINCT e.employee_id) AS numero_de_funcionarios
FROM employees e 
RIGHT JOIN customers c ON e.city = c.city
GROUP BY c.city
ORDER BY cidade;
```

### 4. Criar um relatório que mostra o número de funcionários e clientes de cada cidade

**Full Join**

**Uso**: Utilizado quando queremos a união de Left Join e Right Join, mostrando todos os registros de ambas as tabelas, e preenchendo com `NULL` onde não há correspondência. 

**Exemplo Prático**: Para listar todas as cidades onde temos clientes ou funcionários, e contar ambos em cada cidade, usamos um Full Join.

```sql
-- Cria um relatório que mostra o número de funcionários e clientes de cada cidade (71 linhas)
SELECT
	COALESCE(e.city, c.city) AS cidade,
	COUNT(DISTINCT e.employee_id) AS numero_de_funcionarios,
	COUNT(DISTINCT c.customer_id) AS numero_de_clientes
FROM employees e 
FULL JOIN customers c ON e.city = c.city
GROUP BY e.city, c.city
ORDER BY cidade;
```