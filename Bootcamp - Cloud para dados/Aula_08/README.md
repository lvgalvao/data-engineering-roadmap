Aqui estão os comandos isolados que você pode utilizar para configurar sua instância EC2, clonar o repositório do GitHub, configurar o ambiente e executar o contêiner Docker com as variáveis de ambiente do banco de dados.

https://www.google.com/search?q=how+to+access+my+rds+private+using+bastian+host&oq=how+to+access+my+rds+private+using+bastian+host&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORigATIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRigAdIBCTEwMjc4ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8

### **Comandos para Configuração da Instância EC2:**

1. **Atualizar Pacotes e Instalar Docker e Git:**

   ```bash
   sudo su
   sudo apt-get update
   sudo apt install -y git docker.io docker-compose
   ```

3. **Clonar o Repositório do GitHub:**

   ```bash
   git clone https://github.com/lvgalvao/api-scheduler-python-rds.git /app
   ```

4. **Navegar para o Diretório do Projeto:**

   ```bash
   cd /app
   ```

5. **Construir a Imagem Docker a Partir do Dockerfile:**

   ```bash
   sudo docker build -t api-schedule-app .
   ```

6. **Executar o Contêiner Docker com as Variáveis de Ambiente do Banco de Dados:**

   ```bash
   sudo docker run -d \
  --name api-schedule-app-container \
  -e CMC_API_KEY=<senha> \
  api-schedule-app
   ```

### **Explicações dos Comandos:**

- **Instalação de Docker e Git:** Instala as ferramentas necessárias para rodar o projeto.
- **Início do Docker:** Inicia o serviço Docker e habilita-o para iniciar automaticamente com a instância.
- **Clonagem do Repositório:** Clona o código do repositório para o diretório `/app` na instância.
- **Construção da Imagem Docker:** Cria a imagem Docker a partir do `Dockerfile` disponível no repositório.
- **Execução do Contêiner:** Roda o contêiner Docker, configurando as variáveis de ambiente necessárias para conectar ao banco de dados.

Esses comandos são práticos e podem ser adicionados ao README do seu projeto para facilitar o setup completo da aplicação na instância EC2.

Para configurar as regras de segurança da sua instância EC2, você deve ajustar o Security Group (grupo de segurança) para permitir o acesso necessário à instância de forma segura. Aqui estão as regras comuns e recomendadas para uma configuração básica de uma instância EC2 que hospeda um contêiner Docker executando uma aplicação Python conectando-se a um banco de dados RDS:

### **Regras de Segurança para a Instância EC2:**

1. **Acesso SSH (Porta 22)**:
   - **Tipo**: SSH
   - **Porta**: 22
   - **Origem**: Seu IP específico (ou seja, `My IP`) para acesso seguro. Evite usar `0.0.0.0/0`, pois isso permite acesso de qualquer lugar, o que não é seguro.

2. **Acesso HTTP (Porta 80)**:
   - **Tipo**: HTTP
   - **Porta**: 80
   - **Origem**: `0.0.0.0/0` (aberto para todos) se você precisar que o serviço seja acessível publicamente.
   - **Observação**: Use esta regra se a sua aplicação estiver servindo algo na web.

3. **Acesso HTTPS (Porta 443)** *(Opcional)*:
   - **Tipo**: HTTPS
   - **Porta**: 443
   - **Origem**: `0.0.0.0/0` se precisar de acesso público seguro.

4. **Acesso à Aplicação (Porta 8501 para Streamlit, se aplicável)**:
   - **Tipo**: Custom TCP Rule
   - **Porta**: 8501 (ou a porta específica que sua aplicação utiliza)
   - **Origem**: `0.0.0.0/0` se precisar que o serviço seja acessível publicamente, ou restrinja a IPs específicos conforme sua necessidade.

5. **Acesso ao Banco de Dados (Porta 5432 para PostgreSQL, por exemplo)**:
   - **Tipo**: Custom TCP Rule ou específico para o seu banco (ex.: PostgreSQL)
   - **Porta**: 5432 (ou outra porta se usar um banco de dados diferente)
   - **Origem**: O Security Group do seu banco de dados deve permitir acesso **somente** a partir do Security Group da EC2. Isso é configurado no Security Group do RDS.

### **Exemplo de Regras para o Security Group da EC2:**

| Tipo   | Protocolo | Porta | Origem        | Descrição                                 |
|--------|-----------|-------|---------------|-------------------------------------------|
| SSH    | TCP       | 22    | Seu IP        | Acesso SSH restrito ao seu IP            