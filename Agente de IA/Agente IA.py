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

# --- CONFIGURAÇÃO DA BARRA LATERAL (SIDEBAR) ---
with st.sidebar:

    st.title("🦧 Agente IA")
    st.markdown("Um assistente de IA focado em programação Python para ajudar iniciantes.")

    # Campo de entrada para a chave da API com máscara de senha
    groq_api_key = st.text_input(
        "Insira sua API Key Groq",
        type="password",
        help="Obtenha sua chave em: https://console.groq.com/keys"
    )

    st.markdown("---")
    st.markdown("Desenvolvido para auxiliar em suas dúvidas de programação com Linguagem Python.")

# --- INTERFACE PRINCIPAL ---
st.title("🦧 Agente IA")

st.title("🐍 Assistente Pessoal de Programação Python")

st.caption("Faça sua pergunta sobre Linguagem Python.")

# --- GERENCIAMENTO DE ESTADO DO CHAT ---
# Inicializa a lista de mensagens no st.session_state para que o histórico não suma ao recarregar a página
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens existentes no histórico de chat sempre que o app é atualizado
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
         st.markdown(message["content"])

# --- LÓGICA DO CLIENTE API ---
client = None

# Verifica se a chave foi inserida antes de tentar criar o cliente Groq, e trata erros de inicialização
if groq_api_key:
    try:
        # Tenta instanciar o cliente Groq com a chave fornecida
        client = Groq(api_key = groq_api_key)
    
    except Exception as e:
        # Exibe erro na barra lateral caso a inicialização falhe (ex: chave inválida)
        st.sidebar.error(f"Erro ao iniciar o cliente Groq: {e}")
        st.stop() # Interrompe a execução do script para evitar erros posteriores

# Aviso caso o usuário tente interagir sem ter colocado a chave
elif st.session_state.messages:
    st.warning("Por favorm insira a chave da sua API Groq na barra lateral para continuar.")

# Captura a entrada do usuário através do componente de chat input
if prompt := st.chat_input("Digite sua dúvida sobre programação Python aqui..."):

    # Verifica se o cliente Groq foi inicializado, se não, exibe aviso e para execução
    if not client:
        st.warning("Por favor, insira a chave da sua API Groq na barra lateral para continuar.")
        st.stop()

    # Armazena a mensagem do usuário no estado da sessão
    st.session_state.messages.append({"role":"user", "content":prompt})

    # Exibe a mensagem do usuário no chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepara o prompt completo para enviar à API, combinando o comportamento definido com a pergunta do usuário
    messages_for_api = [{"role":"system", "content":CUSTOM_PROMPT}]
    for msg in st.session_state.messages:
        messages_for_api.append(msg)

    # Cria a resposta do modelo usando a API da Groq, passando o prompt completo
    with st.chat_message("assistant"):
        # Exibe um indicador de que o modelo está "pensando" 
        with st.spinner("Analisando sua pergunta..."):
            try:
                # Chama a API da Groq para gerar a resposta do modelo
                chat_completion = client.chat.completions.create(
                    messages = messages_for_api,
                    model = "openai/gpt-oss-20b",
                    temperature = 0.7,
                    max_tokens = 2048
                )
            
                # Extrai a resposta gerada pela API
                response = chat_completion.choices[0].message.content

                # Exibe a resposta no Streamlit
                st.markdown(response)

                # Armazena a resposta do modelo no estado da sessão para manter o histórico
                st.session_state.messages.append({"role":"assistant", "content":response})

            # Trata erros que possam ocorrer durante a chamada à API e exibe mensagem de erro
            except Exception as e:
                st.error(f"Ocorreu um erro ao se comunicar com a API da Groq: {e}")