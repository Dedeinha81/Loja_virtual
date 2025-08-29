# 🛒 Loja Virtual 

API feita em **Python** com **FastAPI** para cadastro de usuários, produtos e pedidos.  
Projeto desenvolvido como **portfólio**, mostrando minhas habilidades em back-end e APIs REST.

---

## 🚀 Tecnologias usadas

- 🐍 Python 3.11+  
- ⚡ FastAPI  
- 💾 SQLite  
- 🛠 SQLAlchemy  
- 🔑 JWT  
- 🔐 Passlib

---

## ✨ Funcionalidades principais

- 👤 **Usuários**: cadastro e login com autenticação JWT  
- 🛍 **Produtos**: criar, listar, atualizar e deletar produtos  
- 🧾 **Pedidos**: criar pedidos com múltiplos produtos e listar pedidos  

---

## 📂 Estrutura do projeto

loja_virtual/
│
├─ main.py # Inicializa a API

├─ database.py # Configuração do banco SQLite

├─ models.py # Modelos do banco

├─ schemas.py # Schemas para validação

├─ utils.py # Funções auxiliares

├─ routes/ # Rotas separadas por módulo

│ ├─ init.py

│ ├─ usuarios.py

│ ├─ produtos.py

│ └─ pedidos.py

└─ requirements.txt # Dependências do projeto

---

## 🏁 Como rodar o projeto (Windows)

1. Abra o terminal e vá para a pasta do projeto:

 cd C:\Loja_virtual

---

2. Instale as dependências:

 pip install -r requirements.txt

---

3. Rode a API:

uvicorn main:app --reload --host 127.0.0.1 --port 8080

---

> ⚡ A API vai rodar em `http://127.0.0.1:8080`

4. Abra o **Swagger** para testar todas as rotas:

---

## 💡 Exemplos de rotas

### 👤 Cadastrar usuário

POST /usuarios/cadastrar
{

"nome": "Andrea",

"email": "andrea@email.com
",

"senha": "123456"
}

---

### 🔑 Login

POST /usuarios/login
{

"nome": "Andrea",

"email": "andrea@email.com
",

"senha": "123456"
}

---

### 🛍 Criar produto

POST /produtos/
{

"nome": "Camiseta",

"descricao": "Camiseta preta básica",

"preco": 49.90,

"estoque": 10
}

---

### 🧾 Criar pedido

POST /pedidos/
{

"usuario_id": 1,

"itens": [
{

"produto_id": 1,

"quantidade": 2
}
]
}

---

## ⚠️ Observações

- O banco **SQLite** é criado automaticamente (`loja_virtual.db`)  
- Todas as rotas estão disponíveis no **Swagger**  

---

## 👩‍💻 Sobre mim

Sou **Andrea**, estudante de programação e apaixonada por **desenvolvimento back-end**.  
Este projeto é meu **portfólio**, mostrando minhas habilidades em **Python, FastAPI e APIs REST**.


