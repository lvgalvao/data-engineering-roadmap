# Aula 04 - Windows Function

Documentação Postgres:  https://www.postgresql.org/docs/current/functions-window.html

## Com o que vimos até aqui: Group By

Com SQL que vimos até agora conseguimos dois tipos de resultado: todas as linhas (com ou sem filtro/where) ou linhas agrupadas (group by)

Cálcular:
Quantos produtos únicos existem?
Quantos produtos no total?
Qual é o valor total pago?

```sql
SELECT order_id,
       COUNT(order_id) AS unique_product,
       SUM(quantity) AS total_quantity,
       SUM(unit_price * quantity) AS total_price
FROM order_details
GROUP BY order_id
ORDER BY order_id;
```

## Com Windows Function

As `Windows Function` permitem uma análise de dados eficiente e precisa, ao possibilitar cálculos dentro de `partições ou linhas específicas`. Elas são cruciais para tarefas como classificação, agregação e análise de tendências em consultas SQL.

Essas funções são aplicadas a cada linha de um conjunto de resultados, e utilizam uma cláusula `OVER()` para determinar como cada linha é processada dentro de uma "janela", permitindo controle sobre o comportamento da função dentro de um grupo de dados ordenados.

Window Functions Syntax componentes
```sql
window_function_name(arg1, arg2, ...) OVER (
  [PARTITION BY partition_expression, ...]
  [ORDER BY sort_expression [ASC | DESC], ...]
)
```

* **window_function_name**: Este é o nome da função de janela que você deseja usar, como SUM, RANK, LEAD, etc.

* **arg1, arg2, ...:** Estes são os argumentos que você passa para a função de janela, se ela exigir algum. Por exemplo, para a função SUM, você especificaria a coluna que deseja somar.

* **OVER**: Principal conceito das windows functions, ele que cria essa "Janela" onde fazem nossos cálculos

* **PARTITION BY:** Esta cláusula opcional divide o conjunto de resultados em partições ou grupos. A função de janela opera independentemente dentro de cada partição.

* **ORDER BY:** Esta cláusula opcional especifica a ordem em que as linhas são processadas dentro de cada partição. Você pode especificar a ordem ascendente (ASC) ou descendente (DESC).

```sql
SELECT DISTINCT order_id,
   COUNT(order_id) OVER (PARTITION BY order_id) AS unique_product,
   SUM(quantity) OVER (PARTITION BY order_id) AS total_quantity,
   SUM(unit_price * quantity) OVER (PARTITION BY order_id) AS total_price
FROM order_details
ORDER BY order_id;
```

## MIN (), MAX (), AVG ()

Quais são os valores mínimo, máximo e médio de frete pago por cada cliente? (tabela orders)

### Usando Group by

```sql
SELECT customer_id,
   MIN(freight) AS min_freight,
   MAX(freight) AS max_freight,
   AVG(freight) AS avg_freight
FROM orders
GROUP BY customer_id
ORDER BY customer_id;
```

### Detalhes da Consulta Ajustada:

* **`customer_id`**: Seleciona o identificador único do cliente da tabela `orders`.
* **`MIN(freight) AS min_freight`**: Calcula o valor mínimo de frete para cada cliente.
* **`MAX(freight) AS max_freight`**: Calcula o valor máximo de frete para cada cliente.
* **`AVG(freight) AS avg_freight`**: Calcula o valor médio de frete para cada cliente.

### Explicação:

* A função `MIN` extrai o menor valor de frete registrado para cada cliente.
* A função `MAX` obtém o maior valor de frete registrado para cada cliente.
* A função `AVG` fornece o valor médio de frete por cliente, útil para entender o custo médio de envio associado a cada um.
* `GROUP BY customer_id` agrupa os registros por `customer_id`, permitindo que as funções agregadas calculem seus resultados para cada grupo de cliente.
* `ORDER BY customer_id` garante que os resultados sejam apresentados em ordem crescente de `customer_id`, facilitando a leitura e a análise dos dados.

### Usando Windows Function

```sql
SELECT DISTINCT customer_id,
   MIN(freight) OVER (PARTITION BY customer_id) AS min_freight,
   MAX(freight) OVER (PARTITION BY customer_id) AS max_freight,
   AVG(freight) OVER (PARTITION BY customer_id) AS avg_freight
FROM orders
ORDER BY customer_id;
```

### Explicação da Consulta Ajustada:

* **`customer_id`**: Seleciona o identificador único do cliente da tabela `orders`.
* **`MIN(freight) OVER (PARTITION BY customer_id)`**: Utiliza a função de janela `MIN` para calcular o valor mínimo de frete para cada grupo de registros que têm o mesmo `customer_id`.
* **`MAX(freight) OVER (PARTITION BY customer_id)`**: Utiliza a função de janela `MAX` para calcular o valor máximo de frete para cada `customer_id`.
* **`AVG(freight) OVER (PARTITION BY customer_id)`**: Utiliza a função de janela `AVG` para calcular o valor médio de frete para cada `customer_id`.

### Características das Funções de Janela:

* **Funções de Janela (`OVER`)**: As funções de janela permitem que você execute cálculos sobre um conjunto de linhas relacionadas a cada entrada. Ao usar o `PARTITION BY customer_id`, a função de janela é reiniciada para cada novo `customer_id`. Isso significa que cada cálculo de `MIN`, `MAX`, e `AVG` é confinado ao conjunto de ordens de cada cliente individualmente.
* **`DISTINCT`**: A cláusula `DISTINCT` é utilizada para garantir que cada `customer_id` apareça apenas uma vez nos resultados finais, juntamente com seus respectivos valores de frete mínimo, máximo e médio. Isso é necessário porque as funções de janela calculam valores para cada linha, e sem `DISTINCT`, cada `customer_id` poderia aparecer múltiplas vezes se houver várias ordens por cliente.

## Colapso

Para ilustrar como a cláusula `GROUP BY` influencia os resultados de uma consulta SQL e por que ela pode "colapsar" as linhas para uma única linha por grupo, vou dar um exemplo baseado nas funções de agregação `MIN`, `MAX`, e `AVG` que discutimos anteriormente. Essas funções são frequentemente usadas para calcular estatísticas resumidas dentro de cada grupo especificado por `GROUP BY`.

### Exemplo sem GROUP BY

Considere a seguinte consulta sem usar `GROUP BY`:

```sql 
-- 830 linhas
SELECT customer_id, freight
FROM orders;
```

Essa consulta simplesmente seleciona o `customer_id` e o `freight` de cada ordem. Se houver múltiplas ordens para cada cliente, cada ordem aparecerá como uma linha separada no conjunto de resultados.

### Exemplo com GROUP BY

Agora, vamos adicionar `GROUP BY` e funções de agregação:

```sql
-- 89 linhas
SELECT customer_id,
       MIN(freight) AS min_freight,
       MAX(freight) AS max_freight,
       AVG(freight) AS avg_freight
FROM orders
GROUP BY customer_id
ORDER BY customer_id;
```

### O que acontece aqui:

* **`GROUP BY customer_id`**: Esta cláusula agrupa todas as entradas na tabela `orders` que têm o mesmo `customer_id`. Para cada grupo, a consulta calcula os valores mínimo, máximo e médio de `freight`.
    
* **Agregações (`MIN`, `MAX`, `AVG`)**: Cada uma dessas funções de agregação opera sobre o conjunto de `freight` dentro do grupo especificado pelo `customer_id`. Apenas um valor para cada função de agregação é retornado por grupo.
    

### Por que "colapsa" as linhas:

* Quando usamos `GROUP BY`, a consulta não retorna mais uma linha para cada entrada na tabela `orders`. Em vez disso, ela retorna uma linha para cada grupo de `customer_id`, onde cada linha contém o `customer_id` e os valores agregados de `freight` para esse grupo. Isso significa que se um cliente tem várias ordens, você não verá cada ordem individualmente; em vez disso, você verá uma linha resumida com as estatísticas de frete para todas as ordens desse cliente.

### Limitação do SELECT com GROUP BY:

* Se você tentar selecionar uma coluna que não está incluída na cláusula `GROUP BY` e que não é uma expressão agregada, a consulta falhará. Por exemplo, a consulta a seguir resultará em erro porque `order_date` não está em uma função agregada nem no `GROUP BY`:

```sql
SELECT customer_id, order_date, AVG(freight) AS avg_freight
FROM orders
GROUP BY customer_id;
```

### Mensagem de Erro Típica:

* Em muitos sistemas de gerenciamento de banco de dados, como PostgreSQL ou MySQL, essa consulta resultaria em um erro como: "column "orders.order_date" must appear in the GROUP BY clause or be used in an aggregate function".

Este exemplo mostra claramente como o `GROUP BY` "colapsa" as linhas em grupos, permitindo cálculos resumidos, mas também impõe restrições sobre quais colunas podem ser selecionadas diretamente.

Para ilustrar como evitar o "colapso" das linhas utilizando funções de janela (window functions) em vez de `GROUP BY`, vamos utilizar as mesmas estatísticas de frete (mínimo, máximo e médio) por cliente, mas manter todas as linhas de pedidos individuais visíveis no conjunto de resultados. As funções de janela permitem calcular agregações enquanto ainda se mantém cada linha distinta na saída.

### Consulta com Funções de Janela

Aqui está como você pode escrever uma consulta que utiliza funções de janela para calcular o frete mínimo, máximo e médio para cada cliente sem colapsar as linhas:

```sql
SELECT 
    customer_id,
    order_id,  -- Mantendo a visibilidade de cada pedido
    freight,
    MIN(freight) OVER (PARTITION BY customer_id) AS min_freight,
    MAX(freight) OVER (PARTITION BY customer_id) AS max_freight,
    AVG(freight) OVER (PARTITION BY customer_id) AS avg_freight
FROM orders
ORDER BY customer_id, order_id;
```

### Explicação da Consulta

* **Seleção de Colunas**: `customer_id`, `order_id`, e `freight` são selecionados diretamente, o que mantém cada linha de pedido individual visível no resultado.
* **Funções de Janela**: `MIN(freight) OVER`, `MAX(freight) OVER`, e `AVG(freight) OVER` são aplicadas com a cláusula `PARTITION BY customer_id`. Isso significa que as estatísticas de frete são calculadas para cada grupo de `customer_id`, mas a aplicação é feita sem agrupar as linhas em um único resultado por cliente. Cada linha no conjunto de resultados original mantém sua identidade única.
* **`PARTITION BY customer_id`**: Assegura que as funções de janela são recalculadas para cada cliente. Cada pedido mantém sua linha, mas agora também inclui as informações agregadas de frete específicas para o cliente ao qual o pedido pertence.
* **`ORDER BY customer_id, order_id`**: Ordena os resultados primeiro por `customer_id` e depois por `order_id`, facilitando a leitura dos dados.

### Vantagens das Funções de Janela

* **Preservação de Dados Detalhados**: Ao contrário do `GROUP BY`, que agrega e reduz os dados a uma linha por grupo, as funções de janela mantêm cada linha individual do conjunto de dados original visível. Isso é útil para análises detalhadas onde você precisa ver tanto os valores agregados quanto os dados de linha individual.
* **Flexibilidade**: Você pode calcular múltiplas métricas de agregação em diferentes partições dentro da mesma consulta sem múltiplas passagens pelos dados ou subconsultas complexas.

Este método é especialmente útil em relatórios e análises detalhadas onde tanto o contexto agregado quanto os detalhes de cada evento individual (neste caso, cada pedido) são importantes para uma compreensão completa dos dados.

Funções de classificação de janela no SQL são um conjunto de ferramentas valiosas usadas para atribuir classificações, posições ou números sequenciais às linhas dentro de um conjunto de resultados com base em critérios específicos.

Elas são aplicadas em vários cenários, como criar leaderboards, classificar produtos por vendas, identificar os melhores desempenhos ou acompanhar mudanças ao longo do tempo. Essas funções são ferramentas poderosas para obter insights e tomar decisões informadas na análise de dados.

### 2.1 RANK(), DENSE_RANK() e ROW_NUMBER()

* **RANK()**: Atribui um rank único a cada linha, deixando lacunas em caso de empates.
* **DENSE_RANK()**: Atribui um rank único a cada linha, com ranks contínuos para linhas empatadas.
* **ROW_NUMBER()**: Atribui um número inteiro sequencial único a cada linha, independentemente de empates, sem lacunas.

### Exemplo: Classificação dos produtos mais venvidos POR order ID

ex: o mesmo produto pode ficar em primeiro por ter vendido muito por ORDER e depois ficar em segundo por ter vendido muito por ORDER

```sql
SELECT  
  o.order_id, 
  p.product_name, 
  (o.unit_price * o.quantity) AS total_sale,
  ROW_NUMBER() OVER (ORDER BY (o.unit_price * o.quantity) DESC) AS order_rn, 
  RANK() OVER (ORDER BY (o.unit_price * o.quantity) DESC) AS order_rank, 
  DENSE_RANK() OVER (ORDER BY (o.unit_price * o.quantity) DESC) AS order_dense
FROM  
  order_details o
JOIN 
  products p ON p.product_id = o.product_id;
```

### Explicação da Consulta

* **Seleção de Dados**: A consulta seleciona o `order_id`, `product_name` da tabela `products`, e calcula `total_sale` como o produto de `unit_price` e `quantity` da tabela `order_details`.
    
* **Funções de Classificação**:
    
    * **`ROW_NUMBER()`**: Atribui um número sequencial a cada linha baseada no total de vendas (`total_sale`), ordenado do maior para o menor. Cada linha recebe um número único dentro do conjunto de resultados inteiro.
    * **`RANK()`**: Atribui um rank a cada linha baseado no `total_sale`, onde linhas com valores iguais recebem o mesmo rank, e o próximo rank disponível considera os empates (por exemplo, se dois itens compartilham o primeiro lugar, o próximo item será o terceiro).
    * **`DENSE_RANK()`**: Funciona de forma similar ao `RANK()`, mas os ranks subsequentes não têm lacunas. Se dois itens estão empatados no primeiro lugar, o próximo item será o segundo.
* **`JOIN`**: A junção entre `order_details` e `products` é feita pelo `product_id`, permitindo que o nome do produto seja incluído nos resultados baseados nos IDs correspondentes em ambas as tabelas.
    
## Este relatório apresenta o ID de cada pedido juntamente com o total de vendas e a classificação percentual e a distribuição cumulativa do valor de cada venda em relação ao valor total das vendas para o mesmo pedido. Esses cálculos são realizados com base no preço unitário e na quantidade de produtos vendidos em cada pedido.

### Exemplo: Classificação dos produtos mais venvidos usnado SUB QUERY

```sql
SELECT  
  sales.product_name, 
  total_sale,
  ROW_NUMBER() OVER (ORDER BY total_sale DESC) AS order_rn, 
  RANK() OVER (ORDER BY total_sale DESC) AS order_rank, 
  DENSE_RANK() OVER (ORDER BY total_sale DESC) AS order_dense
FROM (
  SELECT 
    p.product_name, 
    SUM(o.unit_price * o.quantity) AS total_sale
  FROM  
    order_details o
  JOIN 
    products p ON p.product_id = o.product_id
  GROUP BY p.product_name
) AS sales
ORDER BY sales.product_name;
```

### Utilidade da Consulta

Esta consulta é útil para análises de vendas, onde é necessário identificar os produtos mais vendidos, bem como sua classificação em termos de receita gerada. Ela permite que os analistas vejam rapidamente quais produtos geram mais receita e como eles se classificam em relação uns aos outros, facilitando decisões estratégicas relacionadas a estoque, promoções e planejamento de vendas.

### Funções PERCENT_RANK() e CUME_DIST()

Ambos retornam um valor entre 0 e 1

* **PERCENT_RANK()**: Calcula o rank relativo de uma linha específica dentro do conjunto de resultados como uma porcentagem. É computado usando a seguinte fórmula:
    * RANK é o rank da linha dentro do conjunto de resultados.
    * N é o número total de linhas no conjunto de resultados.
    * PERCENT_RANK = (RANK - 1) / (N - 1)
* **CUME_DIST()**: Calcula a distribuição acumulada de um valor no conjunto de resultados. Representa a proporção de linhas que são menores ou iguais à linha atual. A fórmula é a seguinte:
    * CUME_DIST = (Número de linhas com valores <= linha atual) / (Número total de linhas)

Ambas as funções PERCENT_RANK() e CUME_DIST() são valiosas para entender a distribuição e posição de pontos de dados dentro de um conjunto de dados, particularmente em cenários onde você deseja comparar a posição de um valor específico com a distribuição geral de dados.

```sql
SELECT  
  order_id, 
  unit_price * quantity AS total_sale,
  ROUND(CAST(PERCENT_RANK() OVER (PARTITION BY order_id 
    ORDER BY (unit_price * quantity) DESC) AS numeric), 2) AS order_percent_rank,
  ROUND(CAST(CUME_DIST() OVER (PARTITION BY order_id 
    ORDER BY (unit_price * quantity) DESC) AS numeric), 2) AS order_cume_dist
FROM  
  order_details;
```

### Explicação da Consulta Ajustada:

* **Seleção de Dados**: A consulta seleciona o `order_id` e calcula `total_sale` como o produto de `unit_price` e `quantity`.
* **Funções de Janela**:
    * **`PERCENT_RANK()`**: Aplicada com uma partição por `order_id` e ordenada pelo `total_sale` de forma descendente, calcula a posição percentual de cada venda em relação a todas as outras no mesmo pedido.
    * **`CUME_DIST()`**: Similarmente, calcula a distribuição acumulada das vendas, indicando a proporção de vendas que não excedem o `total_sale` da linha atual dentro de cada pedido.
* **Arredondamento**: Os resultados de `PERCENT_RANK()` e `CUME_DIST()` são arredondados para duas casas decimais para facilitar a interpretação.

Esta consulta é útil para análises detalhadas de desempenho de vendas dentro de pedidos, permitindo que gestores e analistas identifiquem rapidamente quais itens contribuem mais

A função NTILE() no SQL é usada para dividir o conjunto de resultados em um número especificado de partes aproximadamente iguais ou "faixas" e atribuir um número de grupo ou "bucket" a cada linha com base em sua posição dentro do conjunto de resultados ordenado.

```sql
NTILE(n) OVER (ORDER BY coluna)
```

* **n**: O número de faixas ou grupos que você deseja criar.
* **ORDER BY coluna**: A coluna pela qual você deseja ordenar o conjunto de resultados antes de aplicar a função NTILE().

### Exemplo: Listar funcionários dividindo-os em 3 grupos

```sql
SELECT first_name, last_name, title,
   NTILE(3) OVER (ORDER BY first_name) AS group_number
FROM employees;
```

### Explicação da Consulta Ajustada:

* **Seleção de Dados**: A consulta seleciona `first_name`, `last_name` e `title` da tabela `employees`.
* **NTILE(3) OVER (ORDER BY first_name)**: Aplica a função NTILE para dividir os funcionários em 3 grupos baseados na ordem alfabética de seus primeiros nomes. Cada funcionário receberá um número de grupo (`group_number`) que indica a qual dos três grupos ele pertence.

Esta consulta é útil para análises que requerem a distribuição equitativa dos dados em grupos especificados, como para balanceamento de cargas de trabalho, análises segmentadas, ou mesmo para fins de relatórios onde a divisão em grupos facilita a visualização e o entendimento dos dados.

LAG(), LEAD()

* **LAG()**: Permite acessar o valor da linha anterior dentro de um conjunto de resultados. Isso é particularmente útil para fazer comparações com a linha atual ou identificar tendências ao longo do tempo.
* **LEAD()**: Permite acessar o valor da próxima linha dentro de um conjunto de resultados, possibilitando comparações com a linha subsequente.

### Exemplo: Ordenando os custos de envio pagos pelos clientes de acordo com suas datas de pedido:

```sql
SELECT 
  customer_id, 
  TO_CHAR(order_date, 'YYYY-MM-DD') AS order_date, 
  shippers.company_name AS shipper_name, 
  LAG(freight) OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS previous_order_freight, 
  freight AS order_freight, 
  LEAD(freight) OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS next_order_freight
FROM 
  orders
JOIN 
  shippers ON shippers.shipper_id = orders.ship_via;
```

* **LEAD() e LAG(): Estas funções de janela são usadas para acessar dados de linhas anteriores ou subsequentes dentro de uma partição definida, muito úteis para comparar o valor de frete entre ordens consecutivas de um mesmo cliente.
