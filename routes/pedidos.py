 
# Rotas para criar pedidos e gerenciar carrinho

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Pedido, ItemPedido, Produto
from schemas import ItemPedidoBase, PedidoResponse
from typing import List

# Criando o roteador
router = APIRouter()

# Função para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para criar um pedido
@router.post("/", response_model=PedidoResponse)
def criar_pedido(usuario_id: int, itens: List[ItemPedidoBase], db: Session = Depends(get_db)):
    # Cria o pedido
    novo_pedido = Pedido(usuario_id=usuario_id)
    db.add(novo_pedido)
    db.commit()
    db.refresh(novo_pedido)
    
    # Adiciona os itens ao pedido
    for item in itens:
        produto = db.query(Produto).filter(Produto.id == item.produto_id).first()
        if not produto:
            raise HTTPException(status_code=404, detail=f"Produto {item.produto_id} não encontrado")
        if produto.estoque < item.quantidade:
            raise HTTPException(status_code=400, detail=f"Estoque insuficiente para {produto.nome}")
        
        novo_item = ItemPedido(
            pedido_id=novo_pedido.id,
            produto_id=item.produto_id,
            quantidade=item.quantidade
        )
        produto.estoque -= item.quantidade  # Atualiza estoque
        db.add(novo_item)
    
    db.commit()
    db.refresh(novo_pedido)
    return novo_pedido

# Rota para listar pedidos de um usuário
@router.get("/usuario/{usuario_id}", response_model=List[PedidoResponse])
def listar_pedidos_usuario(usuario_id: int, db: Session = Depends(get_db)):
    pedidos = db.query(Pedido).filter(Pedido.usuario_id == usuario_id).all()
    return pedidos
