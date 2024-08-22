# Bootcamp Cloud: Aula 01

## Introdução à AWS e Cloud Computing

**Objetivo:** Fornecer uma introdução prática ao uso da AWS, abordando a criação de contas, controle de custos e navegação na interface gráfica, com foco em aplicações na área de dados.

---

## 1. Por que Utilizar Cloud?

1. **Escalabilidade:** A cloud permite escalar recursos conforme necessário, sem a necessidade de grandes investimentos iniciais.
2. **Custo-eficiência:** Com a cloud, você paga apenas pelo que utiliza, reduzindo custos operacionais.
3. **Acessibilidade:** Serviços de cloud podem ser acessados de qualquer lugar, facilitando a colaboração e o trabalho remoto.
4. **Segurança:** Provedores de cloud como AWS oferecem robustos recursos de segurança, incluindo criptografia e autenticação multifator.

## 2. O que Não é Cloud

1. **Não é um Data Center On-Premise:** Embora a cloud envolva servidores, não é o mesmo que ter um data center físico na empresa.
2. **Não é apenas armazenamento:** Cloud envolve muito mais do que apenas guardar dados. É um ecossistema completo de serviços.
3. **Não é sempre barato:** Se mal gerido, o uso da cloud pode resultar em custos inesperados.

## 3. Acessando o Site da AWS

1. **Site da AWS:** Visite [aws.amazon.com](https://aws.amazon.com).
2. **Trocando o Idioma:** 
   - No canto superior direito, clique no ícone de globo e selecione “English”.
   - **Motivo:** O inglês é o idioma predominante em certificações, documentação, vagas de emprego, e na própria interface da AWS.

## 4. Cadastro e Configuração Inicial da Conta AWS

**Criar uma Conta na AWS:**
1. Acesse o site oficial da AWS (aws.amazon.com) e clique em "Create an AWS Account".
2. Insira as informações solicitadas, como e-mail, senha e nome da conta.
3. Selecione o tipo de conta e forneça as informações de pagamento (cartão de crédito/débito).
4. Verifique a conta via e-mail e complete o processo de criação.

**Configurações Iniciais:**
- Opte pelo **AWS Free Tier**, que oferece uma camada gratuita com serviços limitados por 12 meses, ideal para quem está começando.
- Após o cadastro, revise as configurações de segurança e habilite a autenticação multifator (MFA) para proteger a conta.

## 5. Controle de Custos na AWS

**Evitar Custos Inesperados:**
- **AWS Budgets:** Use o AWS Budgets para configurar alertas de custo. Acesse o serviço pelo console, defina um orçamento mensal e configure notificações por e-mail.
- **AWS Cost Explorer:** Monitore os gastos em tempo real utilizando o AWS Cost Explorer, que permite visualizar detalhadamente onde e como os recursos estão sendo utilizados.

**Dicas Práticas:**
- Defina **limites de serviço** para evitar que recursos sejam provisionados além do necessário.
- Revise regularmente as instâncias e serviços em execução e encerre aqueles que não estão em uso.

## 6. Navegação na Interface Gráfica da AWS

**AWS Management Console:**
- O **AWS Management Console** é o painel de controle principal da AWS. Ele oferece acesso a todos os serviços disponíveis na plataforma, como S3, EC2 e RDS.

**Serviços Comuns:**
- **S3 (Simple Storage Service):** Armazenamento escalável de objetos, ideal para dados brutos, backups e arquivos de grande volume.
- **EC2 (Elastic Compute Cloud):** Serviço que permite criar e gerenciar instâncias de máquinas virtuais na nuvem, altamente configuráveis.
- **RDS (Relational Database Service):** Serviço gerenciado de banco de dados relacional, que suporta mecanismos como MySQL, PostgreSQL, e SQL Server.

**Documentação e Suporte:**
- A AWS oferece documentação abrangente e suporte direto pelo console. Acesse a documentação para obter informações detalhadas sobre cada serviço e suas configurações.

## 7. Visão Geral dos Produtos AWS

1. **Explorando Todos os Produtos:**
   - Navegue até a seção "Products" no menu principal.
   - Explore as diversas categorias: Computação, Armazenamento, Banco de Dados, etc.

2. **EC2 (Elastic Compute Cloud):**
   - **Visão Geral:** Serviço que permite criar instâncias de servidores virtuais.
   - **Instâncias de Todos os Tipos:** De uso geral, otimizadas para memória, para computação, etc.
   - **Democratização:** A cloud, ao permitir acesso fácil a essas tecnologias, democratiza o acesso à internet e ao conhecimento técnico.

3. **Visão Geral de Vários Tipos de Banco de Dados:**
   - **RDS (Relational Database Service):** Gerencia bancos de dados como MySQL, PostgreSQL, e SQL Server.
   - **DynamoDB:** Banco de dados NoSQL totalmente gerenciado.
   - **Redshift:** Armazenamento e análise de dados em larga escala.
   
   **Motivação para Estudo:** Ao explorar os diferentes tipos de bancos de dados, você é motivado a estudar e entender novas tecnologias.

## 8. Tipos de Serviço AWS

1. **Free Tier:**
   - **12 Meses Gratuitos:** Oferece acesso gratuito a muitos serviços durante o primeiro ano.
   - **Trial Limitado:** Alguns serviços têm um período de trial limitado a 1-3 meses.

## 9. Configuração de Regiões

**Regiões e Zonas de Disponibilidade:**
- **Regiões** são locais geográficos onde a AWS mantém seus data centers. Cada região é composta por várias **Zonas de Disponibilidade**, que são grupos de data centers fisicamente separados.
- A escolha da região influencia a latência dos serviços e pode ter implicações legais e de conformidade, dependendo dos dados armazenados.

**Escolha da Região:**
- Selecione a região mais próxima dos seus usuários ou que atenda aos requisitos específicos de conformidade do seu projeto. No console da AWS, é possível alternar facilmente entre diferentes regiões.

## 10. Configuração de IAM (Identity and Access Management)

**Importância do IAM:**
- Criação de usuários e grupos com permissões específicas.
- Segurança aprimorada com autenticação multifator (MFA).

**Criar um Fator de Autenticação:**
- Acesse o IAM no console AWS.
- Vá para “Users” e selecione seu usuário root.
- Clique em “Security credentials” e ative o MFA.

**Uso do Authy:**
- Utilize o Authy como aplicativo MFA para adicionar uma camada extra de segurança.

**Criar um Acesso Admin no IAM:**
- Vá para "Users" e clique em "Add user".
- Crie um usuário com "Programmatic access" e "AWS Management Console access".
- Defina a senha e anote a Access Key.
- **Add User to Group:** Adicione o usuário ao grupo "Administrators".
- **Attach Permissions:** Associe a permissão "AdministratorAccess".
- **Tags:** Adicione tags para identificar e gerenciar o usuário.
- **Regions:** Defina as regiões de uso para o usuário.

## 11. Criando o Nosso Primeiro Serviço S3

Nesta seção, vamos aprender a criar e configurar um bucket S3 na AWS, além de explorar como armazenar arquivos, configurar permissões e servir um site estático.

### 11.1 Criando o Bucket S3

1. **Nome do Bucket:**
   - Escolha um nome único para o seu bucket. Lembre-se que o nome deve ser globalmente único dentro da AWS.
  
2. **Zona (Region):**
   - Selecione a região onde o bucket será criado. É recomendável escolher a região mais próxima dos seus usuários para reduzir latência.

3. **ACLs (Access Control Lists):**
   - Configure as listas de controle de acesso (ACLs) para definir permissões de leitura e escrita. Por padrão, é melhor manter o controle de acesso restrito.

4. **Bucket Público:**
   - Inicialmente, o bucket deve ser privado por questões de segurança. Se for necessário torná-lo público, isso pode ser feito posteriormente.

5. **Bucket Versioning:**
   - Habilite o versionamento do bucket para manter várias versões de um objeto. Isso pode ser útil para recuperação de dados e auditoria.

6. **Tags:**
   - Adicione tags para identificar e organizar seu bucket. Tags podem incluir informações como ambiente (produção, desenvolvimento), proprietário, e finalidade.

7. **Default Encryption:**
   - Configure a criptografia padrão para garantir que todos os objetos armazenados no bucket sejam criptografados automaticamente.

### 11.2 Acessando o Bucket

- Depois de criar o bucket, acesse-o através do console da AWS. Na interface do bucket, você pode ver e gerenciar todos os objetos armazenados.

### 11.3 Colocando uma Imagem no Bucket

1. **Upload de Arquivo:**
   - Faça upload de uma imagem ou qualquer outro arquivo no bucket.
  
2. **Verificando o Arquivo:**
   - Após o upload, tente acessar o arquivo diretamente. Você notará que, por padrão, o arquivo não será acessível publicamente.

### 11.4 Configurando Permissões: Tornando o Arquivo Público

1. **Padrão Privado:**
   - Por padrão, todos os arquivos em um bucket S3 são privados, ou seja, somente você pode acessá-los.
  
2. **Tornar o Arquivo Público:**
   - Para tornar o arquivo acessível publicamente, você pode modificar as permissões do arquivo ou configurar uma política de bucket.

### 11.5 Bucket Policy: Exemplo de Permissão de Leitura para Usuário Anônimo

- **Bucket Policy:**
   - Adicione uma política ao bucket para permitir que usuários anônimos leiam os arquivos. Um exemplo de política de leitura pública para um bucket S3 pode ser adicionado através do editor de políticas no console da AWS.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicReadGetObject",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::nome-do-bucket/*"
        }
    ]
}
```

### 11.6 Adicionando um Arquivo `index.html`

- **Upload do Arquivo `index.html`:**
   - Adicione um arquivo `index.html` ao seu bucket. Esse arquivo servirá como a página principal do seu site estático.

### 11.7 Abrindo um Website Estático

1. **Configuração de Website Estático:**
   - No console do S3, habilite a opção de hospedagem de site estático. Defina o `index.html` como o documento de índice.
  
2. **Acessando o Website:**
   - Após a configuração, você poderá acessar o site via URL fornecida pelo S3.

### 11.8 Retornando o `index.html` Diretamente na Raiz

- **Configurando o Redirecionamento:**
   - Configure para que o `index.html` seja servido diretamente na raiz do site, garantindo que o usuário veja o conteúdo imediatamente ao acessar o URL do bucket.

### 11.9 O que é um Site Estático?

- **Definição:**
   - Um site estático é um site cujas páginas são servidas exatamente como são armazenadas, sem processamento dinâmico. Isso significa que não há interação com banco de dados ou scripts do lado do servidor, tornando-o ideal para conteúdos simples, como blogs ou páginas de portfólio.

   Aqui está o passo a passo atualizado, começando com o comando `sudo su` para obter acesso root, definindo uma senha para o root, e então seguindo com a instalação do Python e Streamlit, além da execução do aplicativo.

## 12. Criando e Configurando uma Instância EC2

Nesta seção, vamos aprender a configurar uma instância EC2, obter acesso root, definir uma senha para o root, e depois configurar o ambiente com Python e Streamlit para rodar um aplicativo básico de "Hello World", incluindo a renderização de uma imagem armazenada no S3.

### 12.1 Conectando-se à Instância EC2 e Obtendo Acesso Root

1. **Conectar-se via SSH:**
   - Use o comando SSH no terminal para conectar-se à instância. O comando será algo assim:

   ```bash
   ssh -i "caminho-para-sua-chave.pem" ec2-user@seu-endereco-publico-ec2
   ```

2. **Obter Acesso Root:**
   - Assim que estiver conectado, troque para o usuário root usando o comando:

   ```bash
   sudo su
   ```

3. **Definir uma Senha para o Root (se necessário):**
   - Se você ainda não configurou uma senha para o root, ou deseja alterá-la, execute:

   ```bash
   passwd
   ```

   - Você será solicitado a digitar a nova senha para o root e confirmá-la.

### 12.2 Instalando Python, `pip3`, e Streamlit

1. **Atualizar Pacotes e Instalar Python:**
   - Primeiro, atualize os pacotes e instale Python 3 com os seguintes comandos:

   ```bash
   yum update -y
   yum install python3 -y
   ```

2. **Instalando o `pip3`:**
   - Instale o `pip3`, que é o gerenciador de pacotes para Python 3:

   ```bash
   yum install python3-pip -y
   ```

3. **Verificando a Instalação do `pip3`:**
   - Verifique se o `pip3` foi instalado corretamente:

   ```bash
   pip3 --version
   ```

4. **Instalando o Streamlit:**
   - Agora que o `pip3` está instalado, você pode instalar o Streamlit com o comando:

   ```bash
   pip3 install streamlit
   ```

### 12.3 Criando o Código do Streamlit com a Imagem

1. **Criar um Arquivo Python para o Streamlit:**
   - Use o editor de texto `nano` para criar e editar o arquivo `app.py`. No terminal, execute:

   ```bash
   nano app.py
   ```

2. **Inserir o Código para Renderizar a Imagem:**
   - Insira o seguinte código no arquivo `app.py`:

   ```python
   import streamlit as st

   # Título do aplicativo
   st.title("Hello, World!")

   # Descrição
   st.write("Este é um simples aplicativo Streamlit rodando em uma instância EC2 na AWS.")
   ```

3. **Salvar o Arquivo e Sair do Editor:**
   - Para salvar o arquivo, pressione `Ctrl + O` e depois `Enter`.
   - Para sair do editor `nano`, pressione `Ctrl + X`.

### 12.4 Executando o Streamlit na Porta 80

1. **Executar o Streamlit na Porta 80:**
   - Agora que você está logado como root, execute o Streamlit na porta 80:

   ```bash
   streamlit run app.py --server.port 80 --server.enableCORS false
   ```

2. **Acessar a Aplicação:**
   - Acesse o aplicativo no navegador através do endereço IP público da sua instância EC2:

   ```http
   http://seu-endereco-publico-ec2
   ```

### Resultado Esperado

Ao acessar o aplicativo, você verá o título "Hello, World!", uma descrição, e a imagem "fotodaturma.png" renderizada diretamente do S3, com a legenda "Foto da Turma - Primeiro Dia".