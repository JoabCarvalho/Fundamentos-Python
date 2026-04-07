# Importa o módulo para interagir com o SO
import os

# Importa a biblioteca Streamlit para criar a interface web interativa
import streamlit as st

# Importa a  classe Groq para se conectar à API da plataforma Groq e acessar o LLM
from groq import Groq

# Configura a página do Streamlit com título, ícone, layout e estado inicial da sidebar
st.set_page_config(
    page_title="Agente IA",
    page_icon="🦧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Definindo um PROMPT de comportamento e regras do Assistente de IA
CUSTOM_PROMPT = """
Você é o "Agente de IA, um assistente de IA especialista em programação, com foco principal em Python.
Sua missão é ajudar desenvolvedores iniciantes.

REGRAS DE OPERAÇÃO:
1.  **Foco em Programação**: Responda apenas a perguntas relacionadas em programação, algoritmos, estruturas de dados, bibliotecas e frameworks.
2.  **Estrutura da Resposta**: Formate sempre da seguinte maneira:
    * **Explicação Clara**: Começe com uma explicação conceitual breve, clara, de fácil entendimento sobre o assunto. Seja direto e didático.
    * **Exemplo de Código**: Forneça blocos de códigos em Python com sintaxe correta e precisa, muito bem comentado, explicando cada etapa.
    * **Detalhe do Código**: Após os códigos, descreva em detalhe o que cada parte do código faz.
    * **Documentação de Referência**: Forneça o link da documentação.
"""
with st.sidebar:

    st.title("🦧 Agente IA")
    st.markdown("Um assistente de IA focado em programação Python para ajudar iniciantes.")

    groq_api_key = st.text_input(
        "Insira sua API Key Groq",
        type="password",
        help="Obtenha sua chave em: https://console.groq.com/keys"
    )

    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação com Linguagem Python.")

st.title("🦧 Agente IA")

st.title("🐍 Assistente Pessoal de Programação Python")

st.caption("Faça sua pergunta sobre Linguagem Python.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with    st.chat_message(message["role"]):
            st.markdown(message["content"])

client = None

if groq_api_key:
    try:
        client = Groq(api_key = groq_api_key)
    
    except Exception as e:
        st.sidebar.error(f"Erro ao iniciar o cliente Groq: {e}!")
        st.stop()

elif st.session_state.messages:
    st.warning("Por favorm insira a chave da sua API Groq na barra lateral para continuar.")
