 
# Funções auxiliares para senha e JWT

from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

# Configurações de hash de senha
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str):
    return pwd_context.hash(senha)

def verificar_senha(senha: str, hash_senha_db: str):
    return pwd_context.verify(senha, hash_senha_db)

# Configurações JWT
SECRET_KEY = "SUA_CHAVE_SECRETA_SUPER_SEGURA"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def criar_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token

def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
