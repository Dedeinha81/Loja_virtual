 
# Esquemas Pydantic para validação de dados

from pydantic import BaseModel
from typing import List, Optional

# Usuário
class UsuarioBase(BaseModel):
    nome: str
    email: str

class UsuarioCreate(UsuarioBase):
    senha: str

class UsuarioResponse(UsuarioBase):
    id: int
    class Config:
        orm_mode = True

# Produto
class ProdutoBase(BaseModel):
    nome: str
    descricao: str
    preco: float
    estoque: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int
    class Config:
        orm_mode = True

# Item do pedido
class ItemPedidoBase(BaseModel):
    produto_id: int
    quantidade: int

class ItemPedidoResponse(ItemPedidoBase):
    id: int
    class Config:
        orm_mode = True

# Pedido
class PedidoResponse(BaseModel):
    id: int
    usuario_id: int
    itens: List[ItemPedidoResponse] = []
    class Config:
        orm_mode = True
