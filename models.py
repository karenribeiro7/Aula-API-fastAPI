#Esqueleto básico da modelagem de dados

from pydantic import BaseModel #importar a classe base
from uuid import UUID, uuid4 #gerar id's randomicos
from typing import Optional, List #listar os tipos de roles
from enum import Enum #enumerar os tipos de roles

class Role(str, Enum):
    role_1 = "admin"
    role_2 = "aluna"
    role_3 = "instrutora"

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    last_name: str
    email: str
    role: List[Role]