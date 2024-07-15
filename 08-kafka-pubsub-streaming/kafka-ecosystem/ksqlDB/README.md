Claro! Vou explicar cada comando e passo detalhadamente para que você entenda o objetivo de cada um deles.

# Hands On: ksqlDB

Neste exercício, você aprenderá como manipular seus dados usando o ksqlDB. Até agora, estivemos produzindo dados e lendo dados de um tópico do Apache Kafka sem quaisquer etapas intermediárias. Com a transformação e agregação de dados, podemos fazer muito mais!

No último exercício, criamos um Conector Datagen Source para produzir um fluxo de dados de pedidos para um tópico Kafka, serializando-o em Avro usando o Confluent Schema Registry. Este exercício depende dos dados que nosso conector está produzindo, então, se você não completou o exercício anterior, encorajamos você a fazê-lo antes de prosseguir.

Antes de começarmos, certifique-se de que seu Conector Datagen Source ainda está ativo e em execução.

## Passo a Passo

### 1. Criar Cluster ksqlDB
Na página inicial do cluster no Confluent Cloud Console, selecione ksqlDB no menu à esquerda. 
- **Objetivo**: Iniciar o ksqlDB, que é a plataforma de streaming SQL para Apache Kafka, permitindo consultas e transformações em tempo real dos dados no Kafka.

### 2. Configurar Acesso
Escolha "Global access" na página de controle de acesso e continue para dar um nome ao cluster ksqlDB e depois inicie o cluster.
- **Objetivo**: Configurar o acesso ao cluster ksqlDB para garantir que todos os serviços e aplicações tenham acesso ao ksqlDB.

### 3. Registrar Tópico
Após a provisão do cluster ksqlDB, você será levado ao editor ksqlDB. Adicione o tópico `orders` do exercício anterior à aplicação ksqlDB. Registre-o como um stream executando:
```sql
CREATE STREAM orders_stream WITH (
  KAFKA_TOPIC='orders', 
  VALUE_FORMAT='AVRO',
  PARTITIONS=6,
  TIMESTAMP='ordertime');
```
- **Objetivo**: Criar um stream no ksqlDB a partir do tópico `orders` para que possamos realizar consultas SQL sobre os dados em tempo real.

### 4. Visualizar Stream
Navegue até a aba Streams e selecione `orders_stream` para visualizar mais detalhes sobre o stream.
- **Objetivo**: Inspecionar os detalhes do stream, incluindo os campos e o formato dos dados, para entender melhor a estrutura do fluxo de dados.

### 5. Transformar Dados
Execute a seguinte consulta para transformar o campo `ordertime` em um formato mais legível e extrair os dados aninhados do struct `address`:
```sql
SELECT 
    TIMESTAMPTOSTRING(ORDERTIME, 'yyyy-MM-dd HH:mm:ss.SSS') AS ORDERTIME_FORMATTED,
    orderid,
    itemid,
    orderunits,
    address->city, 
    address->state,
    address->zipcode
FROM ORDERS_STREAM;
```
- **Objetivo**: Transformar os dados no stream `orders_stream` para melhorar a legibilidade do campo `ordertime` e extrair campos aninhados do endereço.

### 6. Persistir Resultados
Para persistir os resultados em um novo stream, adicione uma linha `CREATE STREAM` no início da consulta:
```sql
CREATE STREAM ORDERS_STREAM_TS AS
SELECT 
    TIMESTAMPTOSTRING(ORDERTIME, 'yyyy-MM-dd HH:mm:ss.SSS') AS ORDERTIME_FORMATTED,
    orderid,
    itemid,
    orderunits,
    address->city, 
    address->state,
    address->zipcode 
FROM ORDERS_STREAM;
```
- **Objetivo**: Criar um novo stream `ORDERS_STREAM_TS` que contém os dados transformados do stream original `orders_stream`.

### 7. Agregação de Dados
Crie uma tabela para contar quantos pedidos são feitos por estado. O ksqlDB facilita a segmentação dos dados em janelas de tempo:
```sql
CREATE TABLE STATE_COUNTS AS 
SELECT 
  address->state,
  COUNT_DISTINCT(ORDERID) AS DISTINCT_ORDERS
FROM ORDERS_STREAM
WINDOW TUMBLING (SIZE 7 DAYS) 
GROUP BY address->state;
```
- **Objetivo**: Agregar os dados no stream `ORDERS_STREAM` para contar o número distinto de pedidos por estado em uma janela de 7 dias, criando uma tabela `STATE_COUNTS`.

### 8. Consultar Tabela
Navegue até a aba Tables para ver os dados relacionados à tabela.
- **Objetivo**: Visualizar e consultar os dados agregados na tabela `STATE_COUNTS`.

### 9. Consulta de Pull
Para ver apenas os valores mais recentes de uma tabela, execute uma consulta de pull. Veja um instantâneo atual contendo os estados que tiveram mais de dois pedidos por período de uma semana:
```sql
SELECT
    *
FROM STATE_COUNTS
WHERE DISTINCT_ORDERS > 2;
```
- **Objetivo**: Executar uma consulta de pull para obter um snapshot dos dados na tabela `STATE_COUNTS`, filtrando os estados que tiveram mais de dois pedidos na última semana.

Esses passos fornecem uma visão detalhada de como configurar, transformar e consultar dados em tempo real usando o ksqlDB com Apache Kafka.