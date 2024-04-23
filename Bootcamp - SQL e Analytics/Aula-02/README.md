# Aula 01 - SQL para Analytics: Nossas primeiras consultas

## Objetivo

Realizar nossas primeiras consultas no banco Northwind

## Uma tangente antes de realizarmos nossas primeiras consultas

SQL, ou Structured Query Language, é uma linguagem de programação projetada para gerenciar dados armazenados em um sistema de gerenciamento de banco de dados relacional (RDBMS). SQL possui vários componentes, cada um responsável por diferentes tipos de tarefas e operações que podem ser executadas em um banco de dados. Esses componentes incluem DDL, DML, DCL, e DQL, entre outros. Aqui está um resumo de cada um deles:

Cada componente da linguagem SQL tem um papel fundamental na gestão e no uso de bancos de dados, e diferentes tipos de profissionais de tecnologia podem utilizar esses comandos para desempenhar suas funções específicas. Vamos detalhar quem geralmente é responsável por cada tipo de comando e qual o objetivo de cada um dos componentes mencionados (DDL, DML, DQL, DCL, TCL):

### 1. DDL (Data Definition Language)

O DDL ou Linguagem de Definição de Dados é usado para definir e modificar a estrutura do banco de dados e seus objetos, como tabelas, índices, restrições, esquemas, entre outros. Comandos DDL incluem:

* **CREATE**: Usado para criar novos objetos no banco de dados, como tabelas, índices, funções, vistas, triggers, etc.
* **ALTER**: Modifica a estrutura de um objeto existente no banco de dados, por exemplo, adicionando uma coluna a uma tabela ou alterando características de uma coluna existente.
* **DROP**: Remove objetos do banco de dados.
* **TRUNCATE**: Remove todos os registros de uma tabela, liberando o espaço ocupado por esses registros.

* **Responsável**: Administradores de banco de dados (DBAs) e desenvolvedores de banco de dados.
* **Objetivo**: O DDL é usado para criar e modificar a estrutura do banco de dados e de seus objetos. Esses comandos ajudam a definir como os dados são organizados, armazenados, e como as relações entre eles são estabelecidas. Eles são essenciais durante a fase de design do banco de dados e quando são necessárias mudanças na estrutura.

### 2. DML (Data Manipulation Language)

O DML ou Linguagem de Manipulação de Dados é usado para gerenciar dados dentro dos objetos (como tabelas). Inclui comandos para inserir, modificar e deletar dados:

* **INSERT**: Insere dados em uma tabela.
* **UPDATE**: Altera dados existentes em uma tabela.
* **DELETE**: Remove dados de uma tabela.
* **MERGE**: Uma operação que permite inserir, atualizar ou deletar registros em uma tabela com base em um conjunto de condições determinadas.

* **Responsável**: Desenvolvedores de software, analistas de dados e, ocasionalmente, usuários finais através de interfaces que executam comandos DML por trás dos panos.
* **Objetivo**: O DML é crucial para o gerenciamento dos dados dentro das tabelas. Ele é utilizado para inserir, atualizar, deletar e manipular dados armazenados. Analistas de dados podem usar DML para preparar conjuntos de dados para análise, enquanto os desenvolvedores o utilizam para implementar a lógica de negócios.

### 3. DQL (Data Query Language)

O DQL ou Linguagem de Consulta de Dados é fundamentalmente usado para realizar consultas nos dados. O comando mais conhecido na DQL é o **SELECT**, que é utilizado para recuperar dados de uma ou mais tabelas.

* **Responsável**: Analistas de dados, cientistas de dados, e qualquer usuário que necessite extrair informações do banco de dados.
* **Objetivo**: O DQL é usado para consultar e recuperar dados. É fundamental para gerar relatórios, realizar análises, e fornecer dados que ajudem na tomada de decisões. O comando `SELECT`, parte do DQL, é um dos mais usados e é essencial para qualquer tarefa que requer visualização ou análise de dados.

### 4. DCL (Data Control Language)

O DCL ou Linguagem de Controle de Dados inclui comandos relacionados à segurança na acessibilidade dos dados no banco de dados. Isso envolve comandos para conceder e revogar permissões de acesso:

* **GRANT**: Concede permissões de acesso aos usuários.
* **REVOKE**: Remove permissões de acesso.

* **Responsável**: Administradores de banco de dados.
* **Objetivo**: O DCL é usado para configurar permissões em um banco de dados, garantindo que apenas usuários autorizados possam acessar, modificar, ou administrar os dados. Isso é crucial para a segurança e a governança de dados, protegendo informações sensíveis e mantendo a integridade do sistema.

### 5. TCL (Transaction Control Language)

O TCL ou Linguagem de Controle de Transação é usado para gerenciar transações no banco de dados. Transações são importantes para manter a integridade dos dados e garantir que operações múltiplas sejam concluídas com sucesso ou não sejam realizadas de todo:

* **COMMIT**: Confirma uma transação, tornando todas as mudanças permanentes no banco de dados.
* **ROLLBACK**: Desfaz todas as mudanças feitas durante a transação atual.
* **SAVEPOINT**: Define um ponto na transação que pode ser usado para um rollback parcial.

* **Responsável**: Desenvolvedores de software e administradores de banco de dados.
* **Objetivo**: O TCL é usado para gerenciar transações no banco de dados, garantindo que as operações sejam completadas com sucesso ou revertidas em caso de erro. Isso é essencial para manter a consistência e integridade dos dados, especialmente em ambientes onde múltiplas transações ocorrem simultaneamente.

Essa separação de responsabilidades ajuda a manter a organização e eficiência das operações do banco de dados, além de garantir que as ações executadas em um ambiente de banco de dados sejam seguras e alinhadas com as necessidades da organização.

## Se olharmos os comandos que fizemos ontem...

1) Esse comando é de qual subconjunto?

```sql
SELECT * FROM customers WHERE country='Mexico';
```

2) Esse comando é de qual subconjunto?

```sql
INSERT INTO customers VALUES ('ALFKI', 'Alfreds Futterkiste', 'Maria Anders', 'Sales Representative', 'Obere Str. 57', 'Berlin', NULL, '12209', 'Germany', '030-0074321', '030-0076545');
INSERT INTO customers VALUES ('ANATR', 'Ana Trujillo Emparedados y helados', 'Ana Trujillo', 'Owner', 'Avda. de la Constitución 2222', 'México D.F.', NULL, '05021', 'Mexico', '(5) 555-4729', '(5) 555-3745');
INSERT INTO customers VALUES ('ANTON', 'Antonio Moreno Taquería', 'Antonio Moreno', 'Owner', 'Mataderos  2312', 'México D.F.', NULL, '05023', 'Mexico', '(5) 555-3932', NULL);
INSERT INTO customers VALUES ('AROUT', 'Around the Horn', 'Thomas Hardy', 'Sales Representative', '120 Hanover Sq.', 'London', NULL, 'WA1 1DP', 'UK', '(171) 555-7788', '(171) 555-6750');
INSERT INTO customers VALUES ('BERGS', 'Berglunds snabbköp', 'Christina Berglund', 'Order Administrator', 'Berguvsvägen  8', 'Luleå', NULL, 'S-958 22', 'Sweden', '0921-12 34 65', '0921-12 34 67');
```

3) Esse comando é de qual subconjunto?

```sql
CREATE TABLE suppliers (
    supplier_id smallint NOT NULL,
    company_name character varying(40) NOT NULL,
    contact_name character varying(30),
    contact_title character varying(30),
    address character varying(60),
    city character varying(15),
    region character varying(15),
    postal_code character varying(10),
    country character varying(15),
    phone character varying(24),
    fax character varying(24),
    homepage text
);
```

4) Esse comando é de qual subconjunto?

```sql
SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
```

## Agora vamos para nossas primeiras QUERY? (Data Query Language)

Data Query Language (DQL) é um subconjunto da linguagem SQL (Structured Query Language) utilizado especificamente para consultar dados em bancos de dados. DQL é fundamental para extrair informações, realizar análises e gerar relatórios a partir dos dados armazenados em um sistema de gerenciamento de banco de dados relacional (RDBMS). O principal comando em DQL é o `SELECT`, que é amplamente utilizado para selecionar dados de uma ou mais tabelas.

**Objetivos da DQL**

O principal objetivo da DQL é permitir que usuários e aplicações recuperem dados de forma eficiente e precisa de um banco de dados. DQL proporciona a flexibilidade para especificar exatamente quais dados são necessários, como devem ser filtrados, agrupados, ordenados e transformados. Isso torna a DQL uma ferramenta essencial para:

* **Análise de dados**: Extrair conjuntos de dados para análise e tomada de decisão baseada em evidências.
* **Geração de relatórios**: Criar relatórios detalhados que ajudam as organizações a entender o desempenho operacional e estratégico.
* **Visualização de dados**: Alimentar ferramentas de visualização com dados que ajudam a representar informações complexas de maneira compreensível.
* **Auditoria e monitoramento**: Acompanhar e revisar operações e transações para conformidade e segurança.

**Como começar com DQL**

Para começar a usar DQL, é essencial ter um conhecimento básico de SQL e entender a estrutura dos dados dentro do banco de dados com o qual você está trabalhando. Aqui estão alguns passos para começar:

1. **Entenda o esquema do banco de dados**: Conheça as tabelas, colunas, tipos de dados e relações entre as tabelas.
2. **Aprenda os fundamentos do comando `SELECT`**: Comece com consultas simples para selecionar colunas específicas de uma tabela.
3. **Use cláusulas para refinar suas consultas**:
    * **WHERE**: Para filtrar registros.
    * **GROUP BY**: Para agrupar registros.
    * **HAVING**: Para filtrar grupos.
    * **ORDER BY**: Para ordenar os resultados.
4. **Pratique com dados de exemplo**: Use um banco de dados de exemplo para praticar suas consultas e testar diferentes cenários.

**Principais comandos da DQL**

* **SELECT**: O comando mais fundamental em DQL, usado para selecionar dados de uma ou mais tabelas.
    
    ```sql
    SELECT * FROM customers;
    select contact_name, city from customers;
    ```
    
* **DISTINCT**: Usado com `SELECT` para retornar apenas valores distintos.
    
    ```sql
    select country from customers;
    select distinct country from customers;
    select count(distinct country) from customers;
    ```

* **WHERE**: Usado para filtrar.

```sql
-- Seleciona todos os clientes do México
SELECT * FROM customers WHERE country='Mexico';
-- Seleciona clientes com ID específico
SELECT * FROM customers WHERE customer_id='ANATR';
-- Utiliza AND para múltiplos critérios
SELECT * FROM customers WHERE country='Germany' AND city='Berlin';
-- Utiliza OR para mais de uma cidade
SELECT * FROM customers WHERE city='Berlin' OR city='Aachen';
-- Utiliza NOT para excluir a Alemanha
SELECT * FROM customers WHERE country<>'Germany';
-- Combina AND, OR e NOT
SELECT * FROM customers WHERE country='Germany' AND (city='Berlin' OR city='Aachen');
-- Exclui clientes da Alemanha e EUA
SELECT * FROM customers WHERE country<>'Germany' AND country<>'USA';
```

### Mais operadores

Os operadores de comparação no SQL são essenciais para filtrar registros em consultas com base em condições específicas. Vamos examinar cada um dos operadores que você mencionou (`<`, `>`, `<=`, `>=`, `<>`) com exemplos práticos. Suponhamos que temos uma tabela chamada `products` com uma coluna `unit_price` para o preço dos produtos e uma coluna `units_in_stock` para o número de itens em estoque.

### Operador `<` (Menor que)

```sql
-- Seleciona todos os produtos com preço menor que 20
SELECT * FROM products
WHERE unit_price < 20;
```

### Operador `>` (Maior que)

```sql
-- Seleciona todos os produtos com preço maior que 100
SELECT * FROM products
WHERE unit_price > 100;
```

### Operador `<=` (Menor ou igual a)

```sql
-- Seleciona todos os produtos com preço menor ou igual a 50
SELECT * FROM products
WHERE unit_price <= 50;
```

### Operador `>=` (Maior ou igual a)

```sql
-- Seleciona todos os produtos com quantidade em estoque maior ou igual a 10
SELECT * FROM products
WHERE units_in_stock >= 10;
```

### Operador `<>` (Diferente de)

```sql
-- Seleciona todos os produtos cujo preço não é 30
SELECT * FROM products
WHERE unit_price <> 30;
```

### Combinação de Operadores

Você também pode combinar vários operadores em uma única consulta para criar condições mais específicas:

```sql
-- Seleciona todos os produtos com preço entre 50 e 100 (exclusive)
SELECT * FROM products
WHERE unit_price >= 50 AND unit_price < 100;
```

```sql
-- Seleciona todos os produtos com preço fora do intervalo 20 a 40
SELECT * FROM products
WHERE unit_price < 20 OR unit_price > 40;
```

* **Is null and is not null**: Usado em conjunto com o `where` para criar regras mais complexas de filtro nos registros.

```sql
SELECT * FROM customers
WHERE contact_name is Null;

SELECT * FROM customers
WHERE contact_name is not null;
```

* **LIKE**

```SQL
-- Nome do cliente começando com "a":
SELECT * FROM customers
WHERE contact_name LIKE 'a%';
```

Para tratar as strings como maiúsculas ou minúsculas em uma consulta SQL, você pode usar as funções `UPPER()` ou `LOWER()`, respectivamente. Essas funções convertem todas as letras em uma string para maiúsculas ou minúsculas, permitindo que você faça comparações de forma mais flexível, ignorando a diferença entre maiúsculas e minúsculas.

Aqui está como você pode modificar a consulta para encontrar todos os clientes cujo nome começa com a letra "a", independentemente de ser maiúscula ou minúscula:

### Para encontrar nomes que começam com "a" em maiúscula ou minúscula:

```sql
SELECT * FROM customers
WHERE LOWER(contact_name) LIKE 'a%';
```

Essa consulta converte todo o `contact_name` para minúsculas antes de fazer a comparação, o que torna a busca insensível a maiúsculas e minúsculas.

### Para encontrar nomes que começam com "A" em maiúscula:

```sql
SELECT * FROM customers
WHERE UPPER(contact_name) LIKE 'A%';
```

Essa consulta converte todo o `contact_name` para maiúsculas antes de fazer a comparação, garantindo que apenas os nomes que começam com "A" maiúscula sejam selecionados.

Usar `UPPER()` ou `LOWER()` é uma prática comum para garantir que as condições aplicadas em campos de texto não sejam afetadas por diferenças de capitalização nas entradas de dados.

```sql
-- Nome do cliente terminando com "a":
SELECT * FROM customers
WHERE contact_name LIKE '%a';

-- Nome do cliente que possui "or" em qualquer posição:
SELECT * FROM customers
WHERE contact_name LIKE '%or%';

-- Nome do cliente com "r" na segunda posição:
SELECT * FROM customers
WHERE contact_name LIKE '_r%';

-- Nome do cliente que começa com "A" e tem pelo menos 3 caracteres de comprimento:
SELECT * FROM customers
WHERE contact_name LIKE 'A_%_%';

-- Nome do contato que começa com "A" e termina com "o":
SELECT * FROM customers
WHERE contact_name LIKE 'A%o';

-- Nome do cliente que NÃO começa com "a":
SELECT * FROM customers
WHERE contact_name NOT LIKE 'A%';

-- Usando o curinga [charlist] (SQL server)
SELECT * FROM customers
WHERE city LIKE '[BSP]%';

-- Usando o curinga Similar To (Postgres)
SELECT * FROM customers
WHERE city SIMILAR TO '(B|S|P)%';

-- Usando o MySQL (coitado, tem nada)
SELECT * FROM customers
WHERE (city LIKE 'B%' OR city LIKE 'S%' OR city LIKE 'P%');
```

* **Operador IN**

```sql
-- localizado na "Alemanha", "França" ou "Reino Unido":
SELECT * FROM customers
WHERE country IN ('Germany', 'France', 'UK');

-- NÃO localizado na "Alemanha", "França" ou "Reino Unido":
SELECT * FROM customers
WHERE country NOT IN ('Germany', 'France', 'UK');

-- Só para dar um gostinho de uma subqueyr... Seleciona todos os clientes que são dos mesmos países que os fornecedores:

SELECT * FROM customers
WHERE country IN (SELECT country FROM suppliers);

-- Exemplo com BETWEEN
SELECT * FROM products
WHERE unit_price BETWEEN 10 AND 20;

-- Exemplo com NOT BETWEEN
SELECT * FROM products
WHERE unit_price NOT BETWEEN 10 AND 20;

-- Seleciona todos os produtos com preço ENTRE 10 e 20. Adicionalmente, não mostra produtos com CategoryID de 1, 2 ou 3:
SELECT * FROM products
WHERE (unit_price BETWEEN 10 AND 20) AND category_id NOT IN (1, 2, 3);
```

```sql
--selects todos os produtos entre 'Carnarvon Tigers' e 'Mozzarella di Giovanni':
select * from products
where product_name between 'Carnarvon Tigers' and 'Mozzarella di Giovanni'
order by product_name;

--Selecione todas as ordens BETWEEN '04-July-1996' e '09-July-1996':
select * from orders
where order_date between '07/04/1996' and '07/09/1996';
```

* **Tangente sobre diferentes bancos**

O comando SQL que você mencionou é específico para PostgreSQL e não necessariamente padrão em todos os SGBDs (Sistemas de Gerenciamento de Banco de Dados). Cada SGBD pode ter funções e formatos de data ligeiramente diferentes. No entanto, a estrutura básica do comando `SELECT` e a cláusula `WHERE` usando `BETWEEN` são bastante universais.

Aqui estão algumas variantes para outros SGBDs populares:

### SQL Server

Para formatar datas em SQL Server, você usaria a função `CONVERT` ou `FORMAT` (a partir do SQL Server 2012):

```sql
-- Usando CONVERT
SELECT CONVERT(VARCHAR, order_date, 120) FROM orders
WHERE order_date BETWEEN '1996-04-07' AND '1996-09-07';

-- Usando FORMAT
SELECT FORMAT(order_date, 'yyyy-MM-dd') FROM orders
WHERE order_date BETWEEN '1996-04-07' AND '1996-09-07';
```

### MySQL

MySQL utiliza a função `DATE_FORMAT` para formatar datas:

```sql
SELECT DATE_FORMAT(order_date, '%Y-%m-%d') FROM orders
WHERE order_date BETWEEN '1996-04-07' AND '1996-09-07';
```

### Oracle

Oracle também usa a função `TO_CHAR` como PostgreSQL para formatação de datas:

```sql
SELECT TO_CHAR(order_date, 'YYYY-MM-DD') FROM orders
WHERE order_date BETWEEN TO_DATE('1996-04-07', 'YYYY-MM-DD') AND TO_DATE('1996-09-07', 'YYYY-MM-DD');
```

### SQLite

SQLite não tem uma função dedicada para formatar datas, mas você pode usar funções de string para manipular formatos de data padrão:

```sql
SELECT strftime('%Y-%m-%d', order_date) FROM orders
WHERE order_date BETWEEN '1996-04-07' AND '1996-09-07';
```

* **Funções Agregadas** (COUNT, MAX, MIN, SUM, AVG): Usadas para realizar cálculos em um conjunto de valores.

As funções agregadas são uma ferramenta fundamental na linguagem SQL, utilizadas para realizar cálculos sobre um conjunto de valores e retornar um único valor resultante. Essas funções são especialmente úteis em operações que envolvem a análise estatística de dados, como a obtenção de médias, somas, valores máximos e mínimos, entre outros. Ao operar em conjuntos de dados, as funções agregadas permitem extrair insights significativos, suportar decisões de negócios, e simplificar dados complexos em informações gerenciáveis.
    
As funções agregadas geralmente são usadas em consultas SQL com a cláusula GROUP BY, que agrupa linhas que têm os mesmos valores em colunas especificadas. No entanto, podem ser usadas sem GROUP BY para resumir todos os dados de uma tabela. Aqui estão as principais funções agregadas e como são aplicadas:

```sql
-- Exemplo de MIN()
SELECT MIN(unit_price) AS preco_minimo
FROM products;

-- Exemplo de MAX()
SELECT MAX(unit_price) AS preco_maximo
FROM products;

-- Exemplo de COUNT()
SELECT COUNT(*) AS total_de_produtos
FROM products;

-- Exemplo de AVG()
SELECT AVG(unit_price) AS preco_medio
FROM products;

-- Exemplo de SUM()
SELECT SUM(quantity) AS quantidade_total_de_order_details
FROM order_details;
```

### Práticas Recomendadas

* **Precisão de dados**: Ao usar `AVG()` e `SUM()`, esteja ciente do tipo de dados da coluna para evitar imprecisões, especialmente com dados flutuantes.
* **NULLs**: Lembre-se de que a maioria das funções agregadas ignora valores `NULL`, exceto `COUNT(*)`, que conta todas as linhas, incluindo aquelas com valores `NULL`.
* **Performance**: Em tabelas muito grandes, operações agregadas podem ser custosas em termos de desempenho. Considere usar índices adequados ou realizar pré-agregações quando aplicável.
* **Clareza**: Ao usar `GROUP BY`, assegure-se de que todas as colunas não agregadas na sua cláusula `SELECT` estejam incluídas na cláusula `GROUP BY`.

### Exemplo de MIN() com GROUP BY

```sql
-- Calcula o menor preço unitário de produtos em cada categoria
SELECT category_id, MIN(unit_price) AS preco_minimo
FROM products
GROUP BY category_id;
```

### Exemplo de MAX() com GROUP BY

```sql
-- Calcula o maior preço unitário de produtos em cada categoria
SELECT category_id, MAX(unit_price) AS preco_maximo
FROM products
GROUP BY category_id;
```

### Exemplo de COUNT() com GROUP BY

```sql
-- Conta o número total de produtos em cada categoria
SELECT category_id, COUNT(*) AS total_de_produtos
FROM products
GROUP BY category_id;
```

### Exemplo de AVG() com GROUP BY

```sql
-- Calcula o preço médio unitário de produtos em cada categoria
SELECT category_id, AVG(unit_price) AS preco_medio
FROM products
GROUP BY category_id;
```

### Exemplo de SUM() com GROUP BY

```sql
-- Calcula a quantidade total de produtos pedidos por pedido
SELECT order_id, SUM(quantity) AS quantidade_total_por_pedido
FROM order_details
GROUP BY order_id;
```

* **Desafio**

1. Obter todas as colunas das tabelas Clientes, Pedidos e Fornecedores

```sql
SELECT * FROM customers;
SELECT * FROM orders;
SELECT * FROM suppliers;
```

2. Obter todos os Clientes em ordem alfabética por país e nome

```sql
SELECT *
FROM customers
ORDER BY country, contact_name;
```

3. Obter os 5 pedidos mais antigos

```sql
SELECT * 
FROM orders 
ORDER BY order_date
LIMIT 5;
```

4. Obter a contagem de todos os Pedidos feitos durante 1997

```sql
SELECT COUNT(*) AS "Number of Orders During 1997"
FROM orders
WHERE order_date BETWEEN '1997-1-1' AND '1997-12-31';
```

5. Obter os nomes de todas as pessoas de contato onde a pessoa é um gerente, em ordem alfabética

```sql
SELECT contact_name
FROM customers
WHERE contact_title LIKE '%Manager%'
ORDER BY contact_name;
```

6. Obter todos os pedidos feitos em 19 de maio de 1997

```sql
SELECT *
FROM orders
WHERE order_date = '1997-05-19';
```