# Aula 12 : Database Indexing

**Tópico 1: Índices em Bancos de Dados**

- **Introdução aos Índices:** Índices em bancos de dados são estruturas utilizadas para melhorar a eficiência de consultas, permitindo acesso rápido aos dados. Por exemplo, considere uma tabela de alunos em um banco de dados escolar. Sem índices, uma consulta para encontrar o aluno com um determinado ID exigiria uma busca sequencial na tabela. Com um índice, o banco de dados pode ir diretamente para a linha correspondente ao ID especificado.
- **Tipos de Índices:** Existem vários tipos de índices, incluindo índices de árvore B, índices hash e índices de bitmap. Cada tipo tem suas próprias características e utilizações adequadas.
- **Funcionamento dos Índices:** Os índices são geralmente criados com base em uma ou mais colunas de uma tabela. Quando uma consulta é feita usando uma dessas colunas, o banco de dados pode usar o índice correspondente para localizar rapidamente as linhas relevantes na tabela.
- **Vantagens e Desvantagens:** As vantagens dos índices incluem consultas mais rápidas e eficientes, enquanto as desvantagens incluem custo adicional de armazenamento e sobrecarga de atualização durante operações de inserção, atualização e exclusão.

**Tópico 2: Estruturas de Dados B-Tree**
- **Introdução às Estruturas de Dados B-Tree:** Uma B-Tree é uma árvore balanceada que é frequentemente usada em bancos de dados e sistemas de arquivos. Ela é projetada para permitir inserções, exclusões e pesquisas eficientes em grandes conjuntos de dados, mantendo a árvore balanceada e otimizando a profundidade da árvore.
- **Estrutura da B-Tree:** Uma B-Tree consiste em nós, onde cada nó pode ter várias chaves e vários ponteiros para outros nós. Cada nó tem um número mínimo e máximo de chaves e ponteiros, mantendo a árvore balanceada.
- **Operações em B-Tree:** As operações básicas em uma B-Tree incluem inserção, remoção e busca. Por exemplo, durante uma busca, a árvore é percorrida de acordo com a chave procurada, reduzindo eficientemente o espaço de busca a cada passo.
- **Propriedades das B-Trees:** As B-Trees possuem várias propriedades, como balanceamento automático, garantindo que a profundidade da árvore seja mantida em um nível aceitável, mesmo com muitas inserções e remoções.
- **Aplicações Práticas:** As B-Trees são amplamente utilizadas em bancos de dados para índices, como índices de chaves primárias e secundárias, devido à sua eficiência e capacidade de manipular grandes volumes de dados.

Vamos detalhar cada parte do código:

1. **Criação da Tabela com UUID:**
   - Este trecho de código cria uma tabela chamada `pessoas` com três colunas: `id`, `first_name` e `last_name`. A coluna `id` é definida como uma chave primária (`PRIMARY KEY`) e tem o tipo de dados `UUID`. O valor padrão da coluna `id` é gerado usando a extensão `uuid-ossp`, que é usada para gerar UUIDs aleatórios.
   - Exemplo:
     ```sql
     CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

     CREATE TABLE pessoas (
         id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
         first_name VARCHAR(3),
         last_name VARCHAR(3)
     );
     ```

2. **Verificação de Índices Existente:**
   - Este trecho de código verifica os índices existentes na tabela `pessoas` e exibe suas informações, como nome e definição.
   - Exemplo:
     ```sql
     SELECT 
         tablename AS "Tabela",
         indexname AS "Índice",
         indexdef AS "Definição do Índice"
     FROM 
         pg_indexes 
     WHERE 
         tablename = 'pessoas'; -- Substitua 'pessoas' pelo nome da sua tabela
     ```

3. **Dropar a Tabela com UUID e Criar uma SERIAL:**
   - Este trecho de código remove a tabela `pessoas` existente (se houver) e a recria com uma coluna `id` do tipo `SERIAL`, que é uma sequência autoincrementada. Essa abordagem é mais rápida para gerar valores de ID do que o uso de UUIDs.
   - Exemplo:
     ```sql
     CREATE TABLE pessoas (
         id SERIAL PRIMARY KEY,
         first_name VARCHAR(3),
         last_name VARCHAR(3)
     );
     ```

4. **Inserção de 1 Milhão de Registros:**
   - Este trecho de código insere 1 milhão de registros na tabela `pessoas`, gerando valores aleatórios para as colunas `first_name` e `last_name`.
   - Exemplo:
     ```sql
     INSERT INTO pessoas (first_name, last_name)
     SELECT 
         substring(md5(random()::text), 0, 3),
         substring(md5(random()::text), 0, 3)
     FROM 
         generate_series(1, 1000000);
     ```

5. **Explicação sobre a Velocidade de Geração entre SERIAL e UUID:**

Uma das razões pelas quais uma coluna do tipo `serial` é mais rápida para gerar do que uma coluna do tipo `UUID` é a forma como os valores são criados e armazenados.

1. **Serial:**
   - Uma coluna do tipo `serial` é uma sequência numérica que é automaticamente incrementada pelo PostgreSQL. Quando uma nova linha é inserida na tabela e não é especificado um valor para essa coluna, o PostgreSQL gera automaticamente o próximo número na sequência e o atribui à coluna. Esse processo é altamente eficiente, pois não envolve cálculos complicados ou geração de valores aleatórios.

2. **UUID:**
   - Por outro lado, uma coluna do tipo `UUID` geralmente armazena identificadores únicos universais (UUIDs), que são cadeias de caracteres alfanuméricos de 128 bits (ou 16 bytes) gerados usando um algoritmo específico. A geração de um UUID geralmente envolve cálculos mais complexos e aleatórios para garantir que os valores sejam únicos globalmente. Isso pode ser mais demorado em comparação com a simples incrementação de um número inteiro.

Em resumo, a geração de valores para uma coluna do tipo `serial` é mais rápida porque envolve apenas a incrementação de um número, enquanto a geração de valores para uma coluna do tipo `UUID` pode ser mais demorada devido à complexidade do algoritmo de geração e à aleatoriedade necessária para garantir a unicidade global.

Verificando o tempo e buscando somente index

Claro, aqui está o texto aprimorado com mais contexto:

---

**Verificando o tempo e buscando somente pelo índice:**

```sql
SELECT id FROM pessoas WHERE id = 100000;
EXPLAIN ANALYZE SELECT id FROM pessoas WHERE id = 100000;
```

Ao executar essas consultas, estamos analisando o desempenho da busca direta por um registro específico na tabela `pessoas`. Como estamos consultando apenas o índice associado à coluna `id`, esperamos uma execução rápida e eficiente, já que o banco de dados pode usar diretamente o índice para localizar o registro desejado.

**Buscando somente pelo índice, mas observando os detalhes da tabela:**

```sql
SELECT first_name FROM pessoas WHERE id = 100000;
EXPLAIN ANALYZE SELECT first_name FROM pessoas WHERE id = 100000;
```

Nesse caso, mesmo que estejamos consultando apenas o índice da coluna `id`, estamos selecionando uma coluna adicional, `first_name`, da tabela `pessoas`. Isso pode resultar em uma consulta mais lenta, pois o banco de dados pode precisar acessar as páginas de dados da tabela para recuperar os valores de `first_name` associados aos registros encontrados no índice.

**Buscando e trazendo dados da tabela de maneira eficiente:**

```sql
SELECT first_name FROM pessoas WHERE first_name = 'aa';
```

Agora estamos buscando registros na tabela `pessoas` com base no valor exato de `first_name`. Se houver um índice na coluna `first_name`, essa consulta deve ser executada de maneira rápida e eficiente, pois o banco de dados pode usar o índice para localizar diretamente os registros correspondentes.

**Buscando e trazendo dados da tabela da pior maneira possível:**

```sql
SELECT first_name FROM pessoas WHERE first_name LIKE '%a%';
```

Nesta consulta, estamos buscando por valores parciais de `first_name` usando a cláusula `LIKE`. Esta consulta pode ser significativamente mais lenta, especialmente em grandes conjuntos de dados, pois não aproveita eficientemente os índices. O `%` no padrão de correspondência significa que estamos buscando por qualquer valor que contenha o caractere 'a' em qualquer posição da coluna `first_name`, o que pode resultar em uma varredura completa da tabela.

**Criando nosso índice:**

```sql
CREATE INDEX first_name_index ON pessoas(first_name);
```

Aqui estamos criando um índice na coluna `first_name` da tabela `pessoas`, o que nos permitirá otimizar consultas que buscam por valores nessa coluna.

**Comparação após a criação do índice:**

```sql
SELECT first_name FROM pessoas WHERE first_name = 'aa';
```

Agora, após a criação do índice na coluna `first_name`, vamos comparar novamente a consulta que busca por valores exatos de `first_name`. Com o índice em vigor, esperamos uma melhoria significativa no desempenho dessa consulta.

**Comparando agora com o operador LIKE:**

```sql
SELECT first_name FROM pessoas WHERE first_name LIKE '%aa%';
``` 

Nesta consulta, estamos buscando valores parciais de first_name que contenham a sequência 'aa' em qualquer posição. Embora tenhamos criado um índice na coluna first_name, o operador LIKE com o uso de % antes e depois do padrão de correspondência '%aa%' não pode fazer uso eficiente desse índice.

Varredura Completa da Tabela: O operador LIKE com um % no início do padrão significa que o banco de dados precisa verificar cada valor na coluna first_name para encontrar aqueles que contêm a sequência 'aa' em qualquer posição. Isso pode exigir uma varredura completa da tabela, mesmo com um índice criado na coluna.

Uso Ineficiente do Índice: O índice criado na coluna first_name é mais útil para consultas que buscam por valores exatos ou prefixos específicos. No entanto, como o padrão de correspondência '%aa%' não possui um prefixo definido, o otimizador de consultas pode optar por não utilizar o índice, pois uma varredura completa

## Entendendo um pouco mais do Explain

Aqui estão exemplos de consultas e suas respectivas saídas explicadas usando o comando `EXPLAIN`:

1. **Consulta simples:**
```sql
EXPLAIN SELECT * FROM pessoas;
```
Essa consulta irá explicar como o PostgreSQL planeja executar a consulta `SELECT * FROM pessoas`, que simplesmente seleciona todas as colunas da tabela `pessoas`. O resultado pode incluir informações sobre como o PostgreSQL acessa os dados na tabela, como pode ser feito um scan sequencial (percorrer todas as linhas) ou se algum índice será utilizado.

2. **Consulta com ordenação por `id`:**
```sql
EXPLAIN SELECT * FROM pessoas ORDER BY id;
```
Esta consulta adiciona uma cláusula `ORDER BY id`, que ordena os resultados da consulta com base na coluna `id`. O resultado do `EXPLAIN` mostrará como o PostgreSQL planeja executar a ordenação, se um índice na coluna `id` pode ser utilizado e se a ordenação será feita em memória ou em disco.

3. **Consulta com ordenação por `last_name`:**
```sql
EXPLAIN SELECT * FROM pessoas ORDER BY last_name;
```
Similar ao exemplo anterior, esta consulta adiciona uma cláusula `ORDER BY last_name`, que ordena os resultados da consulta com base na coluna `last_name`. O resultado do `EXPLAIN` mostrará como o PostgreSQL planeja executar a ordenação, se um índice na coluna `last_name` pode ser utilizado e como a ordenação será realizada.

Ao analisar a saída do comando `EXPLAIN`, você pode identificar oportunidades de otimização de consulta, como a criação de índices adicionais, ajustes na configuração do banco de dados ou alterações na estrutura da consulta para melhorar o desempenho.

Claro, vou explicar as diferenças entre as operações de busca em índices e varredura de tabelas no contexto do PostgreSQL, e fornecer exemplos de consultas que resultam em cada tipo de operação.

1. **Table Scan (Varredura de Tabela):**
   - A varredura de tabela ocorre quando o PostgreSQL precisa examinar todas as linhas de uma tabela para atender a uma consulta. Isso pode acontecer quando não há índices adequados para a consulta ou quando o custo de usar um índice é maior do que o de percorrer a tabela inteira.
   - Exemplo:
     ```sql
     SELECT * FROM pessoas;
     ```

2. **Index Scan (Varredura de Índice):**
   - Uma varredura de índice ocorre quando o PostgreSQL utiliza um índice para acessar as linhas de uma tabela que satisfazem os critérios da consulta. O banco de dados pode usar um índice se este for mais eficiente do que uma varredura de tabela.
   - Exemplo:
     ```sql
     SELECT * FROM pessoas WHERE id = 100;
     ```
   - Se houver um índice na coluna `id`, o PostgreSQL pode realizar uma varredura de índice para localizar rapidamente as linhas com `id` igual a 100.

3. **Bitmap Index Scan (Varredura de Bitmap de Índice):**
   - Uma varredura de bitmap de índice é uma técnica utilizada pelo PostgreSQL para combinar múltiplos índices em uma única operação. Em vez de procurar diretamente nas linhas da tabela, o PostgreSQL primeiro gera "bitmaps" para cada índice individualmente, representando as linhas que satisfazem os critérios da consulta. Em seguida, ele combina esses bitmaps para encontrar as linhas que satisfazem todos os critérios.
   - Exemplo:
     ```sql
     SELECT id, first_name FROM pessoas WHERE id = 100 OR first_name = 'aa';
     ```
   - Se houver índices separados nas colunas `id` e `first_name`, o PostgreSQL pode realizar uma varredura de bitmap de índice para encontrar as linhas que têm tanto `id` igual a 100 quanto `first_name` igual a 'aa'.

Claro, vou explicar o `Index Only Scan` (Varredura Apenas no Índice) e fornecer um exemplo de consulta que resulta nesse tipo de operação.

5. **Index Only Scan (Varredura Apenas no Índice):**

- O `Index Only Scan` ocorre quando o PostgreSQL pode satisfazer uma consulta apenas usando os dados armazenados no índice, sem a necessidade de acessar a tabela subjacente. Isso é possível quando todas as colunas necessárias para a consulta estão presentes no índice, o que elimina a necessidade de acessar as páginas de dados da tabela.
- Esse tipo de operação é particularmente eficiente, pois reduz a quantidade de E/S (entrada/saída) necessária para atender à consulta, já que apenas o índice precisa ser lido em vez da tabela inteira.
- Para que um `Index Only Scan` ocorra, todas as colunas na cláusula `SELECT` devem ser cobertas pelo índice. Além disso, não deve haver nenhuma coluna não indexada referenciada na consulta.
- Este tipo de operação é especialmente útil para consultas que precisam apenas de colunas indexadas e podem melhorar significativamente o desempenho em comparação com um `Index Scan` ou `Bitmap Index Scan` seguido de uma consulta à tabela.
- Exemplo:
  ```sql
  SELECT first_name FROM pessoas WHERE first_name = 'aa';
  ```
  Se houver um índice na coluna `first_name` e se todas as consultas de seleção envolverem apenas a coluna `first_name`, o PostgreSQL pode usar um `Index Only Scan` para atender a essas consultas, acessando apenas o índice e não a tabela subjacente.

O `Index Only Scan` é uma operação de busca muito eficiente quando todas as colunas necessárias para a consulta estão cobertas pelo índice, resultando em uma redução significativa na quantidade de E/S necessária para atender à consulta.

Vamos examinar cada parte em detalhes:

1. **Custo do Índice:**
   - Este trecho de código calcula o tamanho em disco ocupado pelo índice `first_name_index`. O resultado será exibido em uma unidade de tamanho legível, como KB, MB ou GB. Isso pode ser útil para entender o impacto do índice no armazenamento do banco de dados.
   - Exemplo:
     ```sql
     SELECT pg_size_pretty(pg_relation_size('first_name_index'));
     ```
   - Este comando retornará o tamanho ocupado pelo índice `first_name_index` em disco.

2. **Tamanho Total da Coluna:**
   - Este trecho de código calcula o tamanho total ocupado pela coluna `first_name` em todas as linhas da tabela `pessoas`. O resultado será exibido em uma unidade de tamanho legível, como KB, MB ou GB. Isso pode ser útil para entender quanto espaço a coluna está consumindo no banco de dados.
   - Exemplo:
     ```sql
     SELECT pg_size_pretty(pg_column_size(first_name)::bigint) AS tamanho_total
     FROM pessoas;
     ```
   - Este comando retornará o tamanho total ocupado pela coluna `first_name` em todas as linhas da tabela `pessoas`.

3. **Tamanho Total de Todas as Colunas:**
   - Este trecho de código calcula o tamanho total ocupado por todas as colunas em todas as linhas da tabela `pessoas`. Ele soma os tamanhos individuais de todas as colunas e retorna o resultado em uma unidade de tamanho legível, como KB, MB ou GB. Isso pode ser útil para entender quanto espaço total a tabela está consumindo no banco de dados.
   - Exemplo:
     ```sql
     SELECT pg_size_pretty(SUM(pg_column_size(first_name)::bigint)) AS tamanho_total
     FROM pessoas;
     ```
   - Este comando retornará o tamanho total ocupado por todas as linhas em todas as colunas da tabela `pessoas`.