# 02-frameworks

Esta pasta contém exemplos práticos de diferentes frameworks para desenvolvimento de agentes de IA, demonstrando como construir sistemas multi-agente usando ferramentas populares.

## 📁 Arquivos

### `agno_starter.py`
Exemplo usando o framework **Agno** para análise de notícias do HackerNews.

**Características:**
- Agente especializado em análise de conteúdo técnico
- Integração com HackerNews API
- Modelo Ollama local (Mistral)
- Interface interativa via linha de comando

**Funcionalidades:**
- Análise de tendências no HackerNews
- Insights sobre engajamento de usuários
- Identificação de tópicos em discussão
- Contexto da indústria de tecnologia

### `autoge_starter.py`
Demonstração do framework **AutoGen** com colaboração multi-agente.

**Características:**
- Sistema com múltiplos agentes especializados:
  - **Pesquisador**: Coleta informações e fatos
  - **Escritor**: Transforma pesquisa em conteúdo envolvente
  - **Crítico**: Revisa e sugere melhorias
- Chat em grupo com gerenciamento automático
- Uso do Ollama localmente (sem necessidade de APIs pagas)

**Fluxo de trabalho:**
1. Pesquisador coleta dados sobre energias renováveis
2. Escritor cria explicação para estudantes
3. Crítico revisa e sugere melhorias
4. Processo iterativo até resultado satisfatório

### `ag2_starter.py`
Demonstração do framework **AG2** (formerly AutoGen) com colaboração multi-agente.

**Características:**
- Sistema com múltiplos agentes especializados:
  - **Pesquisador**: Coleta informações e fatos
  - **Escritor**: Transforma pesquisa em conteúdo envolvente
  - **Crítico**: Revisa e sugere melhorias
- API moderna AG2 0.11+ (`LLMConfig`, `ConversableAgent`, `initiate_group_chat`)
- Orquestração via `AutoPattern` com seleção inteligente de agentes
- Uso do Ollama localmente (sem necessidade de APIs pagas)

**Execução:**
```bash
pip install "ag2[openai]>=0.11.0"
ollama pull mistral
python ag2_starter.py
```

**Quando usar AG2:**
- Projetos que precisam de colaboração multi-agente com orquestração
  flexível
- Casos que requerem handoffs inteligentes entre agentes
  especializados
- Integração com ferramentas via MCP (Model Context Protocol)

### `crewai_starter.py`
Exemplo do framework **CrewAI** para geração de conteúdo LinkedIn.

**Características:**
- Agente especializado em criação de conteúdo
- Foco em posts para profissionais de IA
- Modelo Ollama local
- Processo sequencial de execução

**Uso:**
- Gera posts profissionais para LinkedIn
- Conteúdo otimizado para público de IA
- Inclui call-to-action apropriado

### `langchain_langgraph_starter.py`
Sistema multi-agente usando **LangChain + LangGraph**.

**Características:**
- Três agentes especializados:
  - **Classifier**: Categorização de textos
  - **Keywords**: Extração de palavras-chave
  - **Summarizer**: Criação de resumos
- Fluxo de trabalho em grafo
- Visualização do pipeline
- Estado compartilhado entre agentes

**Funcionalidades:**
- Análise colaborativa de textos
- Pipeline visual de processamento
- Geração de gráfico PNG do workflow
- Análise especializada em etapas

## 🚀 Como usar

### Pré-requisitos

1. **Instalar Ollama**:
```bash
# Baixar e instalar: https://ollama.ai
ollama serve
ollama pull mistral:latest
```

2. **Instalar dependências**:
```bash
pip install -r requirements.txt
```

### Executar os exemplos

```bash
# Agno - Análise HackerNews
python agno_starter.py

# AutoGen - Colaboração multi-agente
python autoge_starter.py

# AG2 - Colaboração multi-agente (API moderna)
python ag2_starter.py

# CrewAI - Conteúdo LinkedIn
python crewai_starter.py

# LangChain/LangGraph - Pipeline de análise
python langchain_langgraph_starter.py
```

## 🔧 Configuração

Todos os exemplos estão configurados para usar **Ollama localmente**, não requerendo chaves de API externas.

**URL padrão do Ollama**: `http://localhost:11434`
**Modelo recomendado**: `mistral:latest`

## 📝 Conceitos Demonstrados

- **Multi-agent systems**: Diferentes agentes trabalhando em conjunto
- **Especialização de papéis**: Cada agente tem uma função específica
- **Comunicação entre agentes**: Troca de informações e colaboração
- **Fluxos de trabalho**: Sequências organizadas de tarefas
- **Estado compartilhado**: Memória comum entre agentes
- **Integração com ferramentas externas**: APIs e serviços
- **Processamento local**: Sem dependência de APIs pagas

## 💡 Quando usar cada framework

- **Agno**: Análise de dados e integração com APIs específicas
- **AutoGen**: Colaboração complexa entre múltiplos agentes
- **AG2**: Fork comunitário do AutoGen com orquestração inteligente e API moderna
- **CrewAI**: Workflows estruturados com papéis bem definidos
- **LangChain/LangGraph**: Pipelines complexos com visualização e controle de fluxo

## 🎯 Próximos passos

Explore os outros módulos do workshop:
- `03-prompt-engineering/`: Técnicas de otimização de prompts
- `04-RAG/`: Retrieval-Augmented Generation
- `05-memory/`: Sistemas de memória para agentes
- `06-MCP-A2A/`: Model Context Protocol Agent-to-Agent