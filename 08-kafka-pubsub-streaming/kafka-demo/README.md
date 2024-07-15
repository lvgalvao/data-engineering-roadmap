# Workshop de Kafka - Exercício de Configuração e Produção de Mensagens

## Pré-requisitos

1. **Confluent Cloud Cluster:** Certifique-se de ter configurado o Confluent Cloud Cluster e o CLI conforme os exercícios anteriores.
2. **Kafka CLI:** Tenha o Kafka CLI instalado e configurado para se conectar ao seu cluster Confluent Cloud.

## Passos para o Exercício

### 1. Criar uma Conta no Confluent Cloud
- Vá para a [URL do Confluent Cloud](https://confluent.cloud).
- Insira seu nome, email e senha.
- Clique no botão "Start Free" e espere receber um email de confirmação.
- Confirme seu email para prosseguir com a criação do cluster.

### 2. Configurar o Cluster
- Após confirmar o email, siga as instruções para configurar seu cluster.
- Escolha entre um cluster básico, padrão ou dedicado. Para este exercício, escolha o **cluster básico**.

### 3. Aplicar Código Promocional
- Navegue até "Settings" > "Billing and Payment".
- Insira o código promocional `kafka101` para obter $101 adicionais de uso gratuito.

### 4. Criar um Tópico

#### Criar um Tópico Usando a Interface Web
- Na página inicial do Confluent Cloud, selecione a guia "Topics".
- Clique em "Create Topic" e nomeie o tópico como `tecnologias`.
- Mantenha o número padrão de partições (6) e crie o tópico.

#### Criar um Tópico Usando o CLI
- No terminal, após configurar o CLI conforme os passos seguintes, crie um tópico:

    ```bash
    confluent kafka topic create tecnologias --partitions 6
    ```

### 5. Produzir Mensagens Usando a Interface Web
- Navegue até a guia "Messages" para visualizar a produção e o consumo de mensagens em tempo real.
- Clique em "Produce a new message to this topic".
- Insira `1` como chave e `Python` como valor, e clique em "Produce".

### 6. Configurar a Interface de Linha de Comando (CLI)
- Na página do Confluent Cloud, vá até "CLI and Tools" para baixar e configurar as ferramentas de linha de comando.
- No terminal, faça login no Confluent Cloud:

    ```bash
    confluent login --save
    ```

- Use o mesmo email e senha que você usou para criar sua conta.

### 7. Selecionar Ambiente e Cluster
- Liste os ambientes disponíveis:

    ```bash
    confluent environment list
    ```

- Use o ID do ambiente padrão:

    ```bash
    confluent environment use <environment_id>
    ```

- Liste os clusters Kafka disponíveis:

    ```bash
    confluent kafka cluster list
    ```

- Use o ID do cluster:

    ```bash
    confluent kafka cluster use <cluster_id>
    ```

### 8. Criar e Configurar Chave da API
- Crie uma chave da API:

    ```bash
    confluent api-key create --resource <cluster_id>
    ```

- Salve a chave da API e o segredo fornecidos.
- Use a chave da API:

    ```bash
    confluent api-key use <api_key> --resource <cluster_id>
    ```

### 9. Produzir Mensagens Usando o CLI
- Liste os tópicos disponíveis:

    ```bash
    confluent kafka topic list
    ```

- Para produzir mensagens para o tópico `tecnologias`, abra um terminal CLI e execute:

    ```bash
    confluent kafka topic produce tecnologias
    ```

- No prompt, insira uma mensagem de cada vez e pressione Enter:

    ```plaintext
    1:Python
    2:SQL
    3:Kafka
    4:Spark
    5:Airflow
    6:Kubernetes
    7:Terraform
    8:Docker
    ```

### 10. Consumir Mensagens Usando o CLI
- Abra outro terminal CLI para consumir as mensagens desde o início do tópico:

    ```bash
    confluent kafka topic consume tecnologias --from-beginning
    ```

### 11. Verificar Mensagens no Console Web
- Volte para a interface web do Confluent Cloud e verifique as mensagens produzidas.
- Para ver mensagens na interface web, defina o deslocamento (offset) para zero e verifique cada partição.

### Conclusão

Se você seguiu todos os passos, realizou várias atividades importantes:
- Criou uma conta no Confluent Cloud e configurou seu primeiro cluster Kafka.
- Criou um tópico e produziu mensagens usando a interface web.
- Instalou o CLI, criou uma chave da API e produziu/consumiu mensagens usando o CLI.

### Gráfico Mermaid

```mermaid
graph TD;
    A[Criar Conta no Confluent Cloud] --> B[Configurar Cluster]
    B --> C[Aplicar Código Promocional]
    C --> D[Criar Tópico]
    D --> E[Produzir Mensagens (Web)]
    E --> F[Configurar CLI]
    F --> G[Selecionar Ambiente e Cluster]
    G --> H[Criar e Configurar Chave da API]
    H --> I[Produzir Mensagens (CLI)]
    I --> J[Consumir Mensagens (CLI)]
    J --> K[Verificar Mensagens (Web)]
```

### Referências
- [Confluent Cloud Documentation](https://docs.confluent.io/cloud/current/get-started/index.html)
- [Kafka Documentation](https://kafka.apache.org/documentation/)

---

Espero que este README e o gráfico ajudem no entendimento e execução do exercício sobre configuração e produção de mensagens no Kafka. Se precisar de mais detalhes ou ajuda, estou à disposição!