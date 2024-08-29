# **Bootcamp Cloud: Aula 05: VPC na AWS**

**Objetivo**: Nesta aula, vamos explorar o conceito de VPC (Virtual Private Cloud) na AWS, entender seus componentes principais, como sub-redes públicas e privadas, gateways de internet, endpoints de VPC, e aprender a configurar e utilizar esses elementos para criar uma infraestrutura de rede segura e eficiente na nuvem.

### **1. O Que é VPC?**

- **Definição**: A VPC (Virtual Private Cloud) é um serviço da AWS que permite criar uma rede privada virtual dentro da nuvem. Com a VPC, você tem controle total sobre o seu ambiente de rede, incluindo a escolha de seu próprio intervalo de endereços IP, a criação de sub-redes e a configuração de tabelas de roteamento e gateways de internet.
  
- **Benefícios**:
  - **Isolamento de Rede**: Mantém seus recursos isolados de outros clientes da AWS.
  - **Controle de Segurança**: Permite definir regras de segurança detalhadas para proteger seus recursos.
  - **Flexibilidade de Configuração**: Oferece a possibilidade de personalizar a configuração de sua rede, como endereçamento IP, gateways, e roteamento.

### **2. Componentes Principais de uma VPC**

#### **Sub-redes (Subnets)**

**O que são Sub-redes?**
- As sub-redes são divisões dentro de uma VPC que permitem segmentar e organizar recursos. Cada sub-rede é associada a uma parte do intervalo de endereços IP da VPC e reside em uma única Zona de Disponibilidade (AZ).

**Tipos de Sub-redes:**
- **Sub-redes Públicas**: São sub-redes conectadas a um Gateway de Internet (Internet Gateway), permitindo que recursos dentro delas tenham acesso direto à internet. Ideal para recursos que precisam ser acessíveis externamente, como servidores web.
- **Sub-redes Privadas**: São sub-redes que não possuem acesso direto à internet. Elas são usadas para recursos que devem ser isolados do acesso público, como bancos de dados. O acesso à internet a partir dessas sub-redes é feito por meio de um NAT Gateway, que roteia o tráfego de saída de forma segura.

#### **Sub-redes Públicas (Public Subnets)**

- **Definição**: Sub-redes públicas são configuradas para que os recursos nelas alocados possam se comunicar diretamente com a internet. Isso é feito associando a sub-rede a um Gateway de Internet (IGW).
  
- **Uso Comum**:
  - **Servidores Web**: Servidores que precisam estar acessíveis ao público, como servidores web, geralmente são colocados em sub-redes públicas. Isso permite que eles recebam tráfego de entrada diretamente da internet.
  - **Recursos que Necessitam de Acesso Direto à Internet**: Recursos como proxies, gateways, ou load balancers que devem receber ou enviar dados diretamente pela internet também são colocados em sub-redes públicas.

- **Regras de Segurança**:
  - **Security Groups**: Devem ser configurados para permitir tráfego apenas nas portas e protocolos necessários (por exemplo, HTTP na porta 80 ou HTTPS na porta 443).

#### **Sub-redes Privadas (Private Subnets)**

- **Definição**: Sub-redes privadas são aquelas que não têm acesso direto à internet. Elas são usadas para hospedar recursos que devem ser protegidos de acessos externos diretos, como bancos de dados ou servidores de backend. O tráfego de saída para a internet a partir dessas sub-redes é feito usando um NAT Gateway.

- **Uso Comum**:
  - **Bancos de Dados e Servidores de Aplicação**: Servidores que armazenam dados críticos, como bancos de dados, ou que executam lógica de aplicação sensível, são colocados em sub-redes privadas para proteger contra acessos diretos da internet.
  - **Recursos Backend**: Qualquer recurso que não precisa de acesso direto da internet, mas pode precisar se conectar a outros serviços da AWS ou realizar atualizações de software pela internet.

- **Acesso à Internet através de NAT**:
  - **NAT Gateway**: Para permitir que recursos em sub-redes privadas acessem a internet de forma segura (por exemplo, para baixar atualizações ou acessar APIs), utilizamos um NAT Gateway. O NAT roteia o tráfego de saída das instâncias privadas para a internet, sem expor esses recursos diretamente.

Um **NAT Gateway** (Network Address Translation Gateway) é um serviço na AWS que permite que instâncias em uma sub-rede privada façam solicitações de saída para a internet (como downloads ou atualizações de software) sem estarem diretamente acessíveis de fora da VPC. Vamos entender melhor o papel do NAT Gateway e a vantagem de usá-lo, mesmo com o custo associado.

### **O Que é um NAT Gateway?**
- **NAT Gateway** é um recurso gerenciado da AWS que permite que instâncias em sub-redes privadas tenham acesso de saída à internet (como para downloads ou atualizações), enquanto impede conexões de entrada não solicitadas vindas da internet.
- Funciona traduzindo endereços IP privados (da sub-rede privada) em um endereço IP público (associado ao NAT Gateway) para todo o tráfego de saída, e vice-versa para o tráfego de resposta.

### **Vantagem de Usar um NAT Gateway em uma Sub-rede Privada**

1. **Segurança Aprimorada:**
   - **Controle de Acesso:** Quando você coloca uma instância em uma sub-rede privada e usa um NAT Gateway, a instância não é acessível diretamente pela internet. Isso significa que ninguém pode iniciar uma conexão diretamente com a instância, reduzindo a superfície de ataque.
   - **Isolamento da Rede:** Instâncias em sub-redes privadas são protegidas por não serem visíveis diretamente na internet. O NAT Gateway permite que apenas tráfego de saída seja permitido, não o de entrada não solicitado.

2. **Limitação de Acesso Direto:**
   - **Acesso Controlado:** As instâncias privadas que precisam de conectividade de saída (por exemplo, para acessar atualizações de software, bibliotecas, ou APIs externas) ainda podem fazê-lo sem ficarem diretamente expostas à internet. Isso oferece um equilíbrio entre segurança e funcionalidade.
   - **Prevenção de Ataques:** Como as instâncias em sub-redes privadas não têm IPs públicos, elas não são diretamente atacáveis por scans de portas, ataques de DDoS, ou tentativas de invasão que podem ser direcionadas a IPs públicos.

3. **Compliance e Conformidade:**
   - **Requisitos de Segurança:** Algumas regulamentações de segurança e conformidade (como PCI-DSS, HIPAA, etc.) exigem que servidores de dados críticos (como bancos de dados) sejam isolados e não tenham exposição direta à internet. Usar sub-redes privadas com NAT Gateway cumpre esses requisitos.

### **Por que Não Colocar a Sub-rede Direto como Pública?**

Se você coloca suas instâncias diretamente em uma **sub-rede pública**:
- **Exposição Direta à Internet:** Cada instância em uma sub-rede pública pode receber tráfego de entrada direto da internet. Mesmo que você configure regras de firewall e segurança (Security Groups e NACLs), a instância ainda estará visível e pode ser alvo de ataques.
- **Necessidade de Endereços IP Públicos:** Cada instância precisaria de um IP público, aumentando o custo e o risco de segurança.
- **Superfície de Ataque Maior:** Com a exposição direta, a chance de ataques, como scans de portas ou ataques de DDoS, aumenta significativamente.

Vamos esclarecer os conceitos de **entrada (inbound)** e **saída (outbound)** no contexto de redes e comunicação na internet, bem como entender como isso se aplica a uma infraestrutura na nuvem, como a AWS.

### **Diferença entre Entrada (Inbound) e Saída (Outbound)**

1. **Tráfego de Entrada (Inbound Traffic):**
   - **Definição:** Tráfego de entrada refere-se a todas as conexões e dados que vêm de fora da rede e estão entrando em seus recursos, como instâncias de servidores ou dispositivos.
   - **Exemplos:**
     - Um usuário acessando um site hospedado em um servidor web na AWS.
     - Requisições de API enviadas para um serviço hospedado na sua VPC.
     - Conexões SSH de um administrador tentando acessar remotamente um servidor.

2. **Tráfego de Saída (Outbound Traffic):**
   - **Definição:** Tráfego de saída refere-se a todas as conexões e dados que estão saindo de seus recursos e indo para fora da rede, como para a internet ou outras redes.
   - **Exemplos:**
     - Um servidor em sua sub-rede privada baixando atualizações de software da internet.
     - Envio de dados para um serviço externo, como uma API de terceiros.
     - Conexões de um banco de dados na sua VPC para outro banco de dados em uma rede externa.

### **Como Funciona o NAT Gateway no Contexto de Saída e Entrada?**

Um **NAT Gateway** permite que o tráfego de saída (outbound) de instâncias em uma sub-rede privada alcance a internet sem permitir o tráfego de entrada (inbound) direto da internet para essas instâncias. Vamos ver como isso se aplica a ambos os tipos de tráfego:

- **Tráfego de Saída (Outbound) com NAT Gateway:**
  - **Exemplo de Funcionamento:**
    - Instâncias em uma sub-rede privada que não têm endereços IP públicos enviam solicitações para a internet (como atualizações de software ou chamadas para APIs).
    - O NAT Gateway, localizado em uma sub-rede pública, recebe essas solicitações, traduz os endereços IP privados para o IP público do NAT Gateway e encaminha o tráfego para a internet.
    - Quando a resposta chega, o NAT Gateway traduz de volta para os endereços IP privados e entrega a resposta às instâncias na sub-rede privada.

- **Tráfego de Entrada (Inbound) com NAT Gateway:**
  - **Exemplo de Restrição:**
    - Um NAT Gateway **não** permite conexões de entrada iniciadas da internet para as instâncias na sub-rede privada. Ele bloqueia automaticamente qualquer tentativa de conexão iniciada externamente, garantindo que apenas o tráfego de saída e suas respectivas respostas sejam permitidos.

### **Por que a Distinção é Importante?**

- **Segurança:**
  - Separar o tráfego de entrada e saída é uma prática importante para segurança. Tráfego de entrada direto da internet representa um risco de segurança, pois expõe seus recursos a ataques externos, como tentativas de invasão, DDoS, etc.
  - Tráfego de saída é necessário para muitas operações, como atualizações de software e chamadas de API. No entanto, ele não deve expor diretamente os recursos a ataques de entrada.

- **Uso de NAT Gateway:**
  - Usar um **NAT Gateway** permite que recursos em sub-redes privadas tenham conectividade de saída segura com a internet, sem expô-los a tráfego de entrada desnecessário. Isso protege seus recursos enquanto ainda permite que realizem operações necessárias.

### **Outbound e Inbound: Exemplos Comuns na AWS**

1. **Instância EC2 Pública:**
   - **Inbound:** Pode receber conexões de entrada diretamente da internet (por exemplo, um servidor web recebendo requisições HTTP).
   - **Outbound:** Pode enviar tráfego para a internet (por exemplo, fazer solicitações de saída a uma API externa).

2. **Instância EC2 Privada com NAT Gateway:**
   - **Inbound:** Não pode receber conexões de entrada diretamente da internet (somente resposta a requisições de saída previamente iniciadas).
   - **Outbound:** Pode enviar tráfego de saída para a internet através do NAT Gateway (por exemplo, baixar pacotes de atualização).

### **Conclusão: Diferença entre Entrada e Saída**

- **Entrada (Inbound):** Conexões iniciadas de fora da rede em direção aos seus recursos.
- **Saída (Outbound):** Conexões iniciadas pelos seus recursos em direção a fora da rede.
- **NAT Gateway:** Facilita conexões de saída para recursos em sub-redes privadas, mantendo-os protegidos de conexões de entrada diretas, garantindo um ambiente mais seguro e controlado.

### **Quando Usar um NAT Gateway?**

Use um **NAT Gateway** quando:
- Você precisa que instâncias em sub-redes privadas tenham acesso de saída à internet, mas sem serem diretamente acessíveis de fora da VPC.
- A segurança é uma prioridade e você quer minimizar a exposição dos seus recursos à internet.
- Você quer aproveitar a solução gerenciada da AWS, que oferece alta disponibilidade e manutenção automática.

### **Diferença entre NAT Gateway e VPC Endpoint**

Antes de detalhar onde usar um **NAT Gateway** em vez de um **VPC Endpoint**, vamos esclarecer o que cada um desses recursos faz:

- **NAT Gateway**: Permite que instâncias em sub-redes privadas tenham acesso de saída à internet sem permitir conexões de entrada da internet. Ideal para casos em que os recursos na sub-rede privada precisam se comunicar com serviços fora da VPC (como APIs de terceiros ou atualizações de software).

- **VPC Endpoint**: Permite que sua VPC se conecte diretamente a determinados serviços da AWS (como S3 ou DynamoDB) sem passar pela internet pública. Ideal para quando você deseja acessar serviços da AWS de forma segura e sem exposição à internet.

### **Quando Usar NAT Gateway ao Invés de VPC Endpoint?**

Use o **NAT Gateway** em vez de um **VPC Endpoint** quando:

1. **Conectar a Recursos Fora da AWS:**
   - Se seus recursos em sub-redes privadas precisam se comunicar com serviços ou recursos fora da AWS, como APIs de terceiros, sites para atualizações de software, ou servidores externos.
   - **Exemplo:** Sua instância EC2 em uma sub-rede privada precisa baixar pacotes de software ou atualizações diretamente da internet. Nesse caso, um NAT Gateway permitirá que essa instância tenha acesso de saída sem estar diretamente exposta à internet para conexões de entrada.

2. **Acesso Genérico à Internet:**
   - Quando você precisa de acesso geral à internet para vários propósitos e não está limitado a serviços específicos da AWS.
   - **Exemplo:** Um servidor de banco de dados em uma sub-rede privada que precisa se conectar a um repositório de pacotes para baixar atualizações ou enviar logs para um serviço de monitoramento externo.

3. **Acessar Serviços Não Suportados por VPC Endpoints:**
   - VPC Endpoints atualmente suportam apenas um subconjunto de serviços da AWS (por exemplo, S3, DynamoDB). Se você precisa acessar serviços ou destinos que não são cobertos por VPC Endpoints, você precisará usar um NAT Gateway.
   - **Exemplo:** Conectar-se a um serviço da AWS que não possui um VPC Endpoint específico (como algumas APIs menos comuns ou serviços regionais específicos).

### **Quando Usar VPC Endpoint ao Invés de NAT Gateway?**

Use um **VPC Endpoint** em vez de um **NAT Gateway** quando:

1. **Conectar-se a Serviços da AWS de Forma Segura:**
   - Quando você deseja que sua VPC se conecte diretamente a serviços da AWS (como S3 ou DynamoDB) sem passar pela internet pública. Isso proporciona mais segurança e pode reduzir a latência.
   - **Exemplo:** Um aplicativo em uma instância EC2 em uma sub-rede privada precisa acessar um bucket S3 para armazenar ou recuperar arquivos de dados. Um VPC Endpoint para S3 permitirá essa comunicação sem passar pela internet.

2. **Reduzir Custos:**
   - VPC Endpoints geralmente são mais baratos do que usar um NAT Gateway porque não há cobrança por dados de saída através de um endpoint, enquanto o NAT Gateway cobra por dados transferidos.
   - **Exemplo:** Transferir grandes volumes de dados entre sua VPC e o S3. Um VPC Endpoint para S3 pode reduzir significativamente os custos de transferência de dados em comparação ao uso de um NAT Gateway.

3. **Compliance e Conformidade:**
   - Se suas políticas de segurança exigem que todo o tráfego permaneça dentro da rede da AWS sem passar pela internet pública, usar VPC Endpoints é ideal.
   - **Exemplo:** Organizações que precisam estar em conformidade com regulamentações como PCI-DSS, HIPAA, ou outras normas que exigem controle estrito de onde os dados trafegam.

### **Resumo da Escolha: NAT Gateway vs. VPC Endpoint**

| **Cenário**                                         | **Usar NAT Gateway**                                 | **Usar VPC Endpoint**                                |
|-----------------------------------------------------|------------------------------------------------------|------------------------------------------------------|
| **Conectar a recursos fora da AWS**                 | Sim                                                  | Não                                                  |
| **Acesso geral à internet (saída)**                 | Sim                                                  | Não                                                  |
| **Acessar serviços da AWS sem expor à internet**    | Não                                                  | Sim                                                  |
| **Reduzir custos de transferência de dados**        | Não (pode ser caro para grandes volumes)             | Sim                                                  |
| **Conformidade com regulamentações de segurança**   | Não (passa pela internet pública)                    | Sim (tráfego permanece dentro da rede da AWS)        |
| **Acessar serviços da AWS que não possuem Endpoint**| Sim                                                  | Não                                                  |

### **Conclusão**

- **Use NAT Gateway** quando você precisar que recursos em uma sub-rede privada tenham acesso de saída à internet para fins gerais ou para se comunicar com recursos fora da AWS.
- **Use VPC Endpoints** quando você deseja que seus recursos em sub-redes privadas acessem serviços da AWS de maneira segura e econômica, sem expô-los à internet pública.

### **Conclusão**

Embora o NAT Gateway tenha um custo, ele é essencial para garantir que as instâncias em sub-redes privadas possam se comunicar com a internet sem comprometer a segurança. Ele oferece uma solução balanceada entre a necessidade de conectividade de saída e a necessidade de segurança, proteção e conformidade com normas e regulamentações.

#### **Internet Gateway (IGW)**

- **Definição**: Um Internet Gateway (IGW) é um componente que conecta a VPC à internet. Ele permite que recursos em sub-redes públicas possam se comunicar com a internet.

- **Uso**:
  - **Acesso de Entrada e Saída**: O IGW permite que o tráfego entre a internet e os recursos da VPC flua livremente, garantindo que servidores em sub-redes públicas possam receber e enviar tráfego.
  - **Associado a Sub-redes Públicas**: Uma sub-rede é considerada pública quando associada a um Internet Gateway através de uma tabela de roteamento que direciona o tráfego para a internet.

#### **NAT Gateway**

- **Definição**: Um NAT (Network Address Translation) Gateway permite que instâncias em sub-redes privadas acessem a internet para tráfego de saída, sem permitir conexões de entrada vindas da internet.

- **Uso**:
  - **Tráfego de Saída Seguro**: Permite que recursos em sub-redes privadas, como servidores de aplicação ou bancos de dados, façam solicitações de saída para a internet (por exemplo, para atualizações de software), sem expor esses recursos a acessos externos.
  - **Alocação de IP Elástico**: O NAT Gateway é associado a um Elastic IP para gerenciar o tráfego de saída.

#### **VPC Endpoints**

- **Definição**: Um VPC Endpoint permite conectar sua VPC a serviços AWS diretamente, sem passar pela internet pública. Isso fornece uma maneira segura e eficiente de acessar serviços da AWS como S3 ou DynamoDB dentro da VPC.

- **Tipos de VPC Endpoints**:
  - **Gateway Endpoints**: Usados para serviços baseados em S3 e DynamoDB.
  - **Interface Endpoints**: Usados para conectar serviços AWS mais amplamente (como SQS, SNS) diretamente dentro de sua VPC via interfaces de rede privadas (ENIs).

- **Benefícios**:
  - **Segurança**: Todo o tráfego permanece dentro da rede AWS, sem transitar pela internet pública.
  - **Redução de Latência e Custos**: Ao evitar o tráfego pela internet, você reduz a latência e evita custos associados ao uso de largura de banda pública.

### **3. Passo a Passo: Criando uma VPC na AWS**

**Cenário**: Vamos criar uma VPC com uma sub-rede pública e uma privada, configurar um gateway de internet, um NAT Gateway, VPC Endpoints, e aplicar as regras de segurança necessárias.

#### **1. Criar a VPC**

1. **Acessar o Console VPC**:
   - Faça login no console da AWS e navegue até o serviço **VPC (Virtual Private Cloud)**.
   - No painel do VPC, clique em **"Your VPCs"** e depois em **"Create VPC"**.

2. **Configurar a VPC**:
   - **Nome**: Dê um nome à sua VPC, por exemplo, "MinhaVPC".
   - **CIDR Block**: Defina um bloco CIDR, como "10.0.0.0/16", que representa o intervalo de endereços IP que sua VPC utilizará.
   - **Tenancy**: Escolha entre "default" (uso compartilhado) ou "dedicated" (hardware dedicado).

3. **Criar a VPC**:
   - Clique em **"Create VPC"** para finalizar a criação da VPC.

#### **2. Criar Sub-redes**

1. **Criar Sub-rede Pública**:
   - No painel VPC, selecione **"Subnets"** e clique em **"Create Subnet"**.
   - **Nome**: Dê um nome, como "MinhaSubnetPublica".
   - **VPC**: Selecione a VPC criada anteriormente ("MinhaVPC").
   - **CIDR Block**: Defina um bloco CIDR, como "10.0.1.0/24".
   - **Availability Zone**: Escolha uma zona de disponibilidade.

2. **Criar Sub-rede Privada**:
   - Repita o processo para criar uma sub-rede privada.
   - **Nome**: "MinhaSubnetPrivada".
   - **CIDR Block**: "10.0.2.0/24".
   - Esta sub-rede não terá acesso direto à internet.

#### **3. Configurar um Gateway de Internet**

1. **Criar o Gateway de Internet**:
   - No painel VPC, clique em **"Internet Gateways"** e depois em **"Create Internet Gateway"**.
   - **Nome**: "MeuInternetGateway".
   - Clique em **"Create"**.

2. **Associar o Gateway de Internet à VPC**:
   - Selecione o gateway de internet recém-criado.
   - Clique em **"Actions"** e selecione **"Attach to VPC"**.
  

 - Escolha "MinhaVPC" e clique em **"Attach"**.

#### **4. Configurar um NAT Gateway para a Sub-rede Privada**

1. **Criar um NAT Gateway**:
   - No painel VPC, clique em **"NAT Gateways"** e depois em **"Create NAT Gateway"**.
   - **Nome**: "MeuNATGateway".
   - **Sub-rede**: Escolha a "MinhaSubnetPublica" para que o NAT Gateway possa ter acesso ao Internet Gateway.
   - **Elastic IP Allocation**: Clique em "Allocate Elastic IP" para associar um IP Elástico ao NAT Gateway.

2. **Associar o NAT Gateway à Tabela de Roteamento da Sub-rede Privada**:
   - Vá até **"Route Tables"** e selecione a tabela associada à "MinhaSubnetPrivada".
   - Adicione uma rota para o NAT Gateway para tráfego de saída para a internet.

#### **5. Configurar Tabelas de Roteamento**

1. **Criar uma Tabela de Roteamento para Sub-rede Pública**:
   - No painel VPC, clique em **"Route Tables"** e depois em **"Create Route Table"**.
   - **Nome**: "TabelaPublica".
   - **VPC**: Selecione "MinhaVPC".
   - Clique em **"Create"**.

2. **Adicionar uma Rota para o Gateway de Internet**:
   - Selecione a "TabelaPublica" criada.
   - Clique em **"Routes"** > **"Edit routes"** > **"Add route"**.
   - **Destination**: "0.0.0.0/0" (rota padrão para toda a internet).
   - **Target**: Selecione "MeuInternetGateway".
   - Clique em **"Save changes"**.

3. **Associar a Tabela de Roteamento à Sub-rede Pública**:
   - Clique em **"Subnet associations"** > **"Edit subnet associations"**.
   - Selecione "MinhaSubnetPublica".
   - Clique em **"Save associations"**.

#### **6. Configurar VPC Endpoints**

1. **Criar um VPC Endpoint para o S3**:
   - No painel VPC, clique em **"Endpoints"** e depois em **"Create Endpoint"**.
   - **Nome**: "S3-Endpoint".
   - **Service**: Escolha "com.amazonaws.region.s3".
   - **VPC**: Selecione "MinhaVPC".
   - **Rota**: Selecione as sub-redes desejadas (por exemplo, "MinhaSubnetPrivada") e clique em **"Create Endpoint"**.

### **4. Testando e Verificando a Configuração da VPC**

1. **Lançar Instâncias EC2 em Sub-redes Públicas e Privadas**:
   - No painel EC2, crie uma instância em "MinhaSubnetPublica" e outra em "MinhaSubnetPrivada".
   - Verifique se a instância pública pode acessar a internet e a privada não.

2. **Testar Conexões entre as Instâncias**:
   - Conecte-se à instância na sub-rede pública usando SSH.
   - Da instância pública, tente pingar a instância na sub-rede privada para verificar a conectividade interna.

3. **Testar VPC Endpoints**:
   - Verifique se a instância na sub-rede privada pode acessar o S3 diretamente usando o VPC Endpoint, sem precisar passar pela internet.

### **5. Melhores Práticas ao Configurar VPCs**

- **Segregação de Ambientes**: Use diferentes VPCs para ambientes de desenvolvimento, teste e produção.
- **Monitoramento e Logs**: Habilite o AWS VPC Flow Logs para monitorar e registrar o tráfego de rede.
- **Princípio do Menor Privilégio**: Configure security groups e NACLs para permitir apenas o tráfego necessário.
- **Uso de VPC Endpoints**: Utilize VPC Endpoints para reduzir o tráfego pela internet pública e aumentar a segurança ao acessar serviços AWS.

### **6. Projeto: Criando uma Rede Segura na AWS com VPC**

**Objetivo do Projeto**: Construir uma infraestrutura de rede usando a VPC, garantindo que os recursos críticos estejam isolados e protegidos, enquanto mantém o acesso adequado aos recursos públicos.

**Passo a Passo Resumido:**

1. **Criação de VPC e Sub-redes**:
   - Configure a VPC e divida-a em sub-redes públicas e privadas.
2. **Implementação de Gateways e Tabelas de Roteamento**:
   - Configure o acesso à internet para sub-redes públicas e o uso de NAT para sub-redes privadas.
3. **Aplicação de Regras de Segurança**:
   - Use security groups, NACLs e VPC Endpoints para proteger recursos e otimizar o tráfego.
4. **Teste e Verificação**:
   - Teste o acesso entre instâncias e à internet para validar a configuração.

Essa aula cobre todos os componentes essenciais de uma VPC e fornece uma base sólida para a construção de redes seguras e bem configuradas na AWS.