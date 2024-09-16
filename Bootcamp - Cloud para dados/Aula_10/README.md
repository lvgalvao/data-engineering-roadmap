# Aula 10: Gestão de Custos na AWS

**Objetivo**: Vocês já sentiram que seus projetos na AWS estão sempre te assustando no final do mês com faturas inesperadas? Com recursos espalhados por todos os lados sem nenhum controle? Os custos estão subindo e a organização parece um desafio insuperável? Hoje, na nossa Aula 10 - Gestão de Custos na AWS, isso vai mudar. Nesta aula, vamos refatorar nossa conta, organizar os recursos e implementar práticas eficientes de gestão de custos. Nosso objetivo é organizar a casa e assumir o controle financeiro dos nossos projetos.

Hoje vamos desvendar os segredos da gestão eficiente de custos na AWS. Vamos aprender a estabelecer uma **política de tags focada em governança de custos**, utilizar grupos de recursos, aplicar tags inteligentes e explorar ferramentas como o AWS Cost Explorer e AWS Budgets, que nos darão o controle total sobre nossos projetos. Imagine transformar dez projetos caóticos em um ambiente organizado e econômico. Está na hora de assumir o controle, otimizar recursos e impulsionar nossos resultados. Preparados para essa jornada rumo à eficiência e à economia? Então, vamos começar hoje às 12h!

### **Política de Tags Focada em Governança de Custos**

Antes de iniciarmos com as ferramentas, é crucial estabelecermos uma política de tags consistente e obrigatória para todos os recursos AWS. As tags são fundamentais para a governança de custos, pois permitem a categorização e atribuição de custos aos respectivos responsáveis e projetos.

**5 Tags Obrigatórias Focadas em Governança de Custos:**

1. **CostCenter (Centro de Custo)**:
   - **Descrição**: Identifica o centro de custo ou departamento responsável pelas despesas associadas ao recurso.
   - **Exemplo**: `CostCenter: CC1001`

2. **Project (Projeto)**:
   - **Descrição**: Nome do projeto ao qual o recurso pertence.
   - **Exemplo**: `Project: ProjetoX`

3. **Owner (Responsável)**:
   - **Descrição**: Pessoa ou equipe responsável pelo recurso.
   - **Exemplo**: `Owner: JoãoSilva`

4. **Environment (Ambiente)**:
   - **Descrição**: Indica o ambiente de utilização do recurso.
   - **Exemplo**: `Environment: Production` ou `Environment: Development`

5. **Application (Aplicação)**:
   - **Descrição**: Nome da aplicação ou serviço que utiliza o recurso.
   - **Exemplo**: `Application: AppMobile`

**Importância das Tags na Governança de Custos:**

- **Atribuição de Custos**: Permite que os custos sejam atribuídos corretamente aos centros de custo, projetos e responsáveis.
- **Responsabilidade**: Identifica claramente quem é responsável por cada recurso.
- **Otimização**: Facilita a identificação de recursos subutilizados ou desnecessários.
- **Relatórios Personalizados**: Possibilita a geração de relatórios detalhados por tags no AWS Cost Explorer e outros serviços.

### **Projetos da Aula 10**

1. **Estabelecendo e Aplicando a Política de Tags**

   **Objetivo**: Criar uma política de tags consistente e aplicá-la a todos os recursos AWS, garantindo que as 5 tags obrigatórias estejam presentes em cada recurso.

   **Passo a Passo**:

   1. **Definir a Política de Tags**:
      - Documente as tags obrigatórias e suas respectivas chaves e valores esperados.
      - Distribua a política para todas as equipes envolvidas.

   2. **Acessar o Console AWS**:
      - Faça login no AWS Management Console.

   3. **Identificar Recursos Sem as Tags Obrigatórias**:
      - Navegue até o **Resource Groups & Tag Editor**.
      - Clique em **Tag Editor**.
      - Selecione as regiões e tipos de recursos relevantes.
      - Clique em **Find resources**.

   4. **Filtrar Recursos Sem as Tags Obrigatórias**:
      - Utilize filtros para identificar recursos que não possuem as tags obrigatórias.

   5. **Adicionar as Tags aos Recursos**:
      - Selecione os recursos sem as tags.
      - Clique em **Add tags to selected resources**.
      - Adicione as 5 tags obrigatórias com os valores apropriados.
      - Clique em **Save changes**.

   6. **Automatizar a Conformidade de Tags**:
      - Utilize o **AWS Config** para criar regras que verificam a conformidade das tags.
      - Configure alertas para recursos que não atendam à política de tags.

   **Benefícios**:

   - **Consistência**: Todos os recursos seguem o mesmo padrão de tagueamento.
   - **Governança**: Melhora o controle e a gestão dos recursos.
   - **Facilidade na Gestão de Custos**: As tags permitem atribuir custos corretamente.

   ```mermaid
   graph LR
       Policy[Política de Tags] --> Teams[Equipes]
       Teams --> ApplyTags[Aplicam Tags nos Recursos]
       ApplyTags --> AWSResources[Recursos AWS]
   ```

2. **Organização de Recursos com Tags**

   **Objetivo**: Utilizar as tags aplicadas para organizar e gerenciar os recursos de forma eficaz.

   **Passo a Passo**:

   1. **Verificar Tags nos Recursos**:
      - Confirme que todos os recursos possuem as 5 tags obrigatórias.

   2. **Navegar pelos Recursos Usando Tags**:
      - Utilize o **Tag Editor** para pesquisar recursos por tags.
      - Filtre recursos por `Project`, `CostCenter`, `Owner`, etc.

   3. **Analisar Recursos por Responsável**:
      - Filtre recursos pela tag `Owner` para ver quais recursos estão sob responsabilidade de cada pessoa ou equipe.

   4. **Gerenciar Recursos por Ambiente**:
      - Use a tag `Environment` para distinguir recursos de produção, desenvolvimento, etc.

   **Benefícios**:

   - **Eficiência**: Localização rápida de recursos específicos.
   - **Responsabilização**: Facilita o acompanhamento de quem é responsável por cada recurso.
   - **Otimização**: Identificação de recursos redundantes ou subutilizados.

   ```mermaid
   graph LR
       Tags[Tags] --> Organize[Organização de Recursos]
       Organize --> EfficientManagement[Gestão Eficiente]
   ```

3. **Criando Grupos de Recursos Baseados em Tags**

   **Objetivo**: Criar grupos de recursos utilizando as tags para facilitar o gerenciamento coletivo.

   **Passo a Passo**:

   1. **Acessar o AWS Resource Groups**:
      - No Console AWS, procure por **Resource Groups**.

   2. **Criar um Novo Grupo de Recursos**:
      - Clique em **Create a resource group**.
      - Escolha **Tag-based group**.

   3. **Definir Critérios do Grupo**:
      - Configure o grupo usando as tags obrigatórias.
      - Por exemplo, para agrupar recursos de um projeto:
        - **Key**: `Project`
        - **Value**: `ProjetoX`

   4. **Nomear e Salvar o Grupo**:
      - Dê um nome ao grupo, como `Grupo_ProjetoX`.
      - Clique em **Create group**.

   5. **Utilizar Grupos para Gestão**:
      - Navegue pelos grupos para gerenciar recursos coletivamente.
      - Realize operações em lote quando aplicável.

   **Benefícios**:

   - **Visibilidade**: Visualização consolidada dos recursos por projeto, centro de custo, etc.
   - **Gestão Simplificada**: Ações coletivas nos recursos do grupo.
   - **Facilita a Governança**: Monitoramento e controle aprimorados.

   ```mermaid
   graph LR
       Tags[Tags] --> ResourceGroups[Grupos de Recursos]
       ResourceGroups --> Management[Gestão Simplificada]
   ```

4. **Utilizando o AWS Cost Explorer com Tags**

   **Objetivo**: Analisar os custos detalhadamente utilizando as tags aplicadas nos recursos.

   **Passo a Passo**:

   1. **Acessar o AWS Cost Management**:
      - No Console AWS, vá para **Cost Management**.
      - Selecione **Cost Explorer**.

   2. **Ativar o Cost Explorer (se ainda não estiver ativo)**:
      - Clique em **Enable Cost Explorer**.

   3. **Configurar o Cost Explorer para Exibir Tags**:
      - Vá para **Cost Explorer Settings**.
      - Em **Cost Allocation Tags**, ative as tags que deseja utilizar nos relatórios (as 5 tags obrigatórias).

   4. **Explorar os Custos por Tags**:
      - Crie relatórios filtrando ou agrupando por tags como `CostCenter`, `Project`, `Owner`, etc.
      - Visualize os custos associados a cada centro de custo, projeto ou responsável.

   5. **Identificar Tendências e Oportunidades de Otimização**:
      - Analise os gráficos e dados para identificar áreas de alto gasto.
      - Use as informações para tomar decisões de otimização.

   **Benefícios**:

   - **Transparência**: Visibilidade clara de onde os custos estão sendo gerados.
   - **Atribuição de Custos Precisa**: Alocação correta de despesas aos centros de custo e projetos.
   - **Decisões Informadas**: Dados detalhados para suportar estratégias de otimização.

   ```mermaid
   graph LR
       CostExplorer[Cost Explorer] --> Analysis[Análise de Custos por Tags]
       Analysis --> Optimization[Otimização]
   ```

5. **Configurando AWS Budgets com Base nas Tags**

   **Objetivo**: Estabelecer orçamentos para monitorar os gastos e receber alertas quando os custos excederem limites definidos, utilizando as tags para especificar o escopo.

   **Passo a Passo**:

   1. **Acessar o AWS Budgets**:
      - No **Cost Management**, selecione **Budgets**.

   2. **Criar um Novo Orçamento**:
      - Clique em **Create budget**.

   3. **Selecionar Tipo de Orçamento**:
      - Escolha **Cost Budget**.

   4. **Definir Detalhes do Orçamento**:
      - Nome do orçamento: `Orçamento_CentroDeCusto_CC1001`.
      - Período: Mensal.
      - Valor do orçamento: Defina o valor máximo para o centro de custo, por exemplo, `$5,000`.

   5. **Aplicar Filtros com Tags**:
      - Em **Filters**, adicione a tag:
        - **Key**: `CostCenter`
        - **Value**: `CC1001`

   6. **Configurar Alertas**:
      - Defina quando deseja ser notificado:
        - Quando atingir 80% do orçamento.
        - Quando ultrapassar 100% do orçamento.
      - Adicione os emails dos responsáveis (utilizando a tag `Owner` para referência).

   7. **Revisar e Criar**:
      - Revise as configurações e clique em **Create budget**.

   8. **Repetir para Outros Centros de Custo ou Projetos**:
      - Crie orçamentos para cada centro de custo ou projeto conforme necessário.

   **Benefícios**:

   - **Controle Financeiro**: Monitoramento proativo dos gastos por centro de custo ou projeto.
   - **Alertas Personalizados**: Notificações para os responsáveis quando os limites são atingidos.
   - **Planejamento Financeiro Eficaz**: Apoio na elaboração e cumprimento de orçamentos.

   ```mermaid
   graph LR
       Budgets[AWS Budgets] --> Monitoring[Monitoramento de Custos por Tags]
       Monitoring --> Alerts[Alertas Personalizados]
   ```

6. **Implementando AWS Cost Anomaly Detection com Tags**

   **Objetivo**: Configurar o AWS Cost Anomaly Detection para identificar automaticamente anomalias nos gastos específicos a centros de custo, projetos ou responsáveis.

   **Passo a Passo**:

   1. **Acessar o Cost Anomaly Detection**:
      - No **Cost Management**, selecione **Anomaly Detection**.

   2. **Criar um Monitor de Anomalias**:
      - Clique em **Create monitor**.

   3. **Definir o Escopo do Monitor com Tags**:
      - Escolha **Single Account** ou **Linked Accounts** se houver.
      - Em **Monitor dimensions**, selecione **Tag**:
        - **Key**: `CostCenter`
        - **Value**: `CC1001`

   4. **Configurar Alertas**:
      - Defina o **Anomaly threshold** para determinar a sensibilidade.
      - Adicione os emails dos responsáveis (`Owner`) para notificações.

   5. **Revisar e Criar**:
      - Revise as configurações e clique em **Create monitor**.

   **Benefícios**:

   - **Detecção Personalizada**: Análise de anomalias em áreas específicas.
   - **Resposta Rápida**: Notificações imediatas para os responsáveis.
   - **Proteção Financeira**: Prevenção de gastos inesperados.

   ```mermaid
   graph LR
       AnomalyDetection[Anomaly Detection] --> IdentifyAnomalies[Identifica Anomalias por Tags]
       IdentifyAnomalies --> Notifications[Notificações para Responsáveis]
   ```

### **Ferramentas Adicionais**

- **AWS Config**:
  - Configure regras para garantir que todos os recursos tenham as tags obrigatórias.
  - Receba alertas ou visualize não conformidades quando recursos não atenderem à política.

- **AWS Trusted Advisor**:
  - Utilize as verificações de otimização de custos, segurança e desempenho.
  - Acesse através do Console AWS em **Trusted Advisor**.

- **AWS Cost and Usage Reports**:
  - Obtenha relatórios detalhados que incluem as tags para análise avançada.
  - Configure no **Cost Management** em **Cost and Usage Reports**.

### **Conclusão da Aula 10**

Nesta aula, enfatizamos a importância de uma política de tags bem definida e consistente como base para a governança eficaz de custos na AWS. Aprendemos a aplicar as 5 tags obrigatórias focadas em governança de custos, permitindo uma gestão detalhada e precisa dos recursos. Utilizamos essas tags em conjunto com ferramentas poderosas como o AWS Cost Explorer, AWS Budgets e AWS Cost Anomaly Detection para obter visibilidade, controle e otimização dos gastos.

Ao estabelecer e aderir a uma política de tags robusta, capacitamos nossas equipes a serem responsáveis pelos recursos que gerenciam, promovendo uma cultura de responsabilidade e eficiência. Com essas práticas implementadas, estamos melhor posicionados para transformar um ambiente desorganizado em uma infraestrutura otimizada e financeiramente saudável, garantindo o sucesso contínuo dos nossos projetos.

---

**Próximos Passos**:

- **Revisar a Política de Tags Regularmente**: Certifique-se de que a política continua relevante e atualizada com as necessidades da organização.
- **Treinamento Contínuo**: Promova workshops e sessões de treinamento para as equipes sobre a importância da tagueação correta.
- **Automatização**: Explore ferramentas e scripts para automatizar a aplicação de tags e a conformidade com a política estabelecida.

Com essas ações, garantiremos uma gestão de custos eficaz e uma governança sólida, permitindo que nos concentremos no que realmente importa: impulsionar nossos projetos para o sucesso.

### **Checklist para Evitar Surpresas no Final do Mês**

Para garantir que os custos na AWS permaneçam sob controle e evitar despesas inesperadas, siga este checklist regularmente:

1. **Revisar Orçamentos no AWS Budgets**:
   - Verifique os orçamentos configurados para cada centro de custo, projeto e responsável.
   - Certifique-se de que os alertas estão configurados corretamente e os contatos estão atualizados.

2. **Monitorar Gastos Diariamente**:
   - Utilize o **AWS Cost Explorer** para acompanhar os gastos diários ou semanais.
   - Configure relatórios personalizados para serem enviados por e-mail regularmente.

3. **Analisar Anomalias com o AWS Cost Anomaly Detection**:
   - Revise notificações de anomalias de custo.
   - Investigue imediatamente quaisquer gastos inesperados ou incomuns.

4. **Garantir a Conformidade das Tags**:
   - Use o **AWS Config** para verificar se todos os recursos possuem as **5 tags obrigatórias**.
   - Corrija recursos que não estejam em conformidade com a política de tags.

5. **Desligar Recursos Não Utilizados**:
   - Identifique recursos ociosos ou subutilizados, como instâncias EC2 não utilizadas, volumes EBS não anexados, etc.
   - Desligue ou exclua esses recursos para reduzir custos desnecessários.

6. **Revisar Reservas e Savings Plans**:
   - Avalie se **Reserved Instances** ou **Savings Plans** podem ser utilizados para recursos de uso contínuo.
   - Ajuste ou renove conforme necessário para maximizar economias.

7. **Comunicar-se com as Equipes Responsáveis**:
   - Mantenha as equipes informadas sobre o status dos gastos e orçamentos.
   - Promova uma cultura de responsabilidade financeira e uso consciente dos recursos.

8. **Atualizar a Política de Tags e Governança**:
   - Revise a política de tags periodicamente para garantir que ela atenda às necessidades atuais da organização.
   - Treine novas equipes ou membros sobre a importância e a aplicação correta das tags.

9. **Automatizar Alertas e Ações**:
   - Considere a configuração de alertas adicionais via **Amazon CloudWatch** para monitorar métricas específicas.
   - Use scripts ou **AWS Lambda** para automatizar ações corretivas quando certos limites forem atingidos.

10. **Auditar Configurações de Segurança e Compliance**:
    - Verifique se não há recursos expostos que possam gerar custos devido a uso indevido.
    - Utilize o **AWS Trusted Advisor** e o **AWS Security Hub** para identificar vulnerabilidades.

11. **Documentar e Revisar Processos**:
    - Mantenha a documentação atualizada sobre procedimentos de gestão de custos e governança.
    - Realize revisões regulares dos processos para identificar melhorias potenciais.

12. **Planejar para Eventos Futuros**:
    - Considere lançamentos de novos projetos, campanhas ou eventos sazonais que possam aumentar o uso de recursos.
    - Ajuste orçamentos e recursos antecipadamente para acomodar aumentos previstos.

13. **Utilizar Relatórios Detalhados**:
    - Configure o **AWS Cost and Usage Report** para obter dados detalhados de uso e custo.
    - Analise esses relatórios para insights aprofundados e para identificar áreas de otimização.

14. **Verificar Limites de Serviço**:
    - Monitore os limites de serviço (quotas) para evitar interrupções inesperadas ou custos adicionais.
    - Solicite aumentos de limite antecipadamente, se necessário.

15. **Implementar Políticas de Encerramento Automático**:
    - Configure políticas para encerrar automaticamente recursos não utilizados após um período definido.
    - Utilize tags como `ExpirationDate` ou `AutoDelete` para auxiliar nesse processo.

Seguindo este checklist regularmente, você estará melhor preparado para evitar surpresas no final do mês e manter os custos da AWS sob controle. A gestão proativa e contínua é essencial para uma operação financeira saudável e para o sucesso dos seus projetos na nuvem.

1) Verificar Frankfurt para ver quanto vai reduzir os custos! (removemos RDS e EC2)

2) Paris deletamos TUDO, lambda, ec2, rds e vpc

