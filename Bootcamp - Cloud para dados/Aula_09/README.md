# Bootcamp Cloud: Aula 08 - Integração entre EC2 e RDS para Processamento de Requisições de API e Armazenamento de Dados

**Objetivo**: Nesta aula, vamos aprender a configurar uma instância EC2 para rodar uma aplicação de API utilizando Docker e integrar essa aplicação com um banco de dados Amazon RDS. Vamos explorar as vantagens dessa arquitetura, as melhores práticas de segurança, e como configurar os recursos necessários na AWS.

### **1. Introdução à Integração EC2 e RDS**

A combinação de instâncias EC2 com o Amazon RDS é amplamente utilizada para construir aplicações robustas que precisam processar requisições de APIs e armazenar dados em um banco de dados relacional gerenciado. EC2 oferece flexibilidade e controle sobre a execução do código da aplicação, enquanto o RDS cuida da gestão do banco de dados, garantindo alta disponibilidade, backups automatizados e segurança.

### **2. Benefícios da Integração entre EC2 e RDS**

- **Escalabilidade e Flexibilidade**: A instância EC2 permite escalabilidade horizontal da aplicação, enquanto o RDS escala automaticamente o banco de dados de acordo com a demanda.
- **Gerenciamento Simplificado**: O RDS cuida de atualizações, backups, e manutenção do banco de dados, liberando tempo para focar no desenvolvimento da aplicação.
- **Segurança Avançada**: Com o uso de Security Groups, podemos restringir o acesso ao banco de dados, garantindo que apenas a instância EC2 tenha permissão para se conectar.
- **Alto Desempenho**: O uso combinado de EC2 e RDS permite que aplicações sejam otimizadas para lidar com grandes volumes de requisições e operações de banco de dados.

### **3. Passo a Passo para Configuração da Instância EC2**

#### **3.1. Configurando a Instância EC2**

1. **Acessar o Console EC2**:
   - No console da AWS, navegue até **EC2** e clique em **"Launch Instance"**.

2. **Escolher a AMI (Amazon Machine Image)**:
   - Selecione uma AMI com Ubuntu Server (última versão LTS).

3. **Escolher o Tipo de Instância**:
   - Escolha um tipo de instância que atenda às necessidades do projeto (ex.: t2.micro para desenvolvimento ou t3.medium para produção).

4. **Configuração de Rede**:
   - Selecione a VPC e Sub-rede desejadas.
   - Configure o Security Group permitindo acesso necessário, como SSH na porta 22 para administração e outras portas conforme a aplicação.

5. **Configuração de Armazenamento**:
   - Configure o armazenamento de acordo com o necessário para a aplicação (ex.: 30GB SSD).

6. **Launch**:
   - Revise as configurações e clique em **"Launch"**. Escolha um par de chaves para acesso SSH ou crie um novo.

#### **3.2. Configurando a Aplicação na Instância EC2**

1. **Acessar a Instância via SSH**:
   - Conecte-se à instância EC2 usando o terminal:
     ```bash
     ssh -i "caminho/para/sua-chave.pem" ubuntu@seu-endereco-ec2
     ```

2. **Atualizar Pacotes e Instalar Docker e Git**:
   - Execute os seguintes comandos:
     ```bash
     sudo su
     sudo apt-get update
     sudo apt install -y git docker.io docker-compose
     ```

3. **Clonar o Repositório do Projeto**:
   - Clone o repositório do projeto:
     ```bash
     git clone https://github.com/lvgalvao/api-scheduler-python-rds.git /app
     ```

4. **Construir e Executar o Contêiner Docker**:
   - Navegue para o diretório do projeto e construa a imagem Docker:
     ```bash
     cd /app
     sudo docker build -t api-schedule-app .
     ```
   - Execute o contêiner com as variáveis de ambiente para integração com o RDS:
     ```bash
     sudo docker run -d \
     --name api-schedule-app-container \
     -e DB_HOST=<endereco-rds> \
     -e DB_USER=<usuario> \
     -e DB_PASS=<senha> \
     -e DB_NAME=<nome-do-banco> \
     api-schedule-app
     ```

### **4. Configuração do Banco de Dados Amazon RDS**

#### **4.1. Criando uma Instância RDS**

1. **Acessar o Console do RDS**:
   - Navegue até o serviço **RDS** no console da AWS e clique em **"Create Database"**.

2. **Escolher o Mecanismo do Banco de Dados**:
   - Selecione o banco de dados desejado (ex.: PostgreSQL, MySQL).
   - Escolha a versão de acordo com os requisitos do projeto.

3. **Configurações da Instância**:
   - **DB Instance Class**: Escolha uma classe de instância compatível com a carga esperada (ex.: db.t3.micro para teste).
   - **Multi-AZ Deployment**: Ative se precisar de alta disponibilidade.

4. **Configurações de Conectividade**:
   - **VPC**: Selecione a mesma VPC da instância EC2.
   - **Sub-redes**: Escolha sub-redes privadas para o banco de dados.
   - **Public Access**: Desative para um ambiente de produção, habilite apenas para desenvolvimento com restrições de segurança.

5. **Configurações de Autenticação e Backup**:
   - Configure backups automáticos e defina as políticas de retenção e manutenção.

6. **Criação da Instância**:
   - Clique em **"Create Database"** para finalizar.

### **5. Criando e Configurando Security Groups**

#### **5.1. Criando um Security Group para a Instância EC2**

1. **Acessar o Console EC2**:
   - Navegue até **Security Groups** e clique em **"Create Security Group"**.

2. **Configurar o Security Group**:
   - **Nome**: Nomeie seu grupo (ex.: SG-EC2-API).
   - **Descrição**: Descreva a função (ex.: Security Group para instância EC2 da API).
   - **Regras de Entrada**:
     - **SSH (Porta 22)**: Permita o acesso somente do seu IP (para acesso seguro).
     - **HTTP/HTTPS**: Habilite conforme necessário para a aplicação.

#### **5.2. Criando um Security Group para o Banco de Dados RDS**

1. **Acessar o Console RDS**:
   - No painel do RDS, acesse **Security Groups** e clique em **"Create Security Group"**.

2. **Configurar o Security Group do RDS**:
   - **Nome**: Nomeie seu grupo (ex.: SG-RDS-Database).
   - **Regras de Entrada**:
     - **Banco de Dados (Porta 5432 para PostgreSQL, ou outra conforme o banco)**.
     - **Origem**: Especifique o Security Group da instância EC2 (ex.: SG-EC2-API) para garantir que apenas a instância EC2 possa se conectar ao banco.

### **6. Vantagens e Oportunidades da Integração EC2 + RDS para Engenharia de Dados**

1. **Desempenho e Escalabilidade**: A combinação EC2 e RDS permite processar grandes volumes de dados e escalar conforme a demanda, ideal para pipelines de dados e processamento intensivo.

2. **Facilidade de Manutenção**: Com o RDS gerenciado, as tarefas complexas de manutenção do banco de dados, como backups e patches, são automatizadas, liberando os engenheiros para focar em otimizações de processamento.

3. **Segurança e Controle de Acesso**: A configuração de Security Groups restritivos garante que o tráfego de dados entre a aplicação e o banco seja seguro, minimizando riscos de acesso não autorizado.

4. **Implementação Ágil de Projetos de Dados**: Essa arquitetura facilita a rápida implementação de APIs que coletam, processam e armazenam dados, otimizando fluxos de trabalho de ETL (Extração, Transformação e Carga) com acesso seguro ao banco de dados.

5. **Monitoramento e Otimização**: Utilizando ferramentas da AWS como CloudWatch, é possível monitorar métricas críticas de desempenho tanto da instância EC2 quanto do RDS, ajustando conforme necessário para garantir alta performance.

### **Conclusão**

Nesta aula, aprendemos como configurar e integrar uma instância EC2 com o Amazon RDS, criando uma arquitetura robusta para aplicações que processam requisições de APIs e armazenam dados de forma eficiente e segura. Essa integração é um pilar essencial para qualquer projeto de engenharia de dados, permitindo que você construa soluções escaláveis e de alto desempenho na nuvem.