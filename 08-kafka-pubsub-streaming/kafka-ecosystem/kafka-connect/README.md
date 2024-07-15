# Kafka Connect com Confluent Cloud: Geração e Consumo de Dados

## Visão Geral

Neste exercício, vamos criar um conector de origem para o Kafka Connect no Confluent Cloud, que produzirá dados para um tópico Kafka. Uma vez configurado o conector, consumiremos esses dados a partir da linha de comando.

## Passos

1. **Criar um Tópico**
2. **Configurar o DataGen Connector**
3. **Consumir os Dados**

## Pré-requisitos

- Uma conta no Confluent Cloud
- CLI do Confluent instalado e autenticado

## Passo 1: Criar um Tópico

Primeiro, precisamos fornecer um tópico para o conector DataGen produzir dados. Podemos criar esse tópico usando a interface do Confluent Cloud ou o Confluent CLI.

### Usando a Interface do Confluent Cloud

1. Acesse o painel do Confluent Cloud.
2. Navegue até a seção "Tópicos".
3. Clique em "Criar Tópico".
4. Nomeie o tópico como `inventory` e use as configurações padrão.
5. Clique em "Criar" para finalizar.

### Usando o Confluent CLI

```bash
confluent kafka topic create inventory --partitions 1 --cluster <cluster-id>
```

Substitua `<cluster-id>` pelo ID real do seu cluster Kafka.

## Passo 2: Configurar o DataGen Connector

Agora, precisamos configurar o conector DataGen para gerar dados de amostra de acordo com um esquema predefinido.

### Usando a Interface do Confluent Cloud

1. Navegue até a seção "Connect".
2. Clique em "Adicionar Conector".
3. Selecione "DataGen" da lista de conectores disponíveis.
4. Configure o conector:
    - **Nome do Conector**: DataGen-Inventory
    - **Tópico**: `inventory`
    - **Formato da Mensagem de Saída**: JSON
    - **API Key**: Crie ou selecione uma API Key e um segredo existentes.
    - **Modelo de Dados**: Selecione "Inventory" dos modelos disponíveis.
5. Clique em "Continuar" e revise a configuração.
6. Clique em "Lançar" para iniciar o conector.

### Exemplo de Configuração

```json
{
  "name": "DataGen-Inventory",
  "config": {
    "connector.class": "io.confluent.kafka.connect.datagen.DatagenConnector",
    "kafka.topic": "inventory",
    "quickstart": "Inventory",
    "key.converter": "org.apache.kafka.connect.storage.StringConverter",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "value.converter.schemas.enable": "false",
    "max.interval": 1000,
    "iterations": -1,
    "tasks.max": 1
  }
}
```

Você pode usar a interface do Confluent Cloud para inserir essa configuração.

## Passo 3: Consumir os Dados

Uma vez que o conector DataGen estiver em execução, podemos consumir os dados gerados usando o Confluent CLI.

### Usando o Confluent CLI

```bash
confluent kafka topic consume inventory --from-beginning --cluster <cluster-id>
```

Substitua `<cluster-id>` pelo ID real do seu cluster Kafka.

## Conclusão

Ao longo deste exercício, aprendemos como iniciar rapidamente com o Kafka Connect criando um conector de origem simples que gera dados. Isso é apenas o começo do que o Kafka Connect tem a oferecer. Incentivamos você a explorar mais recursos para entender todas as capacidades do Kafka Connect.

## Recursos Adicionais

- [Documentação do Confluent Kafka Connect](https://docs.confluent.io/platform/current/connect/index.html)
- [Guia de Início Rápido do Confluent Cloud](https://docs.confluent.io/cloud/current/get-started/index.html)
- [Deep Dive no Kafka Connect](https://docs.confluent.io/platform/current/connect/concepts.html)

Seguindo esses passos, você pode configurar facilmente um conector de origem do Kafka Connect, gerar dados de amostra e consumir esses dados usando o Confluent Cloud.