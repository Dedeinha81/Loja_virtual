 
# Ponto de entrada da aplicação FastAPI

from fastapi import FastAPI
from database import criar_banco
from routes import usuarios, produtos, pedidos

# Criando a aplicação FastAPI
app = FastAPI(
    title="Loja Virtual",
    description="API simples de e-commerce com usuários, produtos e pedidos",
    version="1.0.0"
)

# Criando as tabelas no banco ao iniciar o sistema
criar_banco()

# Registrando as rotas
app.include_router(usuarios.router, prefix="/usuarios", tags=["Usuários"])
app.include_router(produtos.router, prefix="/produtos", tags=["Produtos"])
app.include_router(pedidos.router, prefix="/pedidos", tags=["Pedidos"])

# Rota inicial de teste
@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à Loja Virtual!"}