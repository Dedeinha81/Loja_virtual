 
# Rotas para cadastro e login de usuários

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from schemas import UsuarioCreate, UsuarioResponse
from utils import hash_senha, verificar_senha, criar_token

# Criando o roteador
router = APIRouter()

# Função para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota de cadastro de usuário
@router.post("/cadastrar", response_model=UsuarioResponse)
def cadastrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Verifica se o email já existe
    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    # Cria o usuário com senha hash
    novo_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=hash_senha(usuario.senha)
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

# Rota de login
@router.post("/login")
def login_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Busca usuário pelo email
    db_usuario = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if not db_usuario:
        raise HTTPException(status_code=400, detail="Email não cadastrado")
    
    # Verifica a senha
    if not verificar_senha(usuario.senha, db_usuario.senha):
        raise HTTPException(status_code=400, detail="Senha incorreta")
    
    # Cria token JWT
    token = criar_token({"usuario_id": db_usuario.id})
    return {"access_token": token, "token_type": "bearer"}
