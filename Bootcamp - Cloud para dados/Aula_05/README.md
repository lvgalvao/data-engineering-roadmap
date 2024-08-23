# Bootcamp Cloud: Aula 05

## S3: Armazenamento de Dados na AWS

**Objetivo:** Explorar as diversas aplicações do Amazon S3 no contexto de engenharia, ciência e análise de dados, com um foco prático em como configurar e utilizar o serviço via script Python usando o boto3. Além disso, abordaremos a criação de um IAM exclusivo e um grupo de recursos para gerenciar acesso e segurança.

---

## 1. IAM Inicial: Introdução ao IAM e Criação de Políticas para o S3

### 1.1 O que é IAM?

**IAM (Identity and Access Management)** é um serviço da AWS que permite gerenciar o acesso aos recursos da AWS de forma segura. Com IAM, você pode criar e gerenciar usuários e grupos, definir permissões para permitir ou negar acesso a recursos da AWS, e controlar o que cada usuário ou grupo pode fazer dentro da sua conta AWS.

#### **Componentes Principais do IAM:**

- **Usuários:** Representam uma pessoa ou aplicação que interage com os recursos da AWS. Cada usuário tem credenciais de segurança únicas.
- **Grupos:** São conjuntos de usuários que compartilham permissões comuns. Ao adicionar usuários a um grupo, você concede automaticamente as permissões do grupo aos usuários.
- **Policies (Políticas):** São documentos em JSON que definem as permissões para usuários, grupos e roles. Uma política pode permitir ou negar ações específicas em recursos específicos.
- **Roles:** São conjuntos de permissões que você pode atribuir a serviços da AWS ou a aplicações em execução na AWS.

### 1.2 Criando uma Política Específica para Acesso a um Único Bucket

**Objetivo:** Criar uma política que permita a um usuário acessar apenas um bucket específico no S3, com permissões de leitura e escrita.

#### Passo 1: Escrever a Política JSON

1. **Estrutura Básica da Política:**
   - A política em JSON deve especificar o bucket S3 em questão e as ações permitidas (como `s3:GetObject` para leitura e `s3:PutObject` para escrita).

   ```json
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "s3:GetObject",
                   "s3:PutObject",
                   "s3:ListBucket"
               ],
               "Resource": [
                   "arn:aws:s3:::nome-do-bucket-especifico",
                   "arn:aws:s3:::nome-do-bucket-especifico/*"
               ]
           }
       ]
   }
   ```

   - **Effect:** Define se a política permite (`Allow`) ou nega (`Deny`) as ações especificadas.
   - **Action:** Lista as ações permitidas no bucket. Nesse caso, estamos permitindo `s3:GetObject`, `s3:PutObject`, e `s3:ListBucket`.
   - **Resource:** Define os recursos específicos aos quais a política se aplica. O primeiro ARN (Amazon Resource Name) refere-se ao próprio bucket, enquanto o segundo ARN refere-se a todos os objetos dentro do bucket.

#### Passo 2: Criar a Política no AWS IAM

1. **Acessando o IAM:**
   - No AWS Management Console, navegue até o serviço IAM.

2. **Criando a Política:**
   - No menu lateral, clique em “Policies” e depois em “Create policy”.
   - Escolha a aba “JSON” e cole a política que você escreveu no passo anterior.
   - Clique em “Next: Tags” (opcionalmente adicione tags) e depois em “Next: Review”.
   - Dê um nome à política (ex: `S3SpecificBucketAccessPolicy`) e uma descrição, se desejar.
   - Clique em “Create policy” para finalizar.

### 1.3 Criando um Usuário com Acesso Específico ao Bucket

**Objetivo:** Criar um usuário IAM que tenha a política recém-criada aplicada, permitindo que ele acesse somente o bucket específico no S3.

#### Passo 1: Criar o Usuário no IAM

1. **Acessando a Seção de Usuários:**
   - No console do IAM, clique em “Users” no menu lateral e depois em “Add user”.

2. **Configuração Inicial do Usuário:**
   - Dê um nome ao usuário (ex: `s3-specific-bucket-user`).
   - Selecione o tipo de acesso:
     - **Programmatic access:** Se o usuário for interagir com a AWS via API, CLI, ou SDK (por exemplo, usando boto3).
     - **AWS Management Console access:** Se o usuário precisar acessar o console web da AWS.
   - Defina a senha, caso tenha habilitado o acesso ao console.

#### Passo 2: Atribuir a Política ao Usuário

1. **Atribuindo a Política Criada:**
   - Após configurar o acesso, você será solicitado a atribuir permissões ao usuário.
   - Escolha "Attach existing policies directly".
   - Na lista de políticas, procure pela política que você criou (`S3SpecificBucketAccessPolicy`) e marque-a.
   - Clique em “Next: Tags” (opcionalmente adicione tags) e depois em “Next: Review”.

2. **Finalizando a Criação do Usuário:**
   - Revise as configurações e clique em “Create user”.
   - Na próxima tela, você verá as credenciais do usuário (Access Key ID e Secret Access Key), que devem ser salvas em um local seguro. Essas credenciais serão usadas para que o usuário possa acessar o bucket S3 especificado.

---

**Conclusão:** Neste tópico, você aprendeu a criar e aplicar uma política de IAM específica para acessar um único bucket S3, além de configurar um usuário IAM com essa política. Isso garante que o usuário tenha acesso restrito, seguindo as melhores práticas de segurança.