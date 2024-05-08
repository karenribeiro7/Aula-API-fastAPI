from uuid import UUID
from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [ #criando o objeto do banco de dados
    User(
        id=UUID("b3378384-7927-4442-9911-17594374e2f1"), #id do usuário do tipo UUID, que é um id único universal gerado randomicamente pela função uuid4() do módulo uuid
        first_name="Karen", 
        last_name="Ribeiro", 
        email="karen@email.com", 
        role=[Role.role_1]
    ),
    User(
        id=UUID("bd7c3216-9828-401a-8743-b39467c21955"),
        first_name="Ana", 
        last_name="Silva", 
        email="ana@email.com",
        role = [Role.role_2]
    ),
    User(
        id=UUID("9b9282a9-0d3f-4bfb-b6de-26edfe942af1"),
        first_name="Maria",
        last_name="Vieira",
        email="maria@email.com",
        role = [Role.role_3]
    )
] 

@app.get("/")
async def root():
    return {"message": "Olá mundo!"}

@app.get("/api/users/")
async def get_users():
    return db

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
    return {"message": "Usuário não encontrado!"}

@app.post("/api/users")
async def add_user(user: User):
    """
    Adiciona um usuário ao banco de dados.
    - **user**: objeto do tipo User, que contém as informações do usuário a ser adicionado.
    - **id**: id do usuário, gerado automaticamente. string.
    - **first_name**: primeiro nome do usuário. string.
    - **last_name**: sobrenome do usuário. string.
    - **email**: email do usuário. string.
    - **role**: lista de roles do usuário. Role.
    """
    db.append(user)
    return {"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return {"message": "Usuário removido com sucesso!"}
    raise HTTPException(status_code=404, detail=f"Usuário de id {id} não encontrado!")