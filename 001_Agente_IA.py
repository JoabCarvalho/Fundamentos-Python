import os

import streamlit as st

from groq import Groq

st.set_page_config(
    page_title="Agente IA",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

CUSTOM_PROMPT = """
Você é o "Agente Super Inteligente" um assistente de IA especialista em programação, com foco principal em Python.
Sua missão é ajudar desenvolvedores Python iniciais.

REGRAS DE OPERAÇÃO:
1.  ****
2.  ****
    * ****
    * ****
3.  ****
"""