"""AG2 (formerly AutoGen) — Exemplo multi-agente com GroupChat

Demonstra colaboração entre agentes especializados usando AG2 0.11+
com Ollama para inferência local. Três agentes (pesquisador, escritor
e crítico) trabalham juntos para produzir conteúdo educativo.

Requisitos:
    pip install "ag2[openai]>=0.11.0"
    ollama pull mistral
"""

import os

from autogen import ConversableAgent, LLMConfig
from autogen.agentchat import initiate_group_chat
from autogen.agentchat.group.patterns import AutoPattern

# Configuração do LLM — Ollama local (compatível com API OpenAI)
llm_config = LLMConfig(
    {
        "model": os.getenv("LLM_MODEL", "mistral"),
        "base_url": os.getenv(
            "OLLAMA_BASE_URL", "http://localhost:11434/v1"
        ),
        "api_key": "ollama",
    }
)

# --- Agentes especializados ---

pesquisador = ConversableAgent(
    name="pesquisador",
    system_message=(
        "Você é um pesquisador especializado. Seu trabalho é "
        "investigar tópicos em profundidade, encontrar dados "
        "relevantes e apresentar informações verificáveis. "
        "Forneça dados concretos e exemplos reais quando "
        "possível."
    ),
    llm_config=llm_config,
)

escritor = ConversableAgent(
    name="escritor",
    system_message=(
        "Você é um escritor criativo e didático. Seu trabalho "
        "é transformar informações técnicas em conteúdo "
        "acessível e envolvente para estudantes do ensino "
        "médio. Use analogias e exemplos do cotidiano. "
        "Organize o conteúdo com títulos e subtítulos claros."
    ),
    llm_config=llm_config,
)

critico = ConversableAgent(
    name="critico",
    system_message=(
        "Você é um crítico construtivo e revisor de qualidade. "
        "Analise o conteúdo gerado pelos outros agentes: "
        "verifique a precisão das informações, a clareza da "
        "linguagem e a adequação ao público-alvo (estudantes "
        "do ensino médio). Sugira melhorias específicas."
    ),
    llm_config=llm_config,
)

# Agente usuário (automático, sem interação humana)
usuario = ConversableAgent(
    name="usuario", human_input_mode="NEVER"
)

# --- Configuração do GroupChat com AutoPattern ---
# AutoPattern usa um gerenciador com LLM para decidir qual agente
# fala a seguir, permitindo colaboração flexível entre os agentes.

pattern = AutoPattern(
    initial_agent=pesquisador,
    agents=[pesquisador, escritor, critico],
    user_agent=usuario,
    group_manager_args={"llm_config": llm_config},
)

# --- Execução ---

if __name__ == "__main__":
    print("=" * 60)
    print("AG2 (formerly AutoGen) — GroupChat Multi-Agente")
    print("Modelo:", os.getenv("LLM_MODEL", "mistral"))
    print("=" * 60)

    resultado, contexto, ultimo_agente = initiate_group_chat(
        pattern=pattern,
        messages=(
            "Explique o conceito de energia renovável para "
            "estudantes do ensino médio, incluindo os "
            "principais tipos (solar, eólica, hidrelétrica) "
            "e sua importância para o futuro sustentável do "
            "planeta."
        ),
        max_rounds=10,
    )

    print("\n" + "=" * 60)
    print(f"Último agente: {ultimo_agente.name}")
    print("Conversa finalizada.")
