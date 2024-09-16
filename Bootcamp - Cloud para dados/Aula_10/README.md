# Aula 10: Gestão de Custos na AWS

**Objetivo**: Vocês já sentiram que seus projetos na AWS estão sempre te assustando no final do mês com faturas inesperadas? Com recursos espalhados por todos os lados sem nenhum controle? Os custos estão subindo e a organização parece um desafio insuperável? Hoje, na nossa Aula 10 - Gestão de Custos na AWS, isso vai mudar. Nesta aula, vamos refatorar nossa conta, organizar os recursos e implementar práticas eficientes de gestão de custos. Nosso objetivo é organizar a casa e assumir o controle financeiro dos nossos projetos.

Hoje vamos desvendar os segredos da gestão eficiente de custos na AWS. Vamos aprender a utilizar grupos de recursos, aplicar tags inteligentes e explorar ferramentas como o AWS Cost Explorer e AWS Budgets, que nos darão o controle total sobre nossos projetos. Imagine transformar dez projetos caóticos em um ambiente organizado e econômico. Está na hora de assumir o controle, otimizar recursos e impulsionar nossos resultados. Preparados para essa jornada rumo à eficiência e à economia? Então, vamos começar hoje às 12h!

### **Projetos da Aula 10**

1. **Organização de Recursos com Tags**

   **Objetivo**: Aprender a aplicar tags nos recursos AWS para facilitar a identificação, organização e gerenciamento de custos.

   **Passo a Passo**:

   1. **Acessar o Console AWS**:
      - Faça login no AWS Management Console.

   2. **Identificar Recursos Sem Tags**:
      - Navegue até o **Resource Groups & Tag Editor**.
      - Clique em **Tag Editor**.
      - Selecione a região ou regiões onde seus recursos estão.
      - Deixe todos os tipos de recursos selecionados ou escolha os que deseja taguear.
      - Clique em **Find resources**.

   3. **Adicionar Tags aos Recursos**:
      - Na lista de recursos retornados, selecione os recursos que deseja taguear.
      - Clique em **Add tags to selected resources**.
      - Adicione as tags apropriadas. Por exemplo:
        - **Key**: `Project`, **Value**: `Projeto1`
        - **Key**: `Environment`, **Value**: `Production`
      - Clique em **Save changes**.

   4. **Repetir o Processo para Outros Projetos**:
      - Certifique-se de que todos os recursos dos 10 projetos estejam devidamente tagueados.

   **Benefícios das Tags**:
   - Facilita a identificação de recursos.
   - Permite a filtragem de custos por projeto, ambiente, etc.
   - Melhora a organização e a governança.

   ```mermaid
   graph LR
       User[Usuário] -->|Aplica Tags| AWS[Recursos AWS]
       AWS --> CostManagement[Gestão de Custos]
   ```

2. **Criando Grupos de Recursos**

   **Objetivo**: Aprender a criar grupos de recursos baseados em tags para facilitar a visualização e o gerenciamento coletivo de recursos relacionados.

   **Passo a Passo**:

   1. **Acessar o AWS Resource Groups**:
      - No Console AWS, procure por **Resource Groups**.

   2. **Criar um Novo Grupo de Recursos**:
      - Clique em **Create a resource group**.
      - Escolha **Tag-based group**.

   3. **Definir Critérios do Grupo**:
      - Adicione as tags que identificam o projeto. Por exemplo:
        - **Key**: `Project`
        - **Value**: `Projeto1`
      - O grupo incluirá todos os recursos com essas tags.

   4. **Nomear e Salvar o Grupo**:
      - Dê um nome ao grupo, como `Grupo_Projeto1`.
      - Clique em **Create group**.

   5. **Repetir para Outros Projetos**:
      - Crie grupos para cada um dos 10 projetos usando as tags correspondentes.

   **Benefícios dos Grupos de Recursos**:
   - Visualização consolidada dos recursos de um projeto.
   - Acesso rápido a recursos relacionados.
   - Melhora na gestão e operações diárias.

   ```mermaid
   graph LR
       Tags[Tags] --> ResourceGroups[Grupos de Recursos]
       ResourceGroups --> Management[Facilita a Gestão]
   ```

3. **Utilizando o AWS Cost Explorer**

   **Objetivo**: Aprender a usar o AWS Cost Explorer para analisar os custos e identificar tendências e anomalias.

   **Passo a Passo**:

   1. **Acessar o AWS Cost Management**:
      - No Console AWS, vá para **Cost Management**.
      - Selecione **Cost Explorer**.

   2. **Ativar o Cost Explorer (se ainda não estiver ativo)**:
      - Clique em **Enable Cost Explorer**.

   3. **Explorar os Custos**:
      - Utilize os filtros para visualizar os custos por **Service**, **Usage Type**, **Tag**, etc.
      - Para visualizar por projeto, filtre por **Tag Key**: `Project`.

   4. **Analisar Tendências**:
      - Observe os gráficos para identificar padrões de consumo.
      - Identifique picos ou aumentos inesperados nos custos.

   5. **Salvar Relatórios Personalizados**:
      - Customize o relatório conforme suas necessidades.
      - Clique em **Save as report** para salvar a configuração.

   **Benefícios do Cost Explorer**:
   - Visão detalhada dos custos.
   - Identificação de oportunidades de economia.
   - Monitoramento contínuo dos gastos.

   ```mermaid
   graph LR
       CostExplorer[Cost Explorer] --> Analysis[Análise de Custos]
       Analysis --> Optimization[Otimização]
   ```

4. **Configurando AWS Budgets**

   **Objetivo**: Estabelecer orçamentos para monitorar os gastos e receber alertas quando os custos excederem limites definidos.

   **Passo a Passo**:

   1. **Acessar o AWS Budgets**:
      - No **Cost Management**, selecione **Budgets**.

   2. **Criar um Novo Orçamento**:
      - Clique em **Create budget**.

   3. **Selecionar Tipo de Orçamento**:
      - Escolha **Cost Budget**.

   4. **Definir Detalhes do Orçamento**:
      - Nome do orçamento: `Orçamento_Projeto1`.
      - Período: Mensal.
      - Monto do orçamento: Defina o valor máximo que deseja gastar, por exemplo, `$500`.

   5. **Aplicar Filtros**:
      - Em **Filters**, adicione a tag do projeto:
        - **Key**: `Project`
        - **Value**: `Projeto1`

   6. **Configurar Alertas**:
      - Defina quando deseja ser notificado, por exemplo:
        - Quando atingir 80% do orçamento.
        - Quando ultrapassar 100% do orçamento.
      - Adicione os emails que devem receber os alertas.

   7. **Revisar e Criar**:
      - Revise as configurações e clique em **Create budget**.

   8. **Repetir para Outros Projetos**:
      - Crie orçamentos para cada projeto conforme necessário.

   **Benefícios do AWS Budgets**:
   - Controle proativo dos custos.
   - Recebimento de alertas antes que os custos saiam do controle.
   - Planejamento financeiro mais assertivo.

   ```mermaid
   graph LR
       Budgets[AWS Budgets] --> Monitoring[Monitoramento de Custos]
       Monitoring --> Alerts[Alertas]
   ```

5. **Implementando AWS Cost Anomaly Detection**

   **Objetivo**: Configurar o AWS Cost Anomaly Detection para identificar automaticamente anomalias nos gastos e receber notificações.

   **Passo a Passo**:

   1. **Acessar o Cost Anomaly Detection**:
      - No **Cost Management**, selecione **Anomaly Detection**.

   2. **Criar um Monitor de Anomalias**:
      - Clique em **Create monitor**.

   3. **Definir o Escopo do Monitor**:
      - Escolha **Single Account** ou **Linked Accounts** se houver.
      - Em **Monitor dimensions**, você pode selecionar por **Tags**:
        - **Key**: `Project`
        - **Value**: `Projeto1`

   4. **Configurar Alertas**:
      - Defina o **Anomaly threshold** para determinar a sensibilidade.
      - Adicione os emails para notificações.

   5. **Revisar e Criar**:
      - Revise as configurações e clique em **Create monitor**.

   **Benefícios do Cost Anomaly Detection**:
   - Detecção automática de gastos incomuns.
   - Resposta rápida a problemas potenciais.
   - Proteção contra custos inesperados.

   ```mermaid
   graph LR
       AnomalyDetection[Anomaly Detection] --> IdentifyAnomalies[Identifica Anomalias]
       IdentifyAnomalies --> Notifications[Notificações]
   ```

### **Ferramentas Adicionais**

- **AWS Trusted Advisor**:
  - Verifique recomendações de otimização de custos, desempenho, segurança, tolerância a falhas e limites de serviço.
  - Acesse através do Console AWS em **Trusted Advisor**.

- **AWS Cost and Usage Reports**:
  - Obtenha relatórios detalhados de uso e custos.
  - Configure no **Cost Management** em **Cost and Usage Reports**.

### **Conclusão da Aula 10**

Nesta aula, abordamos estratégias e ferramentas essenciais para a gestão eficaz de custos na AWS. Aprendemos a organizar nossos recursos utilizando tags e grupos de recursos, o que facilita a identificação e o gerenciamento dos mesmos. Exploramos o AWS Cost Explorer para analisar nossos gastos, configuramos orçamentos com o AWS Budgets para monitorar e controlar os custos, e implementamos o AWS Cost Anomaly Detection para detectar e responder rapidamente a quaisquer gastos anormais.

Com essas práticas, estamos equipados para transformar um ambiente caótico em um ecossistema organizado e financeiramente otimizado. A gestão de custos não é apenas sobre economizar dinheiro, mas também sobre entender onde e como seus recursos estão sendo utilizados para tomar decisões informadas que impulsionam o sucesso dos seus projetos.