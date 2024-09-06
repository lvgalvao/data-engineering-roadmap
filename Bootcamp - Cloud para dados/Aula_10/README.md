Aqui está a versão atualizada da aula com gráficos Mermaid para cada projeto e ajustes conforme solicitado:

### Aula 10: Projetos Práticos com AWS Lambda

**Objetivo**: Nesta aula, realizaremos uma série de projetos práticos utilizando AWS Lambda. Vamos explorar como configurar funções Lambda para serem acionadas por eventos temporais e específicos, realizar requests HTTP e integrar com o Amazon RDS para criar soluções serverless eficientes.

### **Projetos da Aula 10**

1. **Configuração de Timer de 10 em 10 Minutos com AWS Lambda**

   **Objetivo**: Demonstrar como agendar uma função Lambda para ser executada a cada 10 minutos usando o Amazon CloudWatch Events (ou EventBridge).

   **Passo a Passo**:
   1. Acesse o AWS Management Console e selecione **Lambda**.
   2. Crie uma nova função Lambda com o nome `TimerFunction`.
   3. Vá para **CloudWatch Events** e crie uma nova regra com uma expressão cron `cron(0/10 * * * ? *)` para disparar a cada 10 minutos.
   4. Vincule essa regra à função `TimerFunction`.
   5. Teste para confirmar que a função está sendo acionada conforme esperado.

   ```mermaid
   graph TD
       CW[CloudWatch Events] -->|Trigger a cada 10 minutos| Lambda1[AWS Lambda TimerFunction]
       Lambda1 --> Process1[Executa a Função]
   ```

2. **Configuração de Funções Lambda para Horários Específicos**

   **Objetivo**: Ensinar como configurar a execução de uma função Lambda em horários específicos, como às 9h, 12h, e 18h diariamente.

   **Passo a Passo**:
   1. No AWS Management Console, crie uma função Lambda chamada `SpecificTimeFunction`.
   2. Acesse **CloudWatch Events** e crie uma regra com uma expressão cron, por exemplo, `cron(0 9,12,18 * * ? *)`.
   3. Vincule essa regra à função Lambda `SpecificTimeFunction`.
   4. Teste a configuração simulando o disparo da função nos horários especificados.

   ```mermaid
   graph TD
       CW[CloudWatch Events] -->|Trigger às 9h, 12h, 18h| Lambda2[AWS Lambda SpecificTimeFunction]
       Lambda2 --> Process2[Executa a Função]
   ```

3. **Criação de Funções Lambda para Realizar Requests HTTP**

   **Objetivo**: Demonstrar como usar AWS Lambda para fazer requests HTTP utilizando o módulo `urllib3`, nativo do Python.

   **Passo a Passo**:
   1. Crie uma nova função Lambda chamada `HTTPRequestFunction`.
   2. Utilize o módulo `urllib3` para realizar um GET request para uma API pública e processar a resposta.
   3. Teste a função e visualize os logs para garantir que o request foi realizado corretamente.

   ```python
   import urllib3

   def lambda_handler(event, context):
       http = urllib3.PoolManager()
       response = http.request('GET', 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY')
       data = response.data.decode('utf-8')
       return {
           'statusCode': 200,
           'body': data
       }
   ```

   ```mermaid
   graph TD
       Lambda3[AWS Lambda HTTPRequestFunction] -->|Faz Request HTTP| API[API Externa]
       API --> Process3[Processa Resposta]
   ```

4. **Criação de Funções Lambda para Enviar Requests HTTP**

   **Objetivo**: Mostrar como enviar dados para um endpoint via POST request utilizando o módulo `requests`.

   **Passo a Passo**:
   1. No AWS Lambda, crie uma função chamada `PostRequestFunction`.
   2. Utilize a biblioteca `requests` para enviar um POST request para um endpoint específico.
   3. Configure a função para receber dados do evento e incluí-los no corpo do request.

   ```python
   import requests

   def lambda_handler(event, context):
       url = "https://yourapiendpoint.com/data"
       payload = {'key1': 'value1', 'key2': 'value2'}
       headers = {'Content-Type': 'application/json'}
       response = requests.post(url, json=payload, headers=headers)
       return {
           'statusCode': response.status_code,
           'body': response.json()
       }
   ```

   ```mermaid
   graph TD
       Lambda4[AWS Lambda PostRequestFunction] -->|Envia Request POST| Endpoint[API Endpoint]
       Endpoint --> Process4[Recebe e Processa Dados]
   ```

5. **Integração do AWS Lambda com Amazon RDS**

   **Objetivo**: Demonstrar como conectar uma função Lambda a um banco de dados RDS para fazer um GET request em uma API e inserir os dados no banco de dados.

   **Passo a Passo**:
   1. Crie um banco de dados RDS (PostgreSQL, MySQL, etc.) e configure as permissões de segurança para permitir acesso a partir da função Lambda.
   2. Crie uma função Lambda chamada `RDSIntegrationFunction` e configure-a para acessar o RDS.
   3. Utilize `urllib3` para fazer o GET request e `psycopg2` para inserir os dados no banco RDS.

   ```python
   import urllib3
   import psycopg2

   def lambda_handler(event, context):
       # Fazendo o request HTTP
       http = urllib3.PoolManager()
       response = http.request('GET', 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=YOUR_API_KEY')
       data = response.data.decode('utf-8')
       
       # Configurações de conexão com o RDS
       conn = psycopg2.connect(
           host="rds-endpoint.amazonaws.com",
           database="mydb",
           user="username",
           password="password"
       )
       cursor = conn.cursor()

       # Inserindo dados no RDS
       cursor.execute("INSERT INTO weather_data (response) VALUES (%s)", (data,))
       conn.commit()

       cursor.close()
       conn.close()

       return {
           'statusCode': 200,
           'body': 'Dados inseridos com sucesso no RDS!'
       }
   ```

   ```mermaid
   graph TD
       Lambda5[AWS Lambda RDSIntegrationFunction] -->|Faz Request GET| API[API Externa]
       API --> Process5[Processa Resposta]
       Process5 -->|Insere Dados| RDS[RDS Database]
   ```

### **Conclusão da Aula 10**

Nesta aula prática, exploramos cinco cenários diferentes de uso do AWS Lambda, destacando sua flexibilidade e integração com outros serviços da AWS. As demonstrações forneceram uma base sólida sobre como configurar funções Lambda para operar com eventos temporais, realizar requisições HTTP e conectar-se a bancos de dados RDS, reforçando o papel do Lambda como uma ferramenta essencial para arquiteturas modernas e escaláveis.
