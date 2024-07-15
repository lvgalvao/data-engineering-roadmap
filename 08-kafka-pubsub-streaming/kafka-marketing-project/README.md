## Escopo do Projeto: Simulação de 50 Refrigeradores Espalhados pelo Brasil

Claro! Aqui está o README atualizado com o comando para criar o tópico `marketing-project`.

## Projeto: Monitoramento de Refrigeração no Brasil

### Objetivo

Este projeto tem como objetivo simular 50 refrigeradores espalhados pelo Brasil. Cada refrigerador irá reportar a temperatura a cada segundo. Queremos entender como os refrigeradores estão operando em diferentes regiões e monitorar temperaturas anômalas que podem indicar falhas ou problemas.

### Componentes do Projeto

1. **Producers**:
    - 50 produtores simulando refrigeradores.
    - Cada produtor envia dados de temperatura a cada segundo.
    - As temperaturas são geradas com base em dois intervalos: 
        - 45 refrigeradores com temperaturas entre 0°C e 5°C.
        - 5 refrigeradores com temperaturas entre 20°C e 40°C.
    - Cada produtor tem um ID único gerado com UUID.

2. **Consumer**:
    - Um consumidor que lê os dados em tempo real e exibe as temperaturas usando Streamlit.

3. **Kafka Topic**:
    - Tópico chamado `marketing-project`.

### Passos para Configuração

#### 1. Configurar o Confluent CLI

Certifique-se de que você tenha configurado o Confluent CLI e esteja autenticado:

```bash
confluent login
```

#### 2. Selecionar o Ambiente e o Cluster

```bash
confluent environment use <environment_id>
confluent kafka cluster use <cluster_id>
```

#### 3. Criar o Tópico `marketing-project`

```bash
confluent kafka topic create marketing-project --partitions 6
```

### Objetivo

O objetivo deste projeto é simular 50 refrigeradores espalhados pelo Brasil, gerando dados de temperatura em tempo real. Essa simulação visa monitorar e analisar as variações de temperatura, permitindo uma melhor compreensão do comportamento térmico dos refrigeradores em diferentes regiões e condições climáticas. Com este projeto, pretendemos:

1. **Monitorar Temperaturas em Tempo Real**: Capturar e exibir dados de temperatura de 50 refrigeradores espalhados pelo Brasil, atualizados a cada segundo.
2. **Analisar Distribuição de Temperaturas**: Identificar padrões de temperatura e comportamentos anômalos entre os refrigeradores.
3. **Avaliar Eficiência Térmica**: Verificar a eficiência térmica dos refrigeradores em manter a temperatura dentro de uma faixa desejada.
4. **Identificar Problemas Potenciais**: Detectar refrigeradores que possam estar operando fora da faixa de temperatura esperada, sinalizando possíveis falhas ou necessidade de manutenção.

### Descrição do Projeto

1. **Simulação dos Refrigeradores**:
    - **Quantidade**: 50 refrigeradores.
    - **Localização**: Cada refrigerador terá uma latitude e longitude fixas, representando diferentes regiões do Brasil.
    - **Distribuição de Temperatura**:
        - 45 refrigeradores manterão temperaturas entre 0 e 5 graus Celsius (95%).
        - 5 refrigeradores terão temperaturas entre 20 e 40 graus Celsius (5%), representando possíveis falhas ou condições extremas.

2. **Produção de Dados**:
    - **Intervalo de Produção**: Cada refrigerador gerará uma leitura de temperatura a cada segundo.
    - **Formato dos Dados**: Os dados serão enviados em formato JSON, contendo a latitude, longitude, temperatura e identificador do refrigerador.

3. **Tópico Kafka**:
    - **Nome do Tópico**: `marketing-project`.
    - **Produção e Consumo**: Os dados gerados pelos 50 refrigeradores serão publicados neste tópico Kafka.

4. **Consumidor de Dados**:
    - **Visualização em Tempo Real**: Um consumidor será implementado usando Streamlit para exibir as últimas leituras de temperatura de cada refrigerador em tempo real.
    - **Monitoramento e Análise**: A aplicação Streamlit permitirá monitorar os dados e identificar rapidamente qualquer comportamento anômalo.

### Componentes do Projeto

1. **Producers**:
    - 50 instâncias de produtores, cada uma simulando um refrigerador.
    - Utilização da biblioteca `Faker` para gerar dados de localização e temperatura.
    - Publicação dos dados no tópico `marketing-project` no Kafka.

2. **Consumer**:
    - Uma aplicação Streamlit que consome os dados do tópico `marketing-project`.
    - Exibição dos dados em um dashboard, mostrando a última leitura de temperatura de cada refrigerador.

### Ferramentas e Tecnologias

1. **Apache Kafka**: Para transmissão e ingestão de dados em tempo real.
2. **Confluent Cloud**: Plataforma gerenciada de Kafka para simplificar a configuração e o gerenciamento do cluster.
3. **Faker**: Biblioteca para geração de dados fictícios.
4. **Docker**: Para containerização dos produtores e consumidor.
5. **Streamlit**: Para visualização dos dados em tempo real.

### Implementação

1. **Configuração do Tópico Kafka**:
    - Criar o tópico `marketing-project` no Confluent Cloud.

2. **Desenvolvimento dos Producers**:
    - Implementar o script de produção utilizando `Faker` para gerar os dados de temperatura e localização.
    - Containerizar os produtores usando Docker.

3. **Desenvolvimento do Consumer**:
    - Implementar a aplicação Streamlit para consumir e exibir os dados em tempo real.
    - Containerizar o consumidor usando Docker.

4. **Execução**:
    - Iniciar os 50 produtores e o consumidor utilizando `docker-compose`.

## Executar os Containers
Certifique-se de que o arquivo docker-compose.yml está configurado corretamente e execute os seguintes comandos no terminal para construir a imagem Docker e iniciar os containers:

```bash
docker-compose build
docker-compose up -d
```

### Resultado Esperado

Ao final do projeto, espera-se ter uma simulação funcional de 50 refrigeradores espalhados pelo Brasil, com dados de temperatura sendo gerados e exibidos em tempo real. A aplicação Streamlit fornecerá uma interface intuitiva para monitorar e analisar esses dados, possibilitando a identificação de padrões e anomalias de temperatura, além de fornecer insights sobre a eficiência térmica dos refrigeradores em diferentes condições climáticas.

### Bizu para apagar

confluent kafka topic update marketing-project --config retention.ms=1000

confluent kafka topic delete marketing-project


###

```bash
confluent kafka topic consume marketing-project --from-beginning
```

