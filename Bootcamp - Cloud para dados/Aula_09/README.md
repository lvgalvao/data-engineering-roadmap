### Aula 09: AWS Lambda e Eventos na AWS

**Objetivo**: Nesta aula, exploraremos o AWS Lambda e seu papel dentro de arquiteturas serverless na AWS. Vamos entender as diferenças entre o AWS Lambda e o EC2, discutir suas vantagens e desafios, e aprender como eventos podem ser aproveitados para criar sistemas escaláveis e eficientes.

### 3. **Arquitetura Serverless com AWS Lambda**

Este diagrama mostra uma arquitetura típica serverless, onde múltiplos serviços da AWS interagem com o Lambda para automatizar processos.

```mermaid
graph TB
    S3[S3] --> |Upload de Arquivo| Lambda1[AWS Lambda]
    APIGateway[API Gateway] --> |Requisição HTTP| Lambda2[AWS Lambda]
    DynamoDB[DynamoDB Streams] --> |Alteração na Tabela| Lambda3[AWS Lambda]
    CloudWatch[CloudWatch Events] --> |Alerta| Lambda4[AWS Lambda]
    SQS[SQS] --> |Mensagem na Fila| Lambda5[AWS Lambda]

    Lambda1 --> Process1[Processa Arquivo]
    Lambda2 --> Process2[API Backend]
    Lambda3 --> Process3[Sincroniza Dados]
    Lambda4 --> Process4[Automatiza Resposta]
    Lambda5 --> Process5[Processa Mensagem]
```

### **1. Introdução ao AWS Lambda**

AWS Lambda é um serviço de computação serverless que executa código sem que você precise gerenciar servidores. Ele é ideal para processos pontuais que respondem automaticamente a eventos, como uploads no S3, alterações em bancos de dados, e requisições HTTP através do API Gateway. Embora o termo "serverless" sugira a ausência de servidores, na prática, isso significa que o código é executado em servidores gerenciados pela AWS, não por você.

### **2. Diferença entre AWS Lambda e EC2**

#### **2.1. AWS EC2 (Elastic Compute Cloud)**
- **Definição**: Serviço de computação que permite criar e gerenciar instâncias de servidores virtuais na nuvem, oferecendo controle total sobre o ambiente.
- **Vantagens**:
  - **Controle Completo**: Customização do ambiente de software e hardware.
  - **Ambientes Persistentes**: Ideal para aplicações que exigem disponibilidade contínua.
  - **Escalabilidade Flexível**: Permite ajustes manuais ou automáticos de recursos.
- **Desafios**:
  - **Gerenciamento**: Requer manutenção contínua e configuração detalhada.
  - **Custo**: Pagamento contínuo pelo tempo de execução, independente do uso.
  - **Complexidade de Configuração**: Requer atenção aos detalhes de rede, segurança e capacidade.

#### **2.2. AWS Lambda**
- **Definição**: Serviço que executa código em resposta a eventos sem necessidade de gerenciar servidores, cobrando apenas pelo tempo de execução.
- **Vantagens**:
  - **Serverless**: Reduz a complexidade operacional.
  - **Escalabilidade Automática**: Ajusta automaticamente com base na carga de eventos.
  - **Custo-Eficiência**: Ideal para cargas intermitentes com pagamento por uso.
- **Desafios**:
  - **Limitações de Execução**: Tempo máximo de 15 minutos, com restrições de memória e armazenamento.
  - **Cold Starts**: Pequenos atrasos iniciais quando funções são ativadas após inatividade.
  - **Configuração de Permissões**: Requer configurações cuidadosas para garantir segurança.

### **3. Principais Casos de Uso do AWS Lambda**
- **Processamento de Arquivos**: Automatiza tarefas como redimensionamento de imagens e análise de dados em S3.
- **ETL em Tempo Real**: Transformação de dados em tempo real a partir de streams de dados.
- **APIs Serverless**: Gerenciamento de APIs com API Gateway e Lambda.
- **Eventos de IoT**: Resposta a dados de dispositivos IoT.
- **Automação de Infraestrutura**: Tarefas automatizadas como limpeza de recursos e monitoramento.

### **4. Eventos na AWS e Integração com Lambda**
Lambda pode ser acionado por diversos eventos na AWS, permitindo respostas dinâmicas a mudanças nos serviços.
- **Eventos S3**: Código executado ao upload de arquivos.
- **Eventos DynamoDB Streams**: Funções disparadas por alterações em tabelas.
- **Eventos API Gateway**: Requisições HTTP acionam funções Lambda.
- **Eventos CloudWatch**: Ações baseadas em alertas e agendamentos.
- **Eventos SQS**: Mensagens processadas de filas SQS.

### **5. Configurando uma Função AWS Lambda**
1. **Criar Função no Console AWS Lambda**: Selecione “Author from scratch” e configure nome, runtime e permissões.
2. **Escrever Código**: Escreva o código da função no editor integrado, definindo a lógica do lambda handler.
3. **Adicionar Trigger**: Configure o evento que irá acionar a função, como upload no S3 ou requisição HTTP.
4. **Testar Função**: Utilize o console para testes com eventos simulados e ajuste o código conforme necessário.

### **6. Comparação de Cenários de Uso: AWS Lambda vs. EC2**

| **Critério**           | **AWS EC2**                                  | **AWS Lambda**                              |
|------------------------|----------------------------------------------|---------------------------------------------|
| **Controle**           | Total sobre ambiente e recursos             | Limitado ao código da função                |
| **Persistência**       | Executa continuamente                       | Executa sob demanda, de forma intermitente  |
| **Escalabilidade**     | Manual ou automática                         | Automática com base em eventos              |
| **Gerenciamento**      | Requer configuração e manutenção            | Automação pela AWS                          |
| **Custo**              | Contínuo enquanto ativo                     | Paga apenas pelo uso                        |
| **Tempo de Resposta**  | Latência menor em execução contínua         | Cold starts podem aumentar a latência       |

### **7. Desafios ao Usar AWS Lambda e EC2**
- **AWS Lambda**: 
  - Limitações de tempo e recursos, cold starts e desafios de debug.
- **AWS EC2**: 
  - Requer gerenciamento contínuo, configuração de escalabilidade e custos constantes.

### **8. Motivação para Escolher AWS Lambda**
- **Economia**: Pagamento por uso sem custos fixos.
- **Escalabilidade**: Ajustes automáticos com base na demanda.
- **Foco no Código**: Sem preocupações com infraestrutura.

### **Conclusão**
AWS Lambda oferece uma abordagem serverless que simplifica a execução de código na nuvem, focando em escalabilidade e economia de custos. Comparado ao EC2, o Lambda reduz a complexidade de gerenciamento, mas exige um entendimento claro de suas limitações. A escolha entre Lambda e EC2 deve considerar o caso de uso específico, pesando controle, custos e necessidades operacionais.

Vou criar alguns diagramas usando Mermaid para ilustrar os conceitos apresentados na aula sobre AWS Lambda e EC2. Esses diagramas ajudarão a visualizar como o AWS Lambda funciona, suas integrações com eventos e uma comparação com o EC2.

### **Exemplo: Teste Meu Primeiro Lambda**

Este exemplo de função Lambda vai simplesmente retornar uma mensagem de teste quando invocada. Isso ajudará você a entender o básico de como criar, configurar e testar uma função Lambda.

#### **Passo a Passo para Criar a Função Lambda**

1. **Acesse o Console do AWS Lambda:**
   - Vá para o [AWS Management Console](https://aws.amazon.com/console/) e selecione **Lambda** no menu de serviços.

2. **Criar a Função Lambda:**
   - Clique em **Create Function**.
   - Escolha **Author from scratch**.
   - Configure os seguintes detalhes:
     - **Function name**: `TesteMeuPrimeiroLambda`.
     - **Runtime**: Selecione `Python 3.9` ou outra versão que você prefira.
     - **Permissions**: Selecione **Create a new role with basic Lambda permissions** para permitir que a função grave logs no CloudWatch.

3. **Adicionar o Código da Função:**

   Após criar a função, adicione o seguinte código no editor do console do Lambda:

   ```python
   def lambda_handler(event, context):
       # Função básica que retorna uma mensagem de teste
       return {
           'statusCode': 200,
           'body': 'Olá! Este é o meu primeiro teste com AWS Lambda.'
       }
   ```

4. **Testar a Função Lambda:**

   - Clique em **Deploy** para salvar o código.
   - Clique em **Test** para criar um evento de teste:
     - Dê um nome ao evento de teste, como `EventoTeste`.
     - Use o payload padrão ou um JSON simples, como:
       ```json
       {
         "mensagem": "Teste de invocação"
       }
       ```
   - Clique em **Test** novamente para executar a função.

   Você verá o resultado da execução na parte inferior da página, mostrando algo semelhante a:

   ```json
   {
     "statusCode": 200,
     "body": "Olá! Este é o meu primeiro teste com AWS Lambda."
   }
   ```

### **Explicação do Código**

- **`lambda_handler(event, context)`**: É a função principal que o AWS Lambda executa. Ela recebe dois parâmetros:
  - **`event`**: Contém os dados que você envia quando aciona a função, como um JSON com informações específicas.
  - **`context`**: Inclui informações de contexto sobre a execução da função, como o tempo de execução restante.

- **Retorno da Função**:
  - **`statusCode`**: Código HTTP 200 indicando sucesso.
  - **`body`**: Uma mensagem de resposta simples que é retornada para quem acionou a função.

### **Vantagens deste Exemplo Simples:**

- **Sem Dependências Externas**: Nenhuma instalação de bibliotecas é necessária, o que simplifica o deploy.
- **Facilidade de Configuração**: Com apenas alguns cliques e um pequeno trecho de código, você pode experimentar o AWS Lambda.
- **Ideal para Primeiros Testes**: Um bom ponto de partida para entender o funcionamento básico do AWS Lambda e como ele responde a eventos.

Este exemplo proporciona uma introdução ao uso do AWS Lambda de forma simples, sem complicações adicionais, sendo ideal para iniciantes que desejam entender como começar com funções serverless na AWS.

Vamos ajustar o exemplo para que a função Lambda receba uma mensagem através de um API Gateway, salve essa mensagem em um arquivo JSON e armazene o arquivo em um bucket S3. Esse exemplo será mais prático e útil para demonstrar o fluxo completo de integração entre o Lambda, o API Gateway e o Amazon S3.