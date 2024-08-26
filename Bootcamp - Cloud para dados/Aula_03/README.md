# Bootcamp Cloud: Aula 03

## EC2: Computação Escalável na AWS

**Objetivo:** Introduzir o Amazon EC2 (Elastic Compute Cloud), explorando suas funcionalidades principais, configurações e boas práticas. Durante a aula, criaremos uma instância EC2, configuraremos uma aplicação simples e discutiremos como utilizar o serviço para diferentes cenários na engenharia de dados.

---

### 1. Revisão da Aula Anterior: Configurando e Utilizando o S3

**Objetivo:** Revisar os conceitos e práticas da aula anterior sobre o Amazon S3, focando na criação e configuração de buckets, upload e download de arquivos, e como o S3 pode ser integrado em pipelines de dados.

#### Passo 1: Revisão da Criação de Buckets

1. **Criar um Bucket S3:**
   - Revisamos o processo de criação de um bucket S3, incluindo a escolha da região, configuração de controle de acesso e habilitação de versionamento.

2. **Aplicar Regras de Ciclo de Vida:**
   - Exploramos como configurar regras de ciclo de vida para mover dados entre diferentes classes de armazenamento e excluir objetos automaticamente após um período definido.

#### Passo 2: Revisão do Uso do boto3 para Interagir com o S3

1. **Criar e Listar Buckets:**
   - Utilizamos o boto3 para criar um bucket e listar todos os buckets existentes na conta AWS.

2. **Upload e Download de Arquivos:**
   - Praticamos o upload e download de arquivos entre o sistema local e o S3 utilizando o boto3, além de configurar permissões de acesso.

3. **Excluir Objetos e Buckets:**
   - Exploramos como excluir objetos e buckets utilizando comandos simples do boto3.

#### Passo 3: Revisão de Casos de Uso do S3

1. **Data Lake e ETL:**
   - Discutimos como o S3 é utilizado em arquiteturas de data lake e pipelines ETL, armazenando dados brutos e processados.

2. **Backup e Arquivamento:**
   - Exploramos o uso do S3 para backup e arquivamento de dados críticos, com a utilização de regras de ciclo de vida para otimizar custos.

---

## 2. O que é o EC2?

1. **Definição:**
   - Amazon EC2 (Elastic Compute Cloud) é um serviço de computação em nuvem que oferece capacidade de processamento escalável. Com o EC2, você pode lançar instâncias de máquinas virtuais (VMs) em questão de minutos, configurando-as de acordo com as necessidades específicas do seu projeto.

2. **Componentes Principais do EC2:**
   - **Instâncias:** Máquinas virtuais que rodam sistemas operacionais e aplicativos.
   - **Tipos de Instância:** Variam em termos de CPU, memória, armazenamento e capacidade de rede, permitindo otimizar custos e performance para diferentes workloads.
   - **AMIs (Amazon Machine Images):** Modelos predefinidos que incluem o sistema operacional e software inicial necessário para iniciar uma instância.
   - **Volumes EBS (Elastic Block Store):** Armazenamento persistente que pode ser conectado às instâncias EC2.
   - **Grupos de Segurança:** Firewalls virtuais que controlam o tráfego de entrada e saída das instâncias EC2.

---

## 3. Página Principal do EC2

### 3.1 Nível Gratuito do EC2

O Amazon EC2 oferece uma camada gratuita para novos usuários da AWS, permitindo que explorem e experimentem o serviço sem custos iniciais, dentro de determinados limites.

#### 3.1.1 Uso da Oferta (Mensal)

- **Instâncias do Linux do EC2:**
  - **Utilização:** 11%
  - **Horas Restantes:** 668 horas

Essa oferta inclui até 750 horas de uso de instâncias t2.micro ou t3.micro por mês, tanto para Linux quanto para Windows, durante os primeiros 12 meses após a criação da conta.

#### 3.1.2 Espaço de Armazenamento no EBS

- **Espaço Disponível:** A oferta gratuita também inclui 30 GB de armazenamento em volumes EBS (Elastic Block Store) de propósito geral ou magnéticos.

### 3.2 Integridade do Serviço

A AWS mantém uma alta disponibilidade de seus serviços em diferentes zonas de disponibilidade (AZs) dentro de uma região.

#### 3.2.1 Zonas

As zonas de disponibilidade são locais físicos isolados dentro de uma região da AWS, projetados para operar de forma independente em caso de falhas.

- **Nome da Zona:** `us-east-1a`
  - **ID da Zona:** `use1-az6`

- **Nome da Zona:** `us-east-1b`
  - **ID da Zona:** `use1-az1`

- **Nome da Zona:** `us-east-1c`
  - **ID da Zona:** `use1-az2`

### 3.3 Atributos da Conta

Os atributos da conta fornecem informações sobre a configuração e os recursos padrão disponíveis para sua conta AWS.

#### 3.3.1 VPC Padrão

- **ID da VPC:** `vpc-0cab8f7db8d745f83`

Cada conta AWS tem uma VPC padrão em cada região, que pode ser usada para criar e gerenciar recursos de rede.

#### 3.3.2 Configurações

As configurações de proteção e segurança de dados são fundamentais para garantir que seus recursos na AWS estejam seguros e protegidos.

#### 3.3.3 Console Serial do EC2

O Console Serial do EC2 é uma ferramenta que permite acesso direto ao console de uma instância para solução de problemas em instâncias EC2 que não estão acessíveis pela rede.

---

## 4. Configuração e Lançamento de uma Instância EC2

### 4.1 Criando uma Instância EC2 via AWS Management Console

1. **Acessando o AWS Management Console:**
   - Faça login no [AWS Management Console](https://aws.amazon.com) e navegue até o serviço EC2. Isso pode ser feito digitando "EC2" na barra de pesquisa superior e selecionando "EC2" nos resultados.

2. **Iniciando o Lançamento de uma Instância:**
   - Na página do EC2, clique em “Launch Instance” para iniciar o processo de criação.

3. **Escolhendo uma Amazon Machine Image (AMI):**
   - **AMI:** Selecione uma AMI que contenha o sistema operacional desejado. AMIs podem ser públicas, privadas ou compartilhadas. 
   - **Exemplo:** Escolha uma AMI Amazon Linux 2 ou Ubuntu.

4. **Selecionando o Tipo de Instância:**
   - **Tipo de Instância:** Escolha o tipo de instância que melhor se adequa ao seu workload. Tipos como t2.micro são elegíveis para o nível gratuito, ideal para testes e pequenas aplicações.
   - **Exemplo:** `t2.micro` (1 vCPU, 1 GiB RAM).

5. **Configuração da Instância:**
   - **Número de Instâncias:** Defina quantas instâncias deseja lançar.
   - **Network:** Selecione a VPC e sub-rede onde a instância será criada.
   - **IAM Role:** Atribua uma IAM role se a instância precisar acessar outros serviços AWS.

6. **Configuração de Armazenamento (Volumes EBS):**
   - **Adicionar Volumes:** Configure volumes EBS adicionais se necessário. O volume root é criado automaticamente com a AMI selecionada.
   - **Exemplo:** 8 GiB de General Purpose SSD.

7. **Configuração de Grupos de Segurança:**
   - **Criar/Selecionar Grupo de Segurança:** Configure as regras de firewall para controlar o tráfego de entrada e saída.
   - **Exemplo:** Permitir SSH (porta 22) de um IP específico para acessar a instância.

8. **Revisão e Lançamento:**
   - Revise todas as configurações e clique em “Launch”. Será solicitado que você selecione ou crie um par de chaves para acessar a instância via SSH.

### 4.2 Acessando a Instância via SSH

1. **Obtenção do IP Público da Instância:**
   - Após o lançamento, o EC2 atribui um IP público à instância. Este IP pode ser encontrado no console EC2.

2. **Acessando via SSH:**
   - Use o terminal ou um cliente SSH para acessar a instância.
   - **Exemplo de Comando SSH:**
     ```bash
     ssh -i "minha-chave.pem" ec2-user@ec2-xx-xxx-xx-xx.compute-1.amazonaws.com
     ```

3. **Configuração Inicial:**
   - Uma vez conectado, você pode atualizar o sistema operacional, instalar pacotes adicionais e configurar sua aplicação.

---

### 5. Famílias de Instâncias EC2

O Amazon EC2 oferece várias famílias de instâncias, cada uma projetada para diferentes tipos de workloads. As famílias são categorizadas com base em fatores como uso geral, computação intensiva, memória intensiva e otimização com hardware especializado. Abaixo estão as principais famílias de instâncias EC2 e suas respectivas aplicações em projetos de dados.

#### 5.1 General Purpose (Propósito Geral)

**Descrição:**
As instâncias General Purpose são projetadas para fornecer um equilíbrio de recursos de computação, memória e rede, tornando-as ide

ais para uma ampla variedade de workloads. Elas oferecem uma combinação versátil de recursos, sendo adequadas para a maioria das aplicações.

**Tipos de Instância:**
- **t3, t3a, t4g:** Instâncias com desempenho balanceado que são ideais para aplicações que precisam de uma carga moderada de computação e memória.
- **m6g, m6i, m5:** Oferecem uma proporção mais equilibrada de CPU e memória, sendo ideais para aplicações que exigem um pouco mais de recursos.

**Aplicações em Dados:**
- **Ambientes de Desenvolvimento e Teste:** Instâncias General Purpose são frequentemente usadas para configurar ambientes de desenvolvimento, testar pipelines de dados e executar simulações em pequena escala.
- **Aplicações de Banco de Dados:** Para bancos de dados de uso geral que não requerem otimização extrema de computação ou memória, como pequenos clusters de banco de dados NoSQL.
- **Servidores Web e de Aplicações:** Adequadas para hospedar servidores que processam dados e fornecem APIs para consultas e análises.

#### 5.2 Compute Optimized (Otimização de Computação)

**Descrição:**
As instâncias Compute Optimized são projetadas para workloads que exigem uma alta taxa de computação por núcleo de processador. Elas oferecem alta performance para tarefas intensivas em computação.

**Tipos de Instância:**
- **c7g, c6g, c6i, c5:** Oferecem uma alta relação de vCPU para memória, otimizando o desempenho para aplicações de computação intensiva.

**Aplicações em Dados:**
- **Processamento de Dados em Lote:** Ideal para tarefas como processamento em lote de grandes volumes de dados, onde o tempo de computação é um fator crítico.
- **Analytics e Modelagem de Dados:** Utilizadas em análises avançadas e modelagem estatística que requerem um grande poder de processamento.
- **Simulações e Modelagem Computacional:** Para workloads que envolvem cálculos complexos, como simulações financeiras ou científicas.

#### 5.3 Memory Optimized (Otimização de Memória)

**Descrição:**
As instâncias Memory Optimized são projetadas para workloads que exigem grandes quantidades de memória RAM, oferecendo alta capacidade de memória para processar grandes volumes de dados em memória.

**Tipos de Instância:**
- **r6g, r6i, r5, r5b:** Estas instâncias oferecem uma alta proporção de memória em relação ao número de vCPUs, sendo ideais para aplicações que precisam de grandes volumes de memória.
- **x2gd, x2idn:** São projetadas para cargas de trabalho que necessitam de ainda mais memória, como grandes bancos de dados em memória.

**Aplicações em Dados:**
- **Bancos de Dados em Memória:** Ideal para bancos de dados que mantêm grandes quantidades de dados na RAM, como Redis, Memcached ou bancos de dados em memória do SAP HANA.
- **Análise em Tempo Real:** Utilizadas em aplicações de análise de grandes volumes de dados em tempo real, onde a capacidade de processar dados diretamente na memória é crítica.
- **Big Data e Data Warehousing:** Adequadas para processar grandes volumes de dados em sistemas de data warehousing, como Amazon Redshift, ou para operações de ETL complexas.

#### 5.4 Accelerated Computing (Computação Acelerada)

**Descrição:**
As instâncias Accelerated Computing são projetadas para workloads que podem se beneficiar de hardware especializado, como GPUs ou FPGAs, proporcionando um aumento significativo no desempenho para tarefas específicas.

**Tipos de Instância:**
- **p4, p3:** Instâncias com GPUs NVIDIA, otimizadas para tarefas de deep learning, inferência de machine learning e simulações científicas.
- **g5g, g4ad:** Oferecem GPUs voltadas para renderização gráfica e codificação de vídeo.
- **f1:** Instâncias com FPGAs (Field Programmable Gate Arrays), adequadas para tarefas como criptografia e processamento de sinais.

**Aplicações em Dados:**
- **Treinamento de Modelos de Machine Learning:** Instâncias com GPUs são ideais para treinar modelos complexos de deep learning, permitindo um treinamento mais rápido e eficiente.
- **Inferência em Tempo Real:** Para aplicações de machine learning que requerem inferência em tempo real com latência mínima.
- **Simulações Computacionais e Modelagem 3D:** Utilizadas em simulações que exigem alto poder de processamento gráfico ou operações de matemática intensiva.
- **Análise de Vídeo e Imagem:** Ideal para processar e analisar grandes volumes de dados de vídeo e imagem em tempo real, como em sistemas de vigilância ou análise de conteúdo multimídia.

---

Cada uma dessas famílias de instâncias EC2 é otimizada para diferentes tipos de workloads e oferece recursos específicos que podem ser usados para maximizar a eficiência e o desempenho em projetos de dados. Escolher a instância certa depende dos requisitos específicos do seu projeto, como a quantidade de dados a ser processada, a complexidade das operações e a necessidade de memória, computação ou aceleração de hardware.

---

## 6. Tipos de Preço do EC2

O Amazon EC2 oferece diferentes modelos de precificação para atender às diversas necessidades e orçamentos dos usuários. Compreender esses modelos é essencial para otimizar custos e garantir que você está utilizando os recursos de maneira eficiente. A seguir, são apresentados os principais tipos de preço do EC2:

#### 6.1 Instâncias Sob Demanda (On-Demand)

**Descrição:**
As instâncias Sob Demanda permitem que você pague por capacidade de computação por hora ou por segundo (dependendo do tipo de instância) sem compromisso a longo prazo. Este modelo é ideal para cargas de trabalho que são imprevisíveis ou variáveis.

**Vantagens:**
- **Flexibilidade:** Você pode iniciar, parar e terminar instâncias a qualquer momento sem penalidades.
- **Sem Compromisso Inicial:** Não há necessidade de investir em contratos de longo prazo.
- **Escalabilidade:** Fácil de escalar conforme a demanda aumenta ou diminui.

**Aplicações Comuns:**
- Ambientes de desenvolvimento e teste.
- Aplicações com cargas de trabalho variáveis ou imprevisíveis.
- Projetos de curto prazo que não justificam um compromisso a longo prazo.

#### 6.2 Savings Plans (Planos de Economia)

**Descrição:**
Os Savings Plans oferecem descontos significativos (até 72%) em comparação com as tarifas Sob Demanda em troca de um compromisso de uso consistente (medido em dólares por hora) por um período de 1 ou 3 anos. Existem dois tipos principais de Savings Plans:

- **Compute Savings Plans:** Oferecem maior flexibilidade, aplicando-se a qualquer instância EC2 independente da região, tipo de instância, sistema operacional ou tenancy.
- **EC2 Instance Savings Plans:** Oferecem descontos maiores, mas são aplicáveis apenas a instâncias específicas dentro de uma família de instâncias e região selecionadas.

**Vantagens:**
- **Descontos Significativos:** Economia considerável em comparação com o modelo Sob Demanda.
- **Flexibilidade (no caso dos Compute Savings Plans):** Possibilidade de alterar tipos de instância e regiões sem perder os descontos.
- **Previsibilidade de Custos:** Facilita o planejamento financeiro com base no compromisso de uso.

**Aplicações Comuns:**
- Cargas de trabalho estáveis e previsíveis que podem se comprometer com um nível de uso consistente.
- Empresas que buscam otimizar custos a longo prazo.

#### 6.3 Instâncias Spot

**Descrição:**
As Instâncias Spot permitem que você aproveite a capacidade ociosa da AWS com descontos de até 90% em relação às tarifas Sob Demanda. No entanto, a AWS pode interromper essas instâncias com um aviso prévio de dois minutos quando precisar recuperar a capacidade.

**Vantagens:**
- **Custo Reduzido:** Descontos significativos tornam as Instâncias Spot extremamente econômicas.
- **Escalabilidade:** Ideal para workloads que podem ser interrompidos e retomados sem impacto significativo.

**Desvantagens:**
- **Interrupções:** A possibilidade de interrupção a qualquer momento pode não ser adequada para todas as aplicações.
- **Disponibilidade Variável:** A disponibilidade das Instâncias Spot pode variar conforme a demanda.

**Aplicações Comuns:**
- Processamento em lote e tarefas de ETL.
- Treinamento de modelos de machine learning que podem ser reiniciados.
- Aplicações distribuídas e resilientes que podem lidar com interrupções, como clusters de Hadoop ou Spark.

#### 6.4 Instâncias Dedicadas (Dedicated Instances)

**Descrição:**
As Instâncias Dedicadas são executadas em hardware físico dedicado exclusivamente para a sua conta AWS. Isso garante que suas instâncias não compartilhem hardware com instâncias de outros clientes.

**Vantagens:**
- **Isolamento Físico:** Maior segurança e conformidade para cargas de trabalho sensíveis.
- **Controle de Hardware:** Garantia de que os recursos de hardware não serão compartilhados com outros clientes.

**Desvantagens:**
- **Custo Mais Elevado:** Geralmente, as Instâncias Dedicadas são mais caras do que as instâncias compartilhadas.
- **Menor Flexibilidade de Preço:** Não se beneficiam tanto de descontos como os Savings Plans ou Instâncias Spot.

**Aplicações Comuns:**
- Aplicações que exigem conformidade regulatória específica.
- Cargas de trabalho sensíveis que necessitam de isolamento físico por razões de segurança.
- Ambientes empresariais que requerem controle total sobre o hardware subjacente.

---

### Comparação dos Modelos de Pre

ço

| Modelo de Preço       | Flexibilidade | Desconto em Relação ao On-Demand | Compromisso Necessário | Adequado para                                       |
|-----------------------|---------------|-----------------------------------|------------------------|-----------------------------------------------------|
| Sob Demanda           | Alta          | 0%                                | Nenhum                 | Cargas de trabalho imprevisíveis ou variáveis       |
| Savings Plans         | Média/Alta    | Até 72%                            | Sim (1 ou 3 anos)      | Cargas de trabalho estáveis e previsíveis           |
| Instâncias Spot       | Baixa         | Até 90%                            | Não                    | Processamento em lote, machine learning, workloads resilientes |
| Instâncias Dedicadas  | Média         | 0-30%                             | Nenhum ou contratual    | Aplicações sensíveis, conformidade regulatória      |

### Considerações para Escolha do Modelo de Preço

- **Natureza da Carga de Trabalho:** Se sua aplicação pode tolerar interrupções, as Instâncias Spot podem oferecer enormes economias. Para cargas de trabalho críticas que não podem ser interrompidas, as Instâncias Sob Demanda ou Savings Plans são mais adequadas.
- **Previsibilidade de Uso:** Se você pode prever consistentemente o uso de computação, os Savings Plans proporcionam uma excelente relação custo-benefício.
- **Requisitos de Segurança e Conformidade:** Instâncias Dedicadas são necessárias para certas aplicações que exigem isolamento físico.
- **Orçamento e Otimização de Custos:** Avalie o equilíbrio entre economia e flexibilidade para selecionar o modelo que melhor se alinha ao seu orçamento e necessidades operacionais.

### Estratégias para Otimização de Custos

1. **Mix de Modelos de Preço:** Utilizar uma combinação de diferentes modelos de preço (por exemplo, Sob Demanda para cargas variáveis, Savings Plans para cargas estáveis e Spot para tarefas flexíveis) pode maximizar a economia sem comprometer a performance.
2. **Monitoramento e Ajustes Contínuos:** Utilize ferramentas como AWS Cost Explorer e AWS Trusted Advisor para monitorar o uso e ajustar as estratégias de compra conforme necessário.
3. **Automação com Auto Scaling:** Configure grupos de Auto Scaling para aproveitar automaticamente as Instâncias Spot quando disponíveis e mudar para instâncias Sob Demanda ou reservadas quando necessário.
4. **Escolha de Regiões e Tipos de Instância:** Selecionar regiões com custos mais baixos e tipos de instância que melhor atendem às necessidades de desempenho pode reduzir significativamente os custos.


### 1. **Configurar a Instância EC2**

https://github.com/lvgalvao/AIRFLOW-Do-Jupyter-Notebook-Pro-Deploy