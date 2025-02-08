
# Bibiliotecas
from dotenv import load_dotenv
import os
## Importar funções para receber e enviar mensagem
from langchain_core.messages import SystemMessage, HumanMessage
## Importar modelo para o chat openAi
from langchain_openai import ChatOpenAI

#Executar função para poder chamar os valores posteriormente.
load_dotenv()

#Atribuir token
OPENAI_API_KEY = "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"


# Lista de mensagem
mensagem =  [SystemMessage("Traduza esse texto para inglês"),HumanMessage("Andre Rocha")]
modelo = ChatOpenAI(model='gpt-4o-mini')
resposta = modelo.invoke(mensagem)
print(modelo)