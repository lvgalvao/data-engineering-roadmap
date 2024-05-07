# Aula 11 : Ordem de consulta

Para maximizar a velocidade da sua consulta em qualquer mecanismo SQL, é essencial entender a ordem de execução do SQL. Embora seja possível trabalhar sem esse conhecimento, recomendo a leitura deste artigo para obter um entendimento rápido sobre isso.

O mecanismo SQL não segue a mesma ordem que você define na sua consulta, portanto, é crucial lembrar disso. Por exemplo, embora comecemos com uma instrução SELECT, o mecanismo não começará com esse comando. Neste artigo, examinaremos uma consulta complexa passo a passo para entender como o mecanismo SQL opera nos bastidores.

Importante: todos os exemplos são feitos no PostgreSQL, então as sintaxes podem variar de mecanismo para mecanismo. Ainda assim, esse conceito é aplicável a todos os outros tipos de mecanismos SQL.

Definir a Consulta
Para este exemplo, gostaria de discutir uma consulta típica usada em fluxos de trabalho do mundo real. Suponha que temos um banco de dados para carros com uma tabela para diferentes modelos, e cada modelo tem suas próprias especificações de motor listadas em uma tabela separada. Para ilustrar isso, podemos criar tabelas para este cenário.

```sql
DROP TABLE IF EXISTS cars, engines;
CREATE TABLE cars (
 manufacturer VARCHAR(64),
 model VARCHAR(64),
 country VARCHAR(64),
 engine_name VARCHAR(64),
 year INT
);
CREATE TABLE engines (
 name VARCHAR(64),
 horse_power INT
);

INSERT INTO cars
VALUES 
 ('BMW', 'M4', 'Germany', 'S58B30T0-353', 2021),
 ('BMW', 'M4', 'Germany', 'S58B30T0-375', 2021),
 ('Chevrolet', 'Corvette', 'USA', 'LT6', 2023),
 ('Chevrolet', 'Corvette', 'USA', 'LT2', 2023),
 ('Audi', 'R8', 'Germany', 'DOHC FSI V10-5.2-456', 2019),
 ('McLaren', 'GT', 'UK', 'M840TE', 2019),
 ('Mercedes', 'AMG C 63 S E', 'Germany', 'M139L', 2023);
 
INSERT INTO engines
VALUES 
 ('S58B30T0-353', 473),
 ('S58B30T0-375', 510),
 ('LT6', 670),
 ('LT2', 495),
 ('DOHC FSI V10-5.2-456', 612),
 ('M840TE', 612),
 ('M139L', 469);
```

Para alcançar nosso objetivo de identificar os dois carros mais potentes da Alemanha, estaremos olhando para automóveis modernos que não sejam mais antigos do que oito anos. Para isso, usaremos instruções SQL conhecidas como SELECT, FROM, JOIN, WHERE, GROUP BY, HAVING, ORDER BY e LIMIT.

```sql
SELECT
  cars.manufacturer,
  cars.model,
  cars.country,
  cars.year,
  MAX(engines.horse_power) as maximum_horse_power
FROM cars
JOIN engines ON cars.engine_name = engines.name
WHERE cars.year > 2015 AND cars.country = 'Germany'
GROUP BY cars.manufacturer, cars.model, cars.country, cars.year
HAVING MAX(engines.horse_power)> 200
ORDER BY maximum_horse_power DESC
LIMIT 2
```

Saída da consulta — os dois carros alemães mais potentes do nosso banco de dados de amostra

Agora que temos nossa consulta, vamos entender como o mecanismo a ordena ao executar. Aqui está a ordem:

1. FROM
2. JOIN (e ON)
3. WHERE
4. GROUP BY
5. HAVING
6. SELECT
7. ORDER BY
8. LIMIT

Fonte: https://blog.bytebytego.com/p/ep50-visualizing-a-sql-query

É importante notar que, antes de executar a consulta, o mecanismo SQL cria um plano de execução para reduzir o consumo de recursos. Este plano oferece detalhes valiosos como custos estimados, algoritmos de junção, ordem das operações e mais. Este é um resultado abrangente, e pode ser acessado se necessário.

Passo a Passo
FROM e JOIN
```sql
FROM cars
JOIN engines
```
Ao iniciar uma consulta SQL, o mecanismo precisa saber quais tabelas usar. Isso é realizado começando com uma instrução FROM. Você pode adicionar mais tabelas usando a palavra-chave JOIN,

 desde que compartilhem uma coluna comum que será usada na consulta. É um processo direto que você deve ter em mente.

ON
```sql
ON cars.engine_name = engines.name
```
A seguir na sequência vem o ON, onde definimos como juntar diferentes tabelas. Este processo também envolve o uso de índices pré-definidos, como B-tree e Bitmap, para acelerar os cálculos. É importante notar que existem vários tipos de índices que podem ajudar neste caso. Estas duas etapas requerem uma quantidade considerável de processamento, portanto, é crucial focar e começar a otimizar neste ponto.

WHERE
```sql
WHERE cars.year > 2015 AND cars.country = 'Germany'
```
Ao analisar nossos dados, é importante ter em mente que usar a cláusula WHERE apenas com colunas indexadas pode melhorar o desempenho, especialmente ao lidar com grandes tabelas. Além disso, pode ser benéfico filtrar dados em subconsultas ou CTEs antes da declaração WHERE em alguns cenários para aumentar ainda mais o desempenho.

No entanto, é importante notar que muitos problemas relacionados ao desempenho de consultas estão além do escopo deste artigo. Recomendo aprofundar-se nesses problemas e experimentar várias técnicas para escrever consultas mais rápidas.

GROUP BY e HAVING
```sql
GROUP BY cars.manufacturer, cars.model, cars.country, cars.year
HAVING MAX(engines.horse_power) > 200
```
A seguir na sequência, precisamos seguir a ordem especificada da consulta adequadamente. Depois disso, temos que determinar todas as agregações necessárias que temos que realizar. Quando se trata da cláusula HAVING, é intrigante porque não podemos empregar um alias da linha SELECT. Isso ocorre porque o motor SQL ainda não está ciente desta definição.

SELECT
```sql
SELECT
  cars.manufacturer,
  cars.model,
  cars.country,
  cars.year,
  MAX(engines.horse_power) as maximum_horse_power
```
Uma vez que todos os passos necessários foram completados, prosseguimos para executar a instrução SELECT. Neste ponto, simplesmente especificamos as colunas a serem incluídas na saída final. É importante ter em mente que muitas operações, como mesclagem e agregação, já foram concluídas nesta fase.

ORDER BY e LIMIT
```sql
ORDER BY maximum_horse_power DESC
LIMIT 2
```
Uma vez que executamos os comandos finais, tomamos conhecimento dos aliases que mencionamos na instrução SELECT. Como resultado, podemos utilizar o alias maximum_horse_power em vez do nome da função, embora ainda possamos usar este último. É melhor evitar ordenar uma grande quantidade de dados de saída, pois isso pode consumir uma quantidade significativa de tempo.

## Conclusão

O plano de execução que você visualizou para sua consulta SQL no PostgreSQL detalha como o mecanismo de banco de dados planeja buscar e processar os dados necessários para produzir o resultado desejado. Vamos analisar cada etapa e entender a ordem em que ocorrem, explicando o que cada uma representa:

1. **Seq Scan on cars as cars**
   - **Descrição**: Uma varredura sequencial (Seq Scan) é realizada na tabela `cars`. 
   - **Filtros aplicados**: A consulta verifica cada linha para ver se o ano (`year`) é maior que 2015 e se o país (`country`) é 'Germany'. 
   - **Resultado**: As linhas que não atendem a esses critérios são descartadas, indicado por "Rows Removed by Filter: 3".

2. **Hash**
   - **Descrição**: Esta etapa prepara uma estrutura de dados de hash para a tabela `cars` com base nos resultados da varredura que passaram pelos filtros.
   - **Detalhes**: A hash é construída para otimizar a junção subsequente, usando colunas que serão ligadas com a outra tabela (`engines`).

3. **Seq Scan on engines as engines**
   - **Descrição**: Assim como foi feito com `cars`, uma varredura sequencial é realizada na tabela `engines`.
   - **Resultado**: Todas as 7 linhas da tabela `engines` são lidas.

4. **Hash Inner Join**
   - **Descrição**: Um Hash Join (junção por hash) é realizado entre as tabelas `cars` e `engines`.
   - **Condição de junção**: A junção é feita onde o nome do motor (`engine_name` de `cars` e `name` de `engines`) são iguais.
   - **Resultado**: O resultado são 4 linhas onde a condição de junção é verdadeira.

5. **Sort (rows=4 loops=1)**
   - **Descrição**: As linhas resultantes do Join são ordenadas. O atributo exato da ordenação não está especificado aqui, mas é provável que seja preparação para a agregação.

6. **Aggregate**
   - **Descrição**: Uma função de agregação é aplicada.
   - **Filtro**: O filtro aplicado na agregação é que a potência máxima do motor (`max(engines.horse_power)`) deve ser maior que 200.
   - **Resultado**: Após aplicar o filtro, 3 linhas permanecem.

7. **Sort**
   - **Descrição**: As linhas são novamente ordenadas, desta vez provavelmente pelo valor de potência máxima do motor em ordem descendente.

8. **Limit**
   - **Descrição**: Apenas as duas primeiras linhas do resultado ordenado são retidas, conforme especificado pela cláusula `LIMIT 2` na consulta.

A ordem das operações mostra claramente como o PostgreSQL lida com a consulta, otimizando o processo ao usar técnicas como varreduras sequenciais, hash para junção e filtragem rigorosa antes de aplicar funções de agregação e ordenação, culminando na aplicação de um limite para o resultado final. Esta abordagem ajuda a minimizar o volume de dados manipulados nas etapas finais do processamento da consulta.

## Tudo foi uma mentira

```sql
SELECT
  cars.manufacturer,
  cars.model,
  cars.engine_name,
  engines.horse_power
FROM cars
JOIN engines ON cars.engine_name = engines.name
LIMIT 2;
```

Otimização do Join: O uso do Nested Loop Inner Join sugere que o otimizador percebeu que é mais eficiente processar o join linha a linha devido ao pequeno tamanho do resultado esperado da tabela engines.

Aplicação precoce do Limit: O fato de apenas 2 linhas serem processadas na varredura da tabela engines e resultarem em 2 linhas após o join indica que o LIMIT pode estar influenciando a execução da consulta mais cedo do que o plano sugere visualmente. Isto é, o PostgreSQL está provavelmente limitando o número de linhas processadas em cada etapa para cumprir eficientemente o LIMIT.

Eficiência do Plano: Este plano mostra um uso eficiente de recursos, processando o mínimo de dados necessário para alcançar o resultado desejado, que é fundamental em grandes bases de dados ou em sistemas com recursos limitados.
Portanto, mesmo que o LIMIT apareça ao final no plano visual, sua influência é evidente em todas as etapas anteriores, demonstrando a capacidade do otimizador de consulta do PostgreSQL de integrar profundamente considerações de limitação no plano de execução global.