from langserve import RemoteRunnable

chain_remote = RemoteRunnable("http://localhost:8000/tradutor")

idioma = "Italiano"
texto = "Eu sou programador de computador"

mensagem = chain_remote.invoke({"idioma_desejado":idioma, "texto":texto})
print(mensagem)
