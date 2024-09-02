# **Bootcamp Cloud: Aula 07: Gerenciando Bancos de Dados na Amazon com RDS**

**Objetivo**: Nesta aula, vamos explorar o Amazon RDS (Relational Database Service), entender suas principais funcionalidades, tipos de bancos de dados suportados, e aprender a configurar, gerenciar e otimizar bancos de dados na AWS.

### **1. O Que é o Amazon RDS?**

- **Definição**: O Amazon RDS é um serviço gerenciado de banco de dados relacional na nuvem que facilita a configuração, operação e escalabilidade de bancos de dados relacionais. Ele oferece suporte para diversos mecanismos de banco de dados, como MySQL, PostgreSQL, MariaDB, Oracle, SQL Server e Amazon Aurora.

- **Benefícios**:
  - **Automação de Tarefas**: Automatiza tarefas como backups, atualizações de software, e recuperação de falhas.
  - **Escalabilidade**: Permite ajustar a capacidade de acordo com a demanda de maneira rápida e fácil, sem precisar de grandes investimentos em hardware.
  - **Segurança**: Suporte para encriptação de dados em repouso e em trânsito, além de controles de acesso granulares.
  - **Alta Disponibilidade**: Oferece replicação multi-AZ (Availability Zones) para garantir alta disponibilidade e durabilidade.

### **2. Principais Funcionalidades do Amazon RDS**

#### **Multi-AZ Deployment**

- **O que é?**: Uma configuração que permite implantar instâncias de banco de dados em múltiplas zonas de disponibilidade, proporcionando alta disponibilidade e tolerância a falhas.
- **Benefícios**:
  - **Failover Automático**: Se a instância primária falhar, o RDS promove automaticamente uma réplica para minimizar o tempo de inatividade.
  - **Melhor Desempenho de Leitura e Escrita**: Separação de leituras e escritas entre instâncias primárias e réplicas.

#### **Read Replicas**

- **O que são?**: Réplicas de leitura permitem replicar dados de uma instância RDS para melhorar a performance de leitura.
- **Uso Comum**:
  - **Escalabilidade de Leitura**: Descarrega o tráfego de leitura da instância primária.
  - **Disaster Recovery**: Pode ser usada para recuperar dados rapidamente em caso de falhas.

#### **Backup e Restore Automático**

- **Backup Automático**: Realiza backups automáticos dos dados e dos logs de transações.
- **Snapshots Manuais**: Permitem capturar o estado do banco de dados a qualquer momento.
- **Restore Point-in-Time**: Restaurar o banco de dados para um ponto específico no tempo com precisão.

#### **Segurança no Amazon RDS**

- **Encryption**: Criptografa dados em repouso e em trânsito, utilizando chaves gerenciadas pelo AWS KMS (Key Management Service).
- **Controle de Acesso**: Usando VPC Security Groups, IAM Roles e políticas para restringir o acesso ao banco de dados.
- **Monitoramento**: CloudWatch e Event Subscriptions para monitorar métricas e receber alertas sobre o status do banco de dados.

### **3. Configurando o Amazon RDS: Passo a Passo**

#### **1. Criando uma Instância de Banco de Dados no RDS**

1. **Acessar o Console do RDS**:
   - Faça login no console da AWS e navegue até o serviço **RDS (Relational Database Service)**.
   - Clique em **"Create Database"** para iniciar o processo de configuração.

2. **Escolher o Motor de Banco de Dados**:
   - Selecione o mecanismo de banco de dados desejado (MySQL, PostgreSQL, etc.).
   - Escolha a versão do mecanismo com base nas necessidades de compatibilidade e recursos.

3. **Configuração da Instância**:
   - **Tipo de Instância**: Escolha o tipo de instância que atende à sua carga de trabalho (db.t3.micro para testes ou db.m5.large para produção).
   - **Multi-AZ Deployment**: Ative se desejar alta disponibilidade.

4. **Configuração de Armazenamento**:
   - **Tipo de Armazenamento**: Escolha entre armazenamento SSD padrão, provisionado ou magnético.
   - **Auto Scaling de Armazenamento**: Ative para permitir que o RDS ajuste automaticamente o armazenamento conforme necessário.

5. **Configuração de Conectividade**:
   - **VPC**: Selecione a VPC onde a instância será criada.
   - **Sub-redes**: Escolha as sub-redes dentro da VPC (pública ou privada).
   - **Grupos de Segurança**: Configure Security Groups para controlar o acesso de entrada e saída.

6. **Configuração de Autenticação e Backup**:
   - **Autenticação IAM**: Opcional, para usar credenciais IAM para conectar ao banco de dados.
   - **Backup Automático**: Configure a retenção de backups automáticos e os horários de backup.

7. **Criação da Instância**:
   - Clique em **"Create Database"** para finalizar a criação da instância.

#### **2. Gerenciando Backups e Restaurações**

- **Configurar Backups Automáticos**:
  - Defina o período de retenção dos backups e o horário preferido para realização.
- **Snapshots Manuais**:
  - Faça snapshots manuais antes de realizar mudanças críticas no banco de dados.
- **Restauração**:
  - Utilize a funcionalidade de **Restore to Point in Time** para restaurar o banco a um estado anterior.

#### **3. Monitoramento e Escalabilidade**

- **CloudWatch Metrics**:
  - Monitore o uso de CPU, memória, IOPS, e outras métricas críticas através do CloudWatch.
- **Auto Scaling**:
  - Configure para ajustar automaticamente a capacidade da instância com base na demanda.

### **4. Melhores Práticas ao Utilizar o Amazon RDS**

- **Isolamento de Sub-redes Privadas**: Sempre que possível, implante bancos de dados em sub-redes privadas para evitar a exposição direta à internet.
- **Regras de Segurança e Autenticação**: Use Security Groups restritivos e a autenticação IAM para aumentar a segurança.
- **Multi-AZ e Read Replicas**: Utilize Multi-AZ para alta disponibilidade e Read Replicas para escalar leituras.
- **Testes de Backup e Restauração**: Realize testes periódicos de restauração para garantir que seus backups funcionam conforme o esperado.
- **Monitoramento e Alertas**: Configure alertas para monitorar o desempenho e a integridade do banco de dados.

### **5. Projeto Prático: Criando e Gerenciando um Banco de Dados com Amazon RDS**

**Objetivo do Projeto**: Criar uma instância RDS para um ambiente de produção, configurando backups, segurança e escalabilidade.

**Passo a Passo Resumido**:

1. **Criar a Instância RDS**:
   - Escolha o tipo de banco de dados e configure conforme as necessidades da aplicação.
2. **Configurar Multi-AZ e Read Replicas**:
   - Implemente uma configuração Multi-AZ para alta disponibilidade e uma Read Replica para melhorar o desempenho de leitura.
3. **Aplicar Regras de Segurança**:
   - Use Security Groups para restringir o acesso ao banco de dados, garantindo que apenas instâncias autorizadas possam conectar-se.
4. **Monitorar e Ajustar a Instância**:
   - Utilize o CloudWatch para monitorar métricas de desempenho e ajuste a instância conforme necessário.
5. **Testar Backup e Restauração**:
   - Realize testes para garantir que o processo de backup e restauração está funcionando corretamente.

Essa aula oferece uma visão abrangente sobre o gerenciamento de bancos de dados na AWS com o Amazon RDS, capacitando você a configurar, proteger e escalar seus bancos de dados na nuvem.

### **6. Criando uma VPC do Zero e Configurando o RDS em uma Rede Pública**

Para configurar o Amazon RDS em uma rede pública, vamos criar uma VPC do zero, configurar suas sub-redes, habilitar DNS, e então criar uma instância de banco de dados RDS. Essa configuração é especialmente útil para fins de desenvolvimento ou teste, onde o acesso público ao banco de dados é necessário. 

#### **Passo a Passo para Criar uma VPC com RDS**

**1. Criando a VPC e Sub-rede Pública**

1. **Acessar o Console VPC**:
   - Acesse o console da AWS e navegue até o serviço **VPC**.
   - Clique em **"Create VPC"**.

2. **Configurar a VPC**:
   - **Nome**: Dê um nome à sua VPC, por exemplo, "MinhaVPC-RDS".
   - **CIDR Block**: Defina um bloco CIDR, como "10.0.0.0/16", para o intervalo de endereços IP.
   - **Habilitar DNS**: Marque as opções para habilitar DNS hostnames e DNS resolution para garantir que as instâncias dentro da VPC possam resolver nomes de DNS.
   - Clique em **"Create VPC"** para finalizar a criação.

3. **Criar uma Sub-rede Pública**:
   - No painel VPC, selecione **"Subnets"** e clique em **"Create Subnet"**.
   - **Nome**: "MinhaSubnetPublica".
   - **VPC**: Selecione a VPC recém-criada ("MinhaVPC-RDS").
   - **CIDR Block**: Defina um bloco CIDR, como "10.0.1.0/24".
   - **Availability Zone**: Escolha uma zona de disponibilidade para a sub-rede.
   - Clique em **"Create Subnet"**.

4. **Configurar o Gateway de Internet**:
   - No painel VPC, clique em **"Internet Gateways"** e depois em **"Create Internet Gateway"**.
   - **Nome**: "MeuInternetGateway".
   - Clique em **"Create"**, depois associe o gateway à VPC ("MinhaVPC-RDS") clicando em **"Attach to VPC"**.

5. **Configurar a Tabela de Roteamento**:
   - Vá para **"Route Tables"** e selecione a tabela associada à sua VPC.
   - **Adicionar Rota**: Clique em **"Edit Routes"**, adicione uma rota para "0.0.0.0/0" e selecione o Internet Gateway criado anteriormente.
   - **Associar à Sub-rede Pública**: Vá para **"Subnet Associations"** e associe a tabela à "MinhaSubnetPublica".

**2. Criando o RDS na Rede Pública**

1. **Acessar o Console do RDS**:
   - Navegue para o serviço **RDS** no console da AWS e clique em **"Create Database"**.

2. **Escolher o Motor de Banco de Dados**:
   - Selecione o mecanismo **MySQL** ou outro que desejar.
   - Escolha a versão mais recente que suporte o **Free Tier**.

3. **Configurações da Instância**:
   - **Tipo de Instância**: Escolha **t4g.micro** (Free Tier).
   - **Multi-AZ Deployment**: Desative para um ambiente de teste ou desenvolvimento.
   - **Master Username**: Defina o usuário mestre, por exemplo, "admin".
   - **Master Password**: Crie uma senha segura para o administrador.

4. **Configuração de Conectividade**:
   - **VPC**: Selecione "MinhaVPC-RDS".
   - **Sub-rede Pública**: Escolha a sub-rede pública criada anteriormente.
   - **Public Access**: Ative para permitir que o RDS seja acessado publicamente (para ambientes de teste).
   - **Security Group**: Configure para permitir acesso ao banco (por exemplo, na porta 3306 para MySQL).

5. **Configuração de Backup**:
   - **Backup Retention Period**: Defina o período de retenção de backups automáticos, que pode variar de 1 a 35 dias.
   - **Backup Window**: Escolha um horário de manutenção para os backups automáticos; isso deve ser durante um período de menor carga.

6. **Criar o Banco de Dados**:
   - Revise as configurações e clique em **"Create Database"**. O processo de criação pode levar alguns minutos.

**3. Detalhes de Criação e Configuração do Amazon RDS**

- **Tipos de Armazenamento**:
  - **General Purpose SSD (gp2)**: Para a maioria dos usos comuns, com desempenho balanceado.
  - **Provisioned IOPS (io1)**: Para cargas de trabalho de I/O intensivo, como grandes aplicações OLTP.
  - **Magnetic Storage**: Armazenamento mais econômico, mas menos performático.

- **Opções de Backup**:
  - **Backup Automático**: Realiza backups completos diariamente e backups incrementais dos logs de transações.
  - **Snapshots Manuais**: Criação manual de snapshots para capturar o estado atual do banco de dados.
  - **Point-in-Time Restore**: Permite restaurar o banco de dados para um ponto específico no tempo.

- **Segurança**:
  - **IAM Authentication**: Autenticação de usuários via IAM, para controle mais granular.
  - **VPC Security Groups**: Controle de acesso baseado em IPs e portas, para proteger o banco de dados.

- **Janela de Manutenção**:
  - **Configuração de Manutenção**: Escolha um período de manutenção para realizar updates de software que afetam a instância, garantindo o mínimo de interrupções possíveis.

### **Conclusão**

Essa abordagem de criar uma VPC pública para configurar um RDS permite que você gerencie e acesse seu banco de dados com facilidade, mantendo um nível básico de segurança e controle. Para ambientes de produção, recomenda-se uma configuração mais restritiva, como o uso de sub-redes privadas e a desativação do acesso público direto ao RDS.

Entendido! Vamos configurar o WordPress na instância EC2 usando o AWS Systems Manager Session Manager (AWS Connect) para acesso, sem a necessidade de chaves PEM. Segue o passo a passo completo:

### **Passo a Passo Completo: Instalando o WordPress em uma Instância EC2 Usando Amazon RDS**

#### **1. Preparando o Ambiente na AWS**

**1.1 Criar a VPC e Configurar Rede**

1. **Acessar o Console VPC**:
   - No console da AWS, navegue até **VPC** e clique em **"Create VPC"**.

2. **Configurar a VPC**:
   - **Nome**: "MinhaVPC-WordPress".
   - **CIDR Block**: "10.0.0.0/16".
   - Habilitar DNS hostnames e DNS resolution.
   - Clique em **"Create VPC"**.

3. **Criar Sub-rede Pública**:
   - No painel VPC, selecione **"Subnets"** e clique em **"Create Subnet"**.
   - **Nome**: "MinhaSubnetPublica".
   - **VPC**: Selecione "MinhaVPC-WordPress".
   - **CIDR Block**: "10.0.1.0/24".
   - Escolha uma zona de disponibilidade (ex: us-east-1a).
   - Clique em **"Create Subnet"**.

4. **Configurar o Gateway de Internet**:
   - No painel VPC, clique em **"Internet Gateways"** e em **"Create Internet Gateway"**.
   - **Nome**: "MeuInternetGateway".
   - Clique em **"Create"**, depois associe o gateway à VPC criada clicando em **"Attach to VPC"**.

5. **Configurar a Tabela de Roteamento**:
   - Vá para **"Route Tables"**, selecione a tabela associada à VPC.
   - Clique em **"Edit Routes"** > **"Add route"**, adicione "0.0.0.0/0" e selecione o Internet Gateway.
   - Associe a tabela à sub-rede pública criada.

#### **2. Criar a Instância do Banco de Dados com Amazon RDS**

1. **Acessar o Console do RDS**:
   - Navegue até **RDS** e clique em **"Create Database"**.

2. **Configurar o Banco de Dados**:
   - **Engine**: Selecione **MySQL**.
   - **Version**: Escolha uma versão compatível com WordPress.
   - **Template**: Escolha **Free Tier** se aplicável.
   - **DB Instance Class**: Selecione **db.t4g.micro** (Free Tier).
   - **Multi-AZ**: Desative para ambientes de teste.

3. **Configurações de Identificação e Autenticação**:
   - **DB Instance Identifier**: Nome da instância, ex: "WordPressDB".
   - **Master Username**: "admin".
   - **Master Password**: Defina uma senha segura.

4. **Configurações de Conectividade**:
   - **VPC**: Selecione "MinhaVPC-WordPress".
   - **Subnets**: Escolha a sub-rede pública.
   - **Public Access**: Ative para permitir conexão da instância EC2.
   - **Security Group**: Crie ou selecione um grupo que permita acesso na porta 3306 (MySQL).

5. **Backup e Manutenção**:
   - Configure backups automáticos e defina a janela de manutenção para horários de baixa demanda.

6. **Criar o Banco de Dados**:
   - Revise as configurações e clique em **"Create Database"**.

#### **3. Criar Instância EC2 para Hospedar o WordPress**

**3.1 Criar a Instância EC2**

1. **Acessar o Console EC2**:
   - Vá para **EC2** e clique em **"Launch Instance"**.

2. **Escolher o Sistema Operacional**:
   - Escolha uma Amazon Machine Image (AMI) como **Amazon Linux 2**.

3. **Configurar a Instância**:
   - **Instance Type**: Escolha **t2.micro** (Free Tier).
   - **VPC**: Selecione "MinhaVPC-WordPress".
   - **Subnet**: Escolha "MinhaSubnetPublica".

4. **Configurar o Security Group**:
   - Crie um novo Security Group ou selecione um existente que permita acesso HTTP (porta 80) e HTTPS (porta 443).

5. **Configurar o Acesso via AWS Systems Manager**:
   - Em **Advanced Details**, habilite a opção **Enable AWS Systems Manager** para permitir acesso à instância sem usar chaves SSH.

6. **Lançar a Instância**:
   - Clique em **"Launch"** para iniciar a instância EC2.

**3.2 Configurar o Servidor Web com WordPress**

1. **Conectar à Instância EC2 via AWS Systems Manager**:
   - Acesse o AWS Systems Manager > Session Manager.
   - Selecione a instância EC2 e clique em **"Start session"**.

2. **Assumir o Usuário Root**:

   ```bash
   sudo -s
   ```

3. **Instalar os Pacotes Necessários**:

   ```bash
   yum -y update all
   amazon-linux-extras enable php8.0
   yum -y clean metadata
   yum -y install httpd php php-gd php-mysqlnd
   ```

4. **Iniciar o Servidor Apache**:

   ```bash
   systemctl start httpd
   systemctl enable httpd
   ```

5. **Baixar e Configurar o WordPress**:

   ```bash
   wget https://wordpress.org/latest.tar.gz
   tar -xzf latest.tar.gz
   ```

6. **Mover os Arquivos do WordPress**:

   ```bash
   cp wordpress/wp-config-sample.php wordpress/wp-config.php
   cp -r wordpress/* /var/www/html/
   ```

7. **Configurar o WordPress para Conectar ao RDS**:

   ```bash
   vi /var/www/html/wp-config.php
   ```

   - Edite as seguintes linhas para refletir as credenciais do banco de dados RDS:

   ```php
   define('DB_NAME', 'wordpressdb'); 
   define('DB_USER', 'admin'); 
   define('DB_PASSWORD', 'sua_senha_do_rds'); 
   define('DB_HOST', 'endpoint_do_rds'); 
   ```

8. **Configurar Permissões**:

   ```bash
   sudo chown -R apache /var/www
   sudo chgrp -R apache /var/www
   sudo chmod 2775 /var/www
   find /var/www -type d -exec sudo chmod 2775 {} \;
   find /var/www -type f -exec sudo chmod 0644 {} \;
   ```

9. **Reiniciar o Apache**:

   ```bash
   systemctl restart httpd
   ```

#### **4. Finalizando a Configuração do WordPress**

1. **Verificar o Acesso ao WordPress**:
   - Abra um navegador e vá para o IP público da instância EC2 (http://seu-ip-publico).
   - Siga o assistente de instalação do WordPress para definir o nome do site, usuário e senha de administrador.

2. **Testar o Acesso e Conectividade**:
   - Verifique o acesso interno e externo:

   ```bash
   curl localhost
   curl http://instance-data/latest/meta-data/public-ipv4
   curl $(curl http://instance-data/latest/meta-data/public-ipv4)
   ```

### **Conclusão**

Seguindo este passo a passo, você terá um WordPress totalmente funcional na AWS usando uma instância EC2 para a aplicação e o Amazon RDS para o banco de dados. Esta configuração proporciona escalabilidade, melhor desempenho e separação clara entre a camada de aplicação e o banco de dados. Para produção, considere adicionar camadas de segurança adicionais, como o uso de sub-redes privadas para o RDS, SSL para conexões seguras e otimizações de performance.