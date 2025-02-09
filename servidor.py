from langchainTranslator import chain
from fastapi import FastAPI
from langserve import add_routes


# Criação da aplicação através da função do FastAPI
app = FastAPI(title="Meu APP de IA", description="Traduza textos de qualquer língua.")

# Adicionar rota e endpoint para o servidor
add_routes(app, chain, path="/tradutor")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)