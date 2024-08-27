# **Bootcamp Cloud: Aula 04: IAM na AWS**

**Objetivo**: Nesta aula, vamos explorar o IAM (Identity and Access Management) da AWS. Vamos entender como proteger a conta AWS, o papel do usuário root, como criar e gerenciar usuários, grupos, políticas, e configurar o MFA.

### **1. Protegendo a Conta AWS**

- **Importância**: A conta AWS é o coração da sua infraestrutura na nuvem. Protegê-la é essencial para evitar acessos não autorizados e garantir a segurança dos seus recursos.

### **2. Usuário Root**

- **O que é o Usuário Root**: 
  - O usuário root é a conta inicial criada ao configurar a AWS. Ele tem acesso total a todos os recursos e configurações.
  - **Riscos**: O uso contínuo do usuário root é arriscado, pois ele tem permissões ilimitadas, o que pode levar a potenciais danos em caso de comprometimento.

- **Boas Práticas**:
  - Evitar o uso diário do usuário root.
  - Criar usuários IAM com permissões específicas para tarefas do dia a dia.
  - Habilitar o MFA (Multi-Factor Authentication) para a conta root.

### **3. IAM (Identity and Access Management)**

- **O que é IAM**:
  - IAM permite criar e gerenciar usuários, grupos, e permissões na AWS.
  - Facilita a implementação do princípio do menor privilégio, garantindo que cada usuário tenha apenas as permissões necessárias.

### **4. Configuração do MFA (Multi-Factor Authentication)**

- **O que é MFA**: 
  - MFA adiciona uma camada extra de segurança, exigindo que o usuário forneça uma segunda forma de autenticação além da senha, como um código gerado por um dispositivo móvel.

- **Passo a Passo para Configurar o MFA no Usuário Root**:
  
  1. **Acessar o Console de Gerenciamento da AWS**:
     - Faça login como o usuário root.
  
  2. **Navegar até a Página de Segurança da Conta**:
     - No canto superior direito, clique no nome da conta e selecione "Minha Conta".
     - Role para baixo até "Configurações de segurança" e clique em "Ativar MFA" na seção de autenticação multifator.

  3. **Escolher o Tipo de Dispositivo MFA**:
     - Selecione "Aplicativo autenticador" para usar um dispositivo móvel como segundo fator de autenticação.

  4. **Configurar o Aplicativo Autenticador**:
     - Abra o aplicativo autenticador no seu dispositivo móvel (ex: Google Authenticator).
     - Escaneie o código QR fornecido pela AWS ou insira a chave manualmente.
  
  5. **Verificar o Código MFA**:
     - Insira os códigos gerados pelo aplicativo para verificar a configuração.
  
  6. **Salvar a Configuração**:
     - Confirme e salve a configuração do MFA.

  7. **Testar a Configuração**:
     - Saia e faça login novamente para verificar se o MFA está funcionando corretamente.

---

### **5. Criando um Usuário Administrativo**

**Passo a Passo para Criar um Usuário Administrativo:**

1. **Acessar o Console IAM**:
   - **Faça login** no console da AWS com o usuário root.
   - Navegue até o serviço **IAM (Identity and Access Management)**.
   
2. **Adicionar Novo Usuário**:
   - Clique em **"Usuários"** e selecione **"Adicionar usuário"**.
   - Insira um nome para o novo usuário administrativo, como "admin-user".

3. **Selecionar o Tipo de Acesso**:
   - **Acesso programático**: Marque essa opção para gerar **chaves de acesso** (Access Key ID e Secret Access Key), necessárias para scripts ou automações que interagem com a AWS via API.
   - **Acesso à AWS Management Console**: Marque essa opção para permitir que o usuário faça login no console da AWS. Defina uma senha inicial (você pode permitir que o usuário a redefina no primeiro login ou definir uma senha permanente).

4. **Configurar Permissões**:
   - **Anexar Políticas Diretamente**: 
     - **AdministratorAccess**: Selecione esta política para conceder ao usuário todas as permissões administrativas, permitindo acesso completo a todos os recursos da AWS.
     - **PowerUserAccess** (Alternativa): Selecione esta política se desejar conceder permissões administrativas amplas, mas sem acesso ao gerenciamento de contas, como a criação de novos usuários IAM ou configuração de billing.

5. **Revisar e Criar o Usuário**:
   - Revise as configurações e clique em **"Criar usuário"**.
   - **Download do CSV**: Faça o download do arquivo CSV contendo as chaves de acesso e a senha do console para uso futuro. Estas informações são essenciais para acessar a AWS programaticamente e via console.

6. **Encerramento do Uso do Usuário Root**:
   - Após a criação do usuário administrativo, saia do console e faça login novamente utilizando as credenciais do novo usuário.
   - A partir deste ponto, o uso do usuário root deve ser restrito a tarefas críticas e configurações de segurança inicial.

---

### **6. Comparação: Root vs AdministratorAccess vs PowerUserAccess**

| **Característica**                  | **Usuário Root**                                      | **AdministratorAccess**                          | **PowerUserAccess**                            |
|-------------------------------------|------------------------------------------------------|-------------------------------------------------|------------------------------------------------|
| **Acesso Total**                    | Sim, acesso total e irrestrito a todos os recursos   | Sim, acesso completo a quase todos os recursos  | Não, acesso restrito a certos recursos        |
| **Gerenciamento de IAM**            | Sim                                                  | Sim                                              | Não, sem acesso ao IAM                        |
| **Configuração de Billing**         | Sim                                                  | Sim                                              | Não                                            |
| **Criação de Recursos**             | Sim                                                  | Sim                                              | Sim                                            |
| **Modificação de Políticas de Conta**| Sim                                                  | Sim                                              | Não                                            |
| **Gerenciamento de Faturamento e Conta** | Sim, incluindo alteração de informações de pagamento e fechamento da conta | Não                                              | Não                                            |
| **Cancelamento de Serviços e Fechamento da Conta** | Sim | Não | Não |
| **Alteração de Suporte AWS**        | Sim, pode alterar o plano de suporte (ex: suporte básico para empresarial) | Não | Não |
| **Exclusão de CloudFront Key Pairs**| Sim, pode criar, gerenciar ou excluir CloudFront key pairs | Não | Não |
| **Uso recomendado**                 | Configuração inicial e tarefas críticas de segurança | Uso diário para administração e operações gerais | Uso para administração sem acesso a IAM e Billing |

---

### **7. Questões Frequentes**

1. **O AdministratorAccess pode alterar o Usuário Root?**

   Não, um usuário com a política AdministratorAccess não pode alterar o usuário root. Somente o próprio usuário root pode alterar suas próprias configurações, como o nome de usuário, senha, chaves de acesso, ou desativar o MFA. Isso é uma medida de segurança importante para proteger a conta AWS, garantindo que apenas o usuário root tenha controle total sobre suas próprias credenciais e configurações.

2. **Eu contratei uma consultoria, qual acesso criar?**

   A escolha entre conceder `AdministratorAccess` ou `PowerUserAccess` à consultoria depende da natureza das tarefas que eles irão realizar e do nível de controle que você deseja manter sobre sua conta AWS.

   - **Quando conceder `AdministratorAccess`**:
     - **Cenário**: A consultoria precisa ter acesso completo para gerenciar todos os recursos da AWS, incluindo a criação e gerenciamento de usuários IAM, configuração de políticas, gerenciamento de billing, e outras tarefas administrativas completas.
     - **Risco**: Eles terão permissão para alterar quase todos os aspectos da sua conta, incluindo ações sensíveis que podem impactar a segurança ou o faturamento.

   - **Quando conceder `PowerUserAccess`**:
     - **Cenário**: A consultoria precisa realizar tarefas administrativas gerais, como criar e gerenciar recursos, mas você deseja limitar o acesso a configurações de conta e gerenciamento de usuários IAM.
     - **Risco**: Eles não poderão criar ou gerenciar usuários IAM, alterar configurações de faturamento, ou fazer mudanças no plano de suporte, o que oferece um nível adicional de segurança e controle sobre aspectos críticos da sua conta.

   - **Recomendação**:
     - **PowerUserAccess** pode ser mais apropriado se você quiser manter controle sobre as configurações mais sensíveis da sua conta, como gerenciamento de usuários IAM e informações de faturamento. 
     - **AdministratorAccess** deve ser concedido somente se a consultoria realmente precisar de controle total sobre todos os aspectos da sua infraestrutura AWS, e você confia plenamente que eles irão gerenciar esses recursos de forma segura e responsável. 

---

### **8. Criando um Grupo de "Engenheiro de Dados" no IAM**

**Passo a Passo para Criar um Grupo de "Engenheiro de Dados" no IAM**

1. **Acessar o Console IAM:**
   - Faça login no console da AWS com um usuário que tenha permissões suficientes para gerenciar o IAM.
   - Navegue até o serviço **IAM (Identity and Access Management)**.

2. **Criar um Novo Grupo:**
   - No painel do IAM, selecione **"Gr

upos"** no menu lateral.
   - Clique em **"Criar Novo Grupo"**.
   - Insira o nome do grupo como **"EngenheiroDeDados"**.

3. **Copiar Permissões de um Grupo Existente (Opcional):**
   - Se você já possui um grupo com permissões similares e deseja copiar suas permissões, selecione essa opção e escolha o grupo de referência.
   - Caso contrário, pule esta etapa e prossiga para anexar políticas diretamente.

4. **Anexar Políticas Diretamente:**
   - Na tela de anexar políticas, você verá uma lista de políticas gerenciadas pela AWS.
   - Para o grupo de "Engenheiro de Dados", selecione as seguintes políticas relevantes:

     - **AmazonS3FullAccess**: Dá ao grupo acesso completo ao Amazon S3, permitindo criar, ler, escrever e excluir buckets e objetos.
     - **AmazonEC2FullAccess**: Permite ao grupo gerenciar instâncias EC2, incluindo o provisionamento, configuração e encerramento de instâncias.
     - **AmazonVPCFullAccess**: Concede ao grupo a capacidade de gerenciar redes VPC, sub-redes, roteamento e segurança de redes.
     - **AmazonRDSFullAccess**: Concede permissão para gerenciar instâncias de bancos de dados no Amazon RDS.
     - **AmazonGlueConsoleFullAccess**: Permite ao grupo acessar e usar o serviço de ETL Amazon Glue para operações de dados.
     - **AmazonAthenaFullAccess**: Dá ao grupo a permissão para consultar dados armazenados no S3 usando o Amazon Athena.

   - Após selecionar as políticas desejadas, clique em **"Next Step"**.

5. **Revisar o Grupo:**
   - Revise as permissões que serão concedidas ao grupo.
   - Verifique se todas as políticas necessárias estão anexadas.

6. **Criar o Grupo:**
   - Clique em **"Create Group"** para finalizar a criação do grupo "EngenheiroDeDados".

7. **Adicionar Usuários ao Grupo:**
   - Após a criação do grupo, você pode adicionar usuários existentes ao grupo "EngenheiroDeDados" ou criar novos usuários e associá-los ao grupo.
   - Isso garantirá que todos os membros do grupo tenham as mesmas permissões para acessar e gerenciar os recursos associados ao projeto de dados.

---

### **9. Tags Sugeridas para o Grupo "Engenheiro de Dados"**

As tags ajudam a organizar e identificar recursos relacionados ao grupo, facilitando a gestão e a automação:

- **Project:** Nome do projeto específico (ex: "DataPipeline2024", "CustomerAnalytics").
- **Department:** Nome do departamento ou equipe (ex: "DataEngineering", "AnalyticsTeam").
- **Role:** Descrição da função (ex: "DataEngineer", "DataOps").
- **Environment:** Ambiente onde o grupo atuará (ex: "Production", "Staging", "Development").
- **Owner:** Nome do proprietário ou responsável pelo grupo (ex: "Luciano", "DataTeamLead").
- **CostCenter:** Código ou nome do centro de custos (ex: "CC1001", "MarketingData").
- **Compliance:** Requisitos de conformidade específicos (ex: "GDPR", "HIPAA").
- **BusinessUnit:** Unidade de negócio relevante (ex: "Sales", "ProductDevelopment").
- **Purpose:** Finalidade do grupo (ex: "DataProcessing", "ETLTasks").
- **SecurityLevel:** Nível de segurança exigido (ex: "High", "Confidential").

---

### **10. Projeto: Criando Grupos, Usuários e Anexando Políticas no IAM**

**Passo a Passo: Criando Grupos, Usuários e Anexando Políticas no IAM**

#### **1. Criar os Grupos no IAM**

1. **Acessar o Console IAM:**
   - Faça login no console da AWS e navegue até o serviço **IAM (Identity and Access Management)**.

2. **Criar o Grupo "EngenheiroDeDados":**
   - No painel do IAM, selecione **"Grupos"** no menu lateral.
   - Clique em **"Criar Novo Grupo"**.
   - Nome do grupo: **EngenheiroDeDados**.
   - **Anexar Políticas Diretamente:**
     - **AmazonS3FullAccess**
     - **AmazonEC2FullAccess**
     - **AmazonVPCFullAccess**
   - Clique em **"Criar Grupo"**.

3. **Criar o Grupo "CientistaDeDados":**
   - Repita o processo anterior.
   - Nome do grupo: **CientistaDeDados**.
   - **Anexar Políticas Diretamente:**
     - **AmazonAthenaFullAccess**
     - **AmazonGlueConsoleFullAccess**
   - Clique em **"Criar Grupo"**.

4. **Criar o Grupo "LambdaExecutors":**
   - Repita o processo novamente.
   - Nome do grupo: **LambdaExecutors**.
   - **Anexar Políticas Diretamente:**
     - **AWSLambdaBasicExecutionRole**
   - Clique em **"Criar Grupo"**.

#### **2. Criar os Usuários no IAM**

1. **Criar Usuário 1 (Engenheiro de Dados):**
   - No IAM, selecione **"Usuários"** no menu lateral.
   - Clique em **"Adicionar Usuário"**.
   - Nome do usuário: **Engenheiro1**.
   - **Selecionar o Tipo de Acesso:**
     - Marque **"Acesso programático"** e **"Acesso à AWS Management Console"**.
     - Defina uma senha para o console.
   - **Atribuir ao Grupo:**
     - Selecione o grupo **"EngenheiroDeDados"**.
   - Clique em **"Próximo"** e **"Criar Usuário"**.

2. **Criar Usuário 2 (Engenheiro de Dados):**
   - Repita o processo anterior.
   - Nome do usuário: **Engenheiro2**.
   - Atribua ao grupo **"EngenheiroDeDados"**.

3. **Criar Usuário 3 (Cientista de Dados):**
   - Repita o processo anterior.
   - Nome do usuário: **Cientista1**.
   - Atribua ao grupo **"CientistaDeDados"**.

4. **Criar Usuário 4 (Lambda Executor):**
   - Repita o processo anterior.
   - Nome do usuário: **LambdaExecutor1**.
   - **Atribuir ao Grupo:**
     - Selecione o grupo **"LambdaExecutors"**.

#### **3. Anexar Usuários aos Grupos e Roles**

1. **Verificar Grupos e Políticas:**
   - Navegue até a página de cada grupo (EngenheiroDeDados, CientistaDeDados, LambdaExecutors) e verifique se as políticas apropriadas foram anexadas.

2. **Anexar Roles (para Lambda):**
   - Para o usuário **LambdaExecutor1**, vá em **"Roles"** no menu do IAM.
   - Crie uma nova role chamada **LambdaExecutionRole**.
   - Anexe a política **"AmazonDynamoDBFullAccess"**.
   - Atribua a role ao usuário **LambdaExecutor1**.

#### **4. Revisão e Testes**

1. **Verificar Acessos:**
   - Faça login como cada usuário criado para verificar se as permissões e acessos aos serviços AWS estão funcionando conforme o esperado.
   - Teste a criação e o gerenciamento de recursos em S3, EC2, VPC para engenheiros de dados, Athena e Glue para cientistas de dados, e execução de funções Lambda para o executor de Lambda.

2. **Documentação e Tags:**
   - Considere adicionar tags aos usuários e grupos para facilitar a organização e a gestão dentro da AWS.

---

### **11. Melhores Práticas de IAM**

- **Princípio do Menor Privilégio**: Conceder apenas as permissões necessárias.
- **Senhas Fortes e MFA**: Utilizar autenticação multifator em todas as contas críticas.
- **Monitoramento e Auditoria**: Usar ferramentas como AWS CloudTrail para monitorar atividades.

---

### **12. Acesso Programático na AWS**

**O que é Acesso Programático?**  
Acesso programático permite que você interaja com os serviços da AWS usando a AWS CLI, SDKs (como boto3 para Python), e ferramentas de automação. É ideal para cenários onde você precisa integrar seus aplicativos ou scripts com a AWS para gerenciar e operar recursos na nuvem.

### **Cenário: Construindo um Projeto Python que Precisa de Acesso a um Projeto Específico**

Se você está construindo um projeto Python que precisa de acesso a recursos específicos na AWS, como S3, DynamoDB, ou EC2, você deve criar um usuário IAM com permissões programáticas específicas para o projeto. Aqui está como fazer isso:

---

### **13. Passo a Passo para Criar Acesso Programático para um Projeto Específico**

1. **Acessar o Console IAM:**
   - Faça login no console da AWS.
   - Navegue até o serviço **IAM (Identity and Access Management)**.

2. **Criar um Novo Usuário:**
   - No painel do IAM, selecione **"Usuários"** no menu lateral.
   - Clique em **"Adicionar Usuário"**.
   - Nome do usuário: Escolha

 um nome que reflita o propósito do projeto, como **"ProjetoPythonUser"**.

3. **Selecionar o Tipo de Acesso:**
   - Marque **"Acesso programático"**. Isso gerará um **Access Key ID** e **Secret Access Key**, que você usará para configurar as credenciais no seu código Python.

4. **Configurar Permissões:**
   - **Criar uma Política Personalizada** (opcional):
     - Selecione **"Anexar Políticas Diretamente"** e procure pelas políticas gerenciadas que você precisa, ou crie uma política personalizada que conceda apenas as permissões necessárias para o projeto específico.
     - Exemplo de serviços que você pode precisar:
       - **AmazonS3FullAccess** para interagir com buckets S3.
       - **AmazonDynamoDBFullAccess** para trabalhar com tabelas DynamoDB.
       - **AmazonEC2FullAccess** se seu projeto gerencia instâncias EC2.
   - **Anexar Políticas ao Usuário**: Selecione as políticas necessárias para o usuário conforme o escopo do projeto.

5. **Revisar e Criar o Usuário:**
   - Revise as configurações e clique em **"Criar usuário"**.
   - **Download do CSV**: Baixe o arquivo CSV que contém o **Access Key ID** e o **Secret Access Key**. Estas credenciais serão usadas para configurar o acesso programático no seu projeto Python.

6. **Configurar o Projeto Python:**
   - No seu ambiente de desenvolvimento, configure as credenciais AWS usando o SDK boto3 ou outro SDK apropriado.
   - Exemplo em Python usando boto3:
     ```python
     import boto3

     # Configurando o acesso com as credenciais do IAM
     session = boto3.Session(
         aws_access_key_id='your-access-key-id',
         aws_secret_access_key='your-secret-access-key',
         region_name='your-region'  # Ex: 'us-east-1'
     )

     # Exemplo de uso do S3
     s3 = session.resource('s3')
     for bucket in s3.buckets.all():
         print(bucket.name)
     ```

### **14. Recomendações**

- **Princípio do Menor Privilégio**: Sempre conceda apenas as permissões necessárias para o projeto específico. Se o projeto só precisa acessar o S3, evite adicionar permissões desnecessárias para outros serviços.
- **Segurança das Credenciais**: Armazene as credenciais de forma segura e evite commitá-las em sistemas de controle de versão, como Git. Use serviços como AWS Secrets Manager ou variáveis de ambiente para gerenciar credenciais de maneira segura.

### **15. Exemplo de Uso de Role no IAM: EC2 com Acesso ao S3**

**Cenário Real**: Suponha que você esteja configurando uma instância EC2 na AWS que precisa acessar um bucket S3 para armazenar ou recuperar dados. Em vez de configurar credenciais de acesso diretamente na instância (o que pode ser inseguro), você pode usar uma **IAM Role** para conceder à instância EC2 as permissões necessárias para interagir com o S3. Isso é uma prática recomendada para aumentar a segurança e simplificar o gerenciamento de permissões.

### **Passo a Passo para Criar uma Role para EC2 com Acesso ao S3**

1. **Criar uma IAM Role**

   1.1. **Acessar o Console IAM**:
   - Faça login no console da AWS e navegue até o serviço **IAM (Identity and Access Management)**.
   - No menu lateral, selecione **"Roles"** e clique em **"Create Role"**.

   1.2. **Escolher o Tipo de Trusted Entity**:
   - Na tela de criação da role, selecione **"AWS Service"** como o tipo de trusted entity.
   - Em seguida, selecione **EC2** como o serviço que usará esta role.

   1.3. **Anexar Políticas de Permissão**:
   - Na etapa de anexar políticas, procure pela política gerenciada **AmazonS3FullAccess** ou **AmazonS3ReadOnlyAccess**, dependendo das necessidades do seu projeto.
   - Selecione a política e clique em **"Next"**.

   1.4. **Configurar Nome e Tags**:
   - Dê um nome descritivo para a role, como **EC2-S3-Access-Role**.
   - (Opcional) Adicione tags para facilitar a gestão e identificação da role.

   1.5. **Revisar e Criar a Role**:
   - Revise as configurações e clique em **"Create Role"**.

2. **Atribuir a Role à Instância EC2**

   2.1. **Criar ou Selecionar uma Instância EC2**:
   - Navegue até o serviço **EC2** no console da AWS.
   - Ao criar uma nova instância, na etapa de configuração, procure a seção **IAM role** e selecione a role **EC2-S3-Access-Role** criada anteriormente.

   2.2. **Anexar a Role a uma Instância Existente**:
   - Se você já possui uma instância EC2 em execução, vá para o painel de **Instâncias** no EC2.
   - Selecione a instância desejada, clique em **Actions** > **Security** > **Modify IAM Role**.
   - Selecione a role **EC2-S3-Access-Role** e clique em **Update IAM Role**.

3. **Testar o Acesso do EC2 ao S3**

   3.1. **Acessar a Instância EC2**:
   - Conecte-se à instância EC2 via SSH.

   3.2. **Verificar o Acesso ao S3**:
   - Usando a AWS CLI, execute um comando simples para listar os buckets S3:
     ```bash
     aws s3 ls
     ```
   - Se a role foi atribuída corretamente, você verá a lista de buckets no S3.

   3.3. **Exemplo de Uso no Código**:
   - Se o seu aplicativo na EC2 precisa interagir com o S3 programaticamente, você pode usar o SDK da AWS (por exemplo, boto3 para Python) sem precisar gerenciar manualmente as credenciais:
     ```python
     import boto3

     s3 = boto3.client('s3')
     response = s3.list_buckets()
     for bucket in response['Buckets']:
         print(f'Bucket Name: {bucket["Name"]}')
     ```

### **Por Que Usar uma IAM Role em EC2?**

- **Segurança**: Evita o uso de credenciais embutidas na instância, que podem ser comprometidas.
- **Gerenciamento Simplificado**: As permissões são centralizadas na role e podem ser ajustadas sem necessidade de alterar a configuração da instância.
- **Automação e Escalabilidade**: Ao usar uma role, o acesso a recursos AWS pode ser facilmente gerenciado em grandes ambientes de forma consistente e segura.

Esse é um cenário muito comum em projetos na nuvem, onde a segurança e a facilidade de gerenciamento são cruciais para o sucesso e a manutenção da infraestrutura.

Exatamente! Essa é uma das principais vantagens de usar uma **IAM Role** para uma instância EC2.

### **Vantagens da IAM Role em uma Instância EC2**

1. **Eliminação da Necessidade de Credenciais Embutidas**: 
   - Quando você atribui uma IAM Role a uma instância EC2, o código ou os scripts que você executa nessa instância podem acessar diretamente os recursos da AWS (como S3, DynamoDB, etc.) sem precisar incluir manualmente as **Access Key** e **Secret Access Key** no código. Isso reduz o risco de exposição dessas credenciais, que poderiam ser comprometidas se fossem incluídas diretamente no código.

2. **Segurança Aprimorada**:
   - Ao evitar o uso de credenciais embutidas, você minimiza o risco de que essas credenciais sejam expostas ou mal utilizadas. A IAM Role é gerenciada pela AWS, e as permissões podem ser ajustadas centralmente sem necessidade de atualizar o código na instância.

3. **Gerenciamento Simples e Centralizado**:
   - Com IAM Roles, as permissões para acessar diferentes serviços AWS são definidas de maneira centralizada. Isso facilita a gestão das permissões à medida que o ambiente cresce, sem necessidade de modificar cada instância individualmente.

4. **Rotação Automática de Credenciais**:
   - A AWS automaticamente gerencia e rotaciona as credenciais temporárias associadas a uma IAM Role. Isso significa que as credenciais são continuamente atualizadas sem intervenção manual, garantindo que o acesso continue seguro.

### **Como Funciona na Prática?**

Sim, se você subir um código Python na instância EC2 que tem uma IAM Role configurada com acesso ao S3, por exemplo, você **não precisará especificar as chaves de acesso**. O código simplesmente usará as permissões da IAM Role atribuída à instância para acessar os recursos. Aqui está um exemplo simples:

```python
import boto3

# Não é necessário especificar aws_access_key_id ou aws_secret_access_key
s3 = boto3.client('s3')

# Listando os buckets no S3
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}')
```

Neste exemplo, o código Python roda na instância EC2 e usa automaticamente as permissões da IAM Role para interagir com o S3, sem que você precise se preocupar com as credenciais. Isso torna o processo mais seguro, eficiente e fácil de gerenciar.