# Bootcamp Cloud: Aula 02

## S3: Armazenamento de Dados na AWS

**Objetivo:** Explorar as diversas aplicações do Amazon S3 no contexto de engenharia, ciência e análise de dados, com um foco prático em como configurar e utilizar o serviço via script Python usando o boto3. Além disso, abordaremos a criação de um IAM exclusivo e um grupo de recursos para gerenciar acesso e segurança.

---

### 1. Revisão da Aula Anterior: Verificando Gastos de Ontem e Usando Tags para Filtragem

**Objetivo:** Aprender a utilizar o AWS Cost Explorer para verificar os gastos do dia anterior e aplicar filtros utilizando tags criadas durante o gerenciamento dos recursos.

#### Passo 1: Acessar o AWS Cost Explorer

1. **Login no AWS Management Console:**
   - Acesse sua conta AWS e no console, digite "Cost Explorer" na barra de pesquisa superior e selecione "Cost Explorer" nos resultados.

2. **Ativando o Cost Explorer (se necessário):**
   - Se esta for a primeira vez que você está usando o Cost Explorer, será necessário ativá-lo. Clique em "Enable Cost Explorer".

#### Passo 2: Verificar os Gastos de Ontem

1. **Configurar o Período de Tempo:**
   - No Cost Explorer, selecione o intervalo de datas. No campo "Filter by Date", escolha a data de ontem como início e fim.

2. **Visualizar Gastos:**
   - O Cost Explorer mostrará os gastos do dia anterior, distribuídos por serviço, região, ou qualquer outro filtro padrão da AWS.

#### Passo 3: Usar Tags para Filtragem de Custos

1. **Aplicar Filtros de Tag:**
   - Para ver os custos associados a um grupo específico de recursos, clique em "Add Filter" e selecione "Tag".

2. **Selecionar Tags Relevantes:**
   - Escolha a tag que você criou anteriormente, como `Environment: Production` ou `Project: DataAnalysis`. Isso permitirá que você visualize apenas os custos associados a recursos marcados com essas tags.

3. **Analisar Resultados:**
   - O Cost Explorer atualizará os resultados para mostrar apenas os gastos relacionados aos recursos que possuem a tag selecionada.

#### Passo 4: Configurar Relatórios Personalizados

1. **Criar um Relatório Customizado:**
   - Se você quiser acompanhar esses custos regularmente, pode criar um relatório customizado clicando em "Save as Report".
   - Dê um nome ao relatório (ex: "Gastos Diários por Tag") e defina as configurações para receber atualizações automáticas por e-mail.

#### Passo 5: Boas Práticas ao Usar Tags e Monitorar Custos

1. **Consistência na Aplicação de Tags:**
   - Certifique-se de que todas as equipes utilizem as mesmas convenções de tags para facilitar a filtragem e monitoramento dos custos.

2. **Revisão Regular de Custos:**
   - Incorpore a revisão diária ou semanal dos custos como parte do seu workflow para evitar surpresas no faturamento.

3. **Alertas de Orçamento:**
   - Use o AWS Budgets para criar alertas de orçamento baseados em tags, garantindo que você seja notificado se os gastos superarem os limites previstos.

---

## 2. O que é Storage?

1. **Definição:**
   - Storage, ou armazenamento, refere-se ao espaço onde dados digitais são guardados. No contexto da AWS, o S3 é um serviço de storage de objetos, onde arquivos de todos os tipos e tamanhos podem ser armazenados e acessados com alta disponibilidade e durabilidade.

2. **Tipos de Storage na AWS:**
   - Além do S3, a AWS oferece outros tipos de storage, como EBS (Elastic Block Store) para armazenamento de blocos, e o Amazon EFS (Elastic File System) para armazenamento de arquivos. O S3 é focado no armazenamento de objetos, ideal para grandes volumes de dados não estruturados.

### 2.1 Vantagem da Redundância

1. **O que é Redundância?**
   - Redundância em storage se refere à duplicação de dados em múltiplos locais para garantir a disponibilidade e durabilidade dos dados, mesmo em caso de falhas.

2. **Vantagem da Redundância no S3:**
   - O Amazon S3 armazena automaticamente os dados em pelo menos três zonas de disponibilidade (AZs) dentro de uma região, oferecendo proteção contra falhas em qualquer uma dessas zonas.
   - Isso garante que os dados estejam sempre acessíveis e seguros, mesmo em situações de desastres naturais ou falhas em data centers.

3. **Como Funciona a Redundância no S3?**
   - Ao enviar um arquivo para um bucket S3, o dado é replicado automaticamente em múltiplas AZs. Essa replicação é transparente para o usuário, que não precisa se preocupar com a configuração ou gerenciamento desse processo.
   - A redundância é uma das principais razões pelas quais o S3 oferece uma durabilidade de 99.999999999% (11 noves), garantindo que os dados sejam preservados a longo prazo.

---

## 3. Criação de um Bucket S3: Passo a Passo e Detalhes

### 3.1 Criando um Bucket S3 via AWS Management Console

1. **Acessando o AWS Management Console:**
   - Faça login no [AWS Management Console](https://aws.amazon.com) e navegue até o serviço S3. Isso pode ser feito digitando "S3" na barra de pesquisa superior e selecionando "S3" nos resultados.

2. **Iniciando a Criação do Bucket:**
   - Na página do S3, clique em “Create bucket” para iniciar o processo de criação.

3. **Nome do Bucket:**
   - **Bucket name:** Insira um nome único para o bucket. O nome deve ser globalmente exclusivo em todas as regiões da AWS e seguir as regras de nomenclatura (por exemplo, sem espaços, apenas caracteres minúsculos).
   - **Exemplo:** `meu-bucket-dados-2024`

4. **Escolhendo a Região:**
   - **Region:** Selecione a região onde o bucket será criado. A escolha da região pode afetar a latência e os custos de transferência de dados. É recomendável escolher uma região próxima dos usuários finais ou do local onde os dados serão processados.
   - **Exemplo:** `US West (Oregon)`

5. **Configurações de Controle de Acesso:**
   - **Block Public Access settings for this bucket:** Por padrão, a AWS bloqueia o acesso público a novos buckets. Deixe essa configuração ativada para garantir a segurança dos dados.
   - **Block all public access:** Mantendo essa opção ativada, você evita que qualquer pessoa fora da sua conta AWS tenha acesso aos dados do bucket.

6. **Configurações de Versionamento:**
   - **Bucket Versioning:** Habilitar o versionamento permite que o S3 mantenha várias versões de um objeto, o que é útil para proteção contra exclusões acidentais e para auditoria.
   - **Opções:**
     - **Enable:** Ativa o versionamento.
     - **Disable:** Desativa o versionamento (padrão).
     - **Suspend:** Suspende o versionamento, mantendo versões anteriores sem criar novas versões.
   - **Recomendação:** Habilitar o versionamento se o bucket for usado para armazenar dados críticos ou históricos.

7. **Configurações de Logs de Acesso:**
   - **Server access logging:** Essa opção permite registrar todas as solicitações de acesso ao bucket, o que é útil para auditoria e monitoramento de segurança.
   - **Opções:**
     - **Enable:** Ativa o registro de logs.
     - **Target bucket:** Especifique um bucket para armazenar os logs de acesso.
     - **Target prefix:** Defina um prefixo para os logs, organizando-os dentro do bucket de destino.
   - **Recomendação:** Ativar se precisar monitorar acessos ao bucket.

8. **Criptografia:**
   - **Default encryption:** A criptografia padrão garante que todos os objetos armazenados no bucket sejam criptografados automaticamente.
   - **Opções:**
     - **AES-256:** Criptografia usando a chave gerenciada pela AWS (AES-256).
     - **AWS-KMS:** Criptografia com uma chave gerenciada pelo AWS Key Management Service (KMS), o que oferece maior controle sobre as chaves de criptografia.
   - **Recomendação:** Habilitar a criptografia padrão, especialmente se você estiver armazenando dados sensíveis.

9. **Etiquetas (Tags):**
   - **Add tags:** As tags são pares chave-valor que ajudam a organizar e gerenciar seus buckets.
   - **Exemplo:** 
     - **Key:** `Environment`
     - **Value:** `Production`
   - **Recomendação:** Usar tags para facilitar a identificação e gerenciamento de buckets em ambientes grandes ou complexos.

10. **Gerenciamento de Ciclo de Vida:**
    - **Object Lock:** Esse recurso protege os objetos de serem excluídos ou modificados por um período especificado. É útil para conformidade regulatória e proteção contra exclusão acidental.
    - **Opções:**
      - **Enable:** Ativa o Object Lock (requer habilitação de versionamento).
    - **Recomendação:** Ativar apenas se houver necessidade específica de reten

ção de dados.

11. **Configurações Avançadas:**
    - **Transfer acceleration:** Acelera transferências de dados para e do bucket, usando pontos de presença da AWS globalmente.
    - **Requester Pays:** Esta configuração faz com que o solicitante pague pelos custos de download de dados do bucket, útil em cenários de compartilhamento de dados públicos.
    - **Intelligent-Tiering:** Automatiza o movimento de objetos entre camadas de armazenamento de custo mais baixo com base nos padrões de acesso.
    - **Lifecycle rules:** Crie regras de ciclo de vida para transitar objetos entre diferentes classes de armazenamento (ex: de Standard para Glacier) com base em políticas de retenção.
    - **Recomendação:** Avaliar cada uma dessas opções com base nas necessidades do projeto.

12. **Revisão e Criação do Bucket:**
    - Revise todas as configurações que você escolheu para o bucket.
    - Clique em "Create bucket" para finalizar a criação.

13. **Verificação e Acesso:**
    - Após a criação, o novo bucket aparecerá na lista de buckets do S3. Clique no nome do bucket para acessar a interface de gerenciamento, onde você pode começar a carregar arquivos, configurar permissões adicionais, ou ajustar configurações.

### 3.2 Recursos Avançados no Painel S3

1. **Intelligent-Tiering Archive Configurations:**
   - **Descrição:** O Intelligent-Tiering é uma classe de armazenamento que move automaticamente os objetos entre diferentes camadas de armazenamento (frequentemente acessado e raramente acessado) com base em padrões de acesso. É ideal para otimizar custos sem sacrificar a performance.
   - **Archive Configurations:** Permite a configuração de arquivamento de objetos para camadas de armazenamento ainda mais econômicas, como Deep Archive.

2. **Server Access Logging:**
   - **Descrição:** Essa propriedade permite registrar todas as solicitações feitas ao bucket S3, incluindo acessos e modificações. Esses logs podem ser armazenados em outro bucket S3 para auditoria e análise.
   - **Recomendação:** Habilitar logging pode ser útil para monitoramento de segurança e compliance.

3. **AWS CloudTrail Data Events:**
   - **Descrição:** AWS CloudTrail pode ser configurado para registrar eventos de dados do S3, como acessos a objetos específicos ou mudanças em permissões. **Este serviço pode ter custos associados**, especialmente se muitos eventos forem registrados.
   - **Recomendação:** Usar o CloudTrail para monitorar eventos críticos, como alterações em buckets sensíveis.

4. **Event Notifications:**
   - **Descrição:** Configura notificações para eventos específicos no bucket, como a criação de novos objetos ou exclusão de objetos. Essas notificações podem acionar funções Lambda, filas SQS, ou tópicos SNS.
   - **Exemplo de Uso:** Automatizar a geração de thumbnails quando uma nova imagem é carregada no bucket.

5. **Object Lock:**
   - **Descrição:** O Object Lock impede que objetos sejam excluídos ou sobrescritos por um período determinado, o que é útil para conformidade regulatória e prevenção de perda de dados.
   - **Recomendação:** Usar em buckets que armazenam dados sensíveis que não podem ser alterados ou excluídos.

6. **Static Website Hosting:**
   - **Descrição:** Permite configurar o bucket S3 para hospedar um site estático, servindo arquivos como HTML, CSS e JavaScript diretamente da nuvem.
   - **Exemplo de Uso:** Hospedagem de páginas web simples, como portfólios ou blogs estáticos.

### 3.3 Exemplo Prático: Bucket Temporário com Regras de Ciclo de Vida

1. **Cenário:** Vamos supor que você esteja gerenciando um pipeline de ETL (Extract, Transform, Load) onde os dados são extraídos de várias fontes e carregados em um bucket temporário para processamento.

2. **Processo:**
   - **Passo 1:** Criação do Bucket Temporário
     - Nomeie o bucket como `temp-etl-bucket`.
     - Este bucket armazena os dados extraídos antes do processamento.
   
   - **Passo 2:** Processamento dos Dados
     - Uma vez que os dados estejam no bucket temporário, um job de processamento (como um script Python ou um AWS Lambda) é acionado para transformar os dados.
     - Após o processamento, os dados transformados são movidos para um bucket final, `processed-data-bucket`.

   - **Passo 3:** Aplicação de Regras de Ciclo de Vida
     - Configure uma regra de ciclo de vida para o bucket `temp-etl-bucket`:
       - **Transição de Armazenamento:** Após 7 dias, mova os dados para uma classe de armazenamento mais econômica, como Glacier.
       - **Exclusão Automática:** Após 30 dias, exclua permanentemente os objetos do bucket.

3. **Configuração da Regra de Ciclo de Vida:**
   - No console do S3, vá para a aba “Management” e selecione “Lifecycle Rules”.
   - Clique em “Create lifecycle rule”.
   - Nomeie a regra (ex: `TempDataCleanup`).
   - Defina as condições:
     - **Prefix:** Se necessário, limite a regra a um determinado prefixo (por exemplo, `/temp`).
     - **Transition:** Mova os dados para o Glacier após 7 dias.
     - **Expiration:** Exclua os dados após 30 dias.

4. **Benefícios:**
   - **Redução de Custos:** Ao mover os dados para o Glacier e posteriormente excluí-los, você reduz custos de armazenamento.
   - **Automação:** As regras de ciclo de vida garantem que o bucket temporário seja gerenciado automaticamente, sem necessidade de intervenção manual.
   - **Segurança:** Garantir que os dados temporários sejam excluídos ajuda a minimizar riscos de segurança e conformidade.

---

## 4. Exemplo de Uso do S3 via Python (boto3)

### 4.1 Instalando o boto3

1. **Instalação do boto3:**
   - Para interagir com o S3 via Python, é necessário instalar o boto3, o SDK da AWS para Python:

   ```bash
   pip install boto3
   ```

### 4.2 Configurando Credenciais AWS

1. **Configuração das Credenciais:**
   - Antes de utilizar o boto3, é necessário configurar as credenciais da AWS. Isso pode ser feito através do `aws configure` ou definindo variáveis de ambiente.

   ```bash
   aws configure
   ```

2. **Configuração Manual (Opcional):**
   - As credenciais também podem ser configuradas manualmente:

   ```python
   import boto3

   session = boto3.Session(
       aws_access_key_id='YOUR_ACCESS_KEY',
       aws_secret_access_key='YOUR_SECRET_KEY',
       region_name='us-west-2'
   )
   s3 = session.resource('s3')
   ```

### 4.3 Criando e Gerenciando Buckets

1. **Criando um Bucket:**
   - Use o boto3 para criar um novo bucket S3:

   ```python
   import boto3

   s3 = boto3.client('s3')
   bucket_name = 'meu-novo-bucket'

   s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={
       'LocationConstraint': 'us-west-2'})
   ```

2. **Listando Buckets:**
   - Verifique todos os buckets existentes:

   ```python
   response = s3.list_buckets()

   for bucket in response['Buckets']:
       print(bucket['Name'])
   ```

### 4.4 Upload e Download de Arquivos

1. **Upload de Arquivos:**
   - Carregue um arquivo local para o S3:

   ```python
   s3.upload_file('local-file.txt', bucket_name, 's3-file.txt')
   ```

2. **Download de Arquivos:**
   - Baixe um arquivo do S3 para o sistema local:

   ```python
   s3.download_file(bucket_name, 's3-file.txt', 'local-file.txt')
   ```

### 4.5 Configurando ACLs e Políticas de Bucket

1. **Definindo Permissões de Acesso:**
   - Use boto3 para definir permissões de leitura/escrita:

   ```python
   s3.put_object_acl(Bucket=bucket_name, Key='s3-file.txt', ACL='public-read')
   ```

2. **Políticas de Bucket:**
   - Configure uma política de bucket para permitir acesso público:

   ```python
   bucket_policy = {
       'Version': '2012-10-17',
       'Statement': [{
           'Sid': 'PublicReadGetObject',
           'Effect': 'Allow',
           'Principal': '*',
           'Action': 's3:GetObject',
           'Resource': f'arn:aws:s3:::{bucket_name}/*'
       }]
   }

   s3.put_bucket_policy(Bucket=bucket_name, Policy=json.dumps(bucket_policy))
   ```

### 4.6 Excluindo Objetos e Buckets

1. **Excluir um Objeto:**
   - Remova um arquivo do S3:

   ```python
   s3.delete_object(Bucket=bucket_name, Key='s3-file.txt')
   ```

2. **Excluir um Bucket:**
   - Delete um bucket (após excluir todos os objetos):

   ```python
   s3.delete_bucket(Bucket=bucket_name)
   ```

---

## 5.

 Casos de Uso do S3 em Engenharia, Ciência e Análise de Dados

### 5.1 Engenharia de Dados

1. **Data Lake:**
   - O S3 é frequentemente utilizado como uma camada de armazenamento em data lakes, onde dados brutos de diferentes fontes são armazenados antes de serem processados e analisados.
   - Vantagens incluem escalabilidade, baixo custo, e integração com serviços como AWS Glue e Amazon Athena.

2. **ETL (Extract, Transform, Load):**
   - O S3 é essencial em pipelines ETL, onde dados são extraídos de fontes diversas, transformados, e armazenados no S3 antes de serem carregados em um data warehouse ou banco de dados.
   - Exemplos incluem armazenar arquivos CSV ou Parquet que são processados periodicamente por ferramentas como Apache Spark ou AWS Glue.

3. **Backup e Arquivamento:**
   - O S3 é uma solução robusta para backup e arquivamento de dados críticos, com suporte para versionamento e regras de ciclo de vida para mover dados entre diferentes classes de armazenamento, como S3 Glacier.

### 5.2 Ciência de Dados

1. **Armazenamento de Datasets:**
   - Cientistas de dados podem utilizar o S3 para armazenar grandes datasets que são utilizados em modelagem, treinamento de algoritmos de machine learning, e análise exploratória de dados.

2. **Integração com Amazon SageMaker:**
   - O S3 é integrado ao Amazon SageMaker, permitindo que datasets sejam carregados diretamente do S3 para notebooks e treinamentos de modelos de machine learning.
   - Modelos treinados também podem ser armazenados no S3 para versionamento e reutilização.

3. **Data Sharing e Colaboração:**
   - O S3 permite o compartilhamento de grandes datasets com equipes distribuídas ou com outros pesquisadores, através da configuração de permissões e políticas de acesso.

### 5.3 Análise de Dados

1. **Análise com Amazon Athena:**
   - O Amazon S3 pode ser usado como o local de armazenamento para dados analisados com Amazon Athena, que permite executar queries SQL diretamente sobre dados armazenados no S3 sem a necessidade de carregar esses dados para um banco de dados relacional.

2. **Dashboards e Reporting:**
   - Dados armazenados no S3 podem ser facilmente integrados a ferramentas de BI e reporting, como Amazon QuickSight ou Tableau, para criar dashboards e relatórios atualizados em tempo real.

3. **Log Storage e Análise:**
   - Logs de aplicações, servidores, e eventos podem ser armazenados no S3 e analisados usando Amazon Athena ou serviços de terceiros, ajudando a identificar padrões e insights operacionais.

---

**Conclusão:** Nesta aula, exploramos o Amazon S3 como um serviço fundamental para a gestão de dados na AWS, cobrindo desde a criação e configuração de buckets, até exemplos práticos de uso com Python e casos de uso em diferentes áreas. Além disso, discutimos boas práticas de segurança e gerenciamento de dados, incluindo o uso de IAM e grupos de recursos, para garantir que seus dados estejam seguros e bem gerenciados.