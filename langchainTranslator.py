
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
open_api_sk = os.getenv("OPENAI_API_KEY")


# Lista de mensagem
mensagem =  [SystemMessage("Traduza esse texto para inglês"),HumamMessage("Andre Rocha")]

modelo = ChatOpenAI(model='gpt-4o-mini')