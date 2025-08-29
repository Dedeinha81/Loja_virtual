 
# Conexão com o banco de dados SQLite (teste rápido, sem MySQL)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configurações do banco SQLite
DATABASE_URL = "sqlite:///./loja_virtual.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # necessário para SQLite
    echo=True,
    future=True
)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

# Função para criar as tabelas no banco
def criar_banco():
    Base.metadata.create_all(bind=engine)
