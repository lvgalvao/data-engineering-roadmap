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
WHERE EXTRACT(YEAR FROM o.order_date) = 1996; -- EXTRACT(part FROM date) part pode ser YEAR, MONTH, DAY, etc
```

Gustavo trouxe tambem essa implementacao

'WHERE DATE_PART('YEAR', o.order_date) = 1996'

No SQL server pode usar o 

'WHERE YEAR(o.order_date) = 1996'

No contexto da sua consulta, o uso de EXTRACT na cláusula WHERE serve especificamente para aplicar um filtro nos dados retornados pelo SELECT, garantindo que apenas registros do ano de 1996 sejam incluídos no conjunto de resultados. Este é um uso legítimo e comum de EXTRACT para manipulação de condições baseadas em datas dentro de cláusulas WHERE.

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

### Exemplo de Resultados da Consulta

| cidade | numero_de_funcionarios | numero_de_clientes |
| --- | --- | --- |
| Kirkland | 1 | 1 |
| London | 4 | 6 |
| Redmond | 1 | 0 |
| Seattle | 2 | 1 |
| Tacoma | 1 | 0 |

### Descrição da Tabela

* **cidade**: O nome da cidade onde os funcionários e clientes estão localizados.
* **numero_de_funcionarios**: Contagem dos funcionários distintos nessa cidade. Este número vem diretamente da tabela `employees`.
* **numero_de_clientes**: Contagem dos clientes distintos que têm a mesma cidade que os funcionários. Se não houver clientes em uma cidade onde há funcionários, o número será 0.

### Explicação Detalhada

* **Kirkland**: Tem um equilíbrio entre o número de funcionários e clientes, com ambos os valores sendo 1. Isso indica uma correspondência direta entre locais de funcionários e clientes.
* **London**: Apresenta uma maior concentração tanto de funcionários quanto de clientes, com mais clientes (6) do que funcionários (4), indicando uma forte presença de ambos na cidade.
* **Redmond**: Tem 1 funcionário, mas nenhum cliente registrado nesta cidade, sugerindo que, embora a empresa tenha presença laboral aqui, não há clientes registrados.
* **Seattle**: Tem 2 funcionários e apenas 1 cliente, mostrando uma presença menor de clientes em relação aos funcionários.
* **Tacoma**: Similar a Redmond, tem funcionários (1) mas nenhum cliente, o que pode indicar uma área onde a empresa opera, mas ainda não estabeleceu uma base de clientes.

Essa análise é particularmente útil para entender como os recursos humanos da empresa (funcionários) estão distribuídos em relação à sua base de clientes em diferentes locais. Isso pode ajudar a identificar cidades onde a empresa pode precisar intensificar esforços de aquisição de clientes ou avaliar a eficácia de suas operações e estratégias de mercado locais.


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

### Diferenças Principais do `RIGHT JOIN`

1. **Foco na Tabela à Direita**: Ao contrário do `LEFT JOIN` que foca na tabela à esquerda, o `RIGHT JOIN` garante que todos os registros da tabela à direita (neste caso, `customers`) estejam presentes no resultado. Se não houver correspondência na tabela à esquerda (`employees`), as colunas relacionadas desta tabela aparecerão como `NULL`.
    
2. **Exibição de Dados Não Correspondentes**: Como mostrado, o `RIGHT JOIN` pode exibir linhas onde não há correspondência na tabela à esquerda, o que é útil para identificar dados que estão apenas na tabela à direita. No contexto de um negócio, isso pode destacar áreas (ou dados) que requerem atenção, como clientes em locais onde a empresa não tem funcionários representados.
    
3. **Utilização Estratégica para Análise de Dados**: O `RIGHT JOIN` é menos comum que o `LEFT JOIN` porque muitas vezes as tabelas são organizadas de modo que a tabela mais importante (ou abrangente) seja colocada à esquerda da consulta. No entanto, o `RIGHT JOIN` é útil quando a tabela à direita é prioritária e queremos garantir que todos os seus registros sejam analisados.


### 4. Criar um relatório que mostra o número de funcionários e clientes de cada cidade

* **Análise Completa de Dados**: O `FULL JOIN` é útil quando você precisa de uma visão completa dos dados em duas tabelas relacionadas, especialmente para identificar onde os dados estão faltando em uma ou ambas as tabelas.
* **Relatórios Abrangentes**: Permite criar relatórios que mostram todas as possíveis relações entre duas tabelas, incluindo onde as relações não existem.
* **Análise de Lacunas de Dados**: Ajuda a identificar lacunas nos dados de ambas as tabelas simultaneamente, facilitando análises de cobertura e consistência entre conjuntos de dados.

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

Esta consulta retorna uma lista de todas as cidades conhecidas por ambas as tabelas, junto com a contagem de funcionários e clientes em cada cidade. Aqui estão alguns cenários possíveis no resultado:

### Análise do Resultado

O resultado do `FULL JOIN` mostra:

* A maioria das cidades listadas tem clientes, mas não funcionários (indicado por "0" no número de funcionários).
* Em algumas cidades, como "Kirkland", "Redmond", "Seattle", e "Tacoma", há funcionários e/ou clientes, mostrando correspondência direta entre as tabelas.
* Notavelmente, em cidades como "London" e "Madrid", o número de clientes é significativamente maior do que o de funcionários, o que pode indicar centros de alta atividade de clientes sem uma proporção correspondente de suporte de funcionários.

### Observações Importantes

1. **Cidades com apenas Clientes**: A maioria das cidades no resultado possui clientes, mas não funcionários. Isso pode sugerir que a empresa tem uma ampla base de clientes geograficamente, mas uma distribuição mais limitada de sua força de trabalho.
    
2. **Cidades com Funcionários e sem Clientes**: Cidades como "Redmond" e "Tacoma" têm funcionários, mas nenhuma contagem de clientes listada, indicando que há operações da empresa sem correspondente atividade de clientes registrada nesses locais.
    
3. **Concentrações de Clientes e Funcionários**: Em cidades como "London", "Seattle", e "Sao Paulo", há uma concentração significativa de clientes e alguma presença de funcionários, sugerindo centros operacionais ou mercados importantes para a empresa.
    
4. **Ausência de Dados em Algumas Cidades**: Algumas cidades têm zero funcionários e clientes, indicando que pode haver um erro de dados, cidades listadas incorretamente, ou simplesmente que não há atividade de funcionários ou clientes registrados nesses locais.
    

### Implicações Estratégicas

A partir desses dados, a empresa poderia considerar várias ações estratégicas:

* **Expansão de Funcionários**: Investir em recursos humanos nas cidades com altos números de clientes, mas baixa presença de funcionários, para melhorar o suporte e a satisfação do cliente.
    
* **Análise de Mercado**: Realizar uma análise mais aprofundada sobre por que certas cidades têm alta atividade de clientes e ajustar as estratégias de marketing e vendas conforme necessário.
    
* **Revisão de Dados**: Verificar a precisão dos dados para entender melhor as discrepâncias ou ausências nas contagens de funcionários e clientes.
    
Este exemplo realça o valor de usar `FULL JOIN` para obter uma visão completa da relação entre duas variáveis críticas (funcionários e clientes) e como essa informação pode ser usada para insights estratégicos.

## Having

### 1. Criar um relatório que mostra a quantidade total de produtos (da tabela order_details)

```sql
-- Cria um relatório que mostra a quantidade total de produtos encomendados.
-- Mostra apenas registros para produtos para os quais a quantidade encomendada é menor que 200 (5 linhas)
SELECT o.product_id, p.product_name, SUM(o.quantity) AS quantidade_total
FROM order_details o
JOIN products p ON p.product_id = o.product_id
GROUP BY o.product_id, p.product_name
HAVING SUM(o.quantity) < 200
ORDER BY quantidade_total DESC;
```

### 2. Criar um relatório que mostra o total de pedidos por cliente desde 31 de dezembro de 1996

```sql
-- Cria um relatório que mostra o total de pedidos por cliente desde 31 de dezembro de 1996.
-- O relatório deve retornar apenas linhas para as quais o total de pedidos é maior que 15 (5 linhas)
SELECT customer_id, COUNT(order_id) AS total_de_pedidos
FROM orders
WHERE order_date > '1996-12-31'
GROUP BY customer_id
HAVING COUNT(order_id) > 15
ORDER BY total_de_pedidos;
```

### Explicação das Consultas Convertidas

**Consulta 1:**

* **Seleção e Junção**: A consulta seleciona o `product_id` e `product_name` da tabela `products` e junta com a tabela `order_details` pelo `product_id`.
* **Agrupamento e Filtragem**: Os dados são agrupados por `product_id` e `product_name`, e a função agregada `SUM(o.quantity)` calcula a quantidade total de cada produto encomendado. A cláusula `HAVING` é usada para filtrar produtos cuja quantidade total encomendada é menor que 200.

**Consulta 2:**

* **Filtragem de Data**: A consulta filtra os pedidos realizados após 31 de dezembro de 1996.
* **Agrupamento e Contagem**: Agrupa os pedidos pelo `customer_id` e conta o número de pedidos feitos por cada cliente usando `COUNT(order_id)`.
* **Filtragem de Resultados**: Utiliza a cláusula `HAVING` para incluir apenas os clientes que fizeram mais de 15 pedidos desde a data especificada.