
# Bibiliotecas
from dotenv import load_dotenv
import os
## Importar funções para receber e enviar mensagem
from langchain_core.messages import SystemMessage, HumanMessage

## Parser, pegar a resposta e transformar em texto
from langchain_core.output_parsers import StrOutputParser

## Importar modelo para o chat openAi
from langchain_openai import ChatOpenAI

## Importar templates para mensagem
from langchain_core.prompts import ChatPromptTemplate

#Executar função para poder chamar os valores posteriormente.
load_dotenv()

#Atribuir token
open_api_sk = os.getenv("OPENAI_API_KEY")
print(open_api_sk)

# Lista de mensagem
mensagem =  [SystemMessage("Traduza esse texto para inglês"),HumanMessage("Eu gosto de abacate")]

# Modelo Escoclhido
modelo = ChatOpenAI(model='gpt-4o')

# Retornar apenas resposta e não outros metadatas
parser = StrOutputParser()

# Determinando variáveis
idioma = 'Inglês'
texto = 'Quero aprender inglês'

# Criar um template para mensagem
template_mensagem = ChatPromptTemplate.from_messages([("system", "Traduza o texto para {idioma}"),("user", "Quero traduzir: {texto}"),])


# Usar chain para processamento
chain = template_mensagem | modelo | parser

# Invokar cadeia de execuções
texto = chain.invoke({"idioma":idioma, "texto":texto})

# Exibir retorno
print(texto)