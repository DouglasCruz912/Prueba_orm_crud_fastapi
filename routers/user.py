from fastapi import APIRouter, status
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet
from starlette.status import *
from sqlalchemy.orm import Session
from config.db import engine


key = Fernet.generate_key()
f = Fernet(key)

user = APIRouter()


@user.get("/usersList", response_model=list[User])
async def get_users():
        with Session(engine) as session:
         return session.execute(users.select()).fetchall()


@user.post("/addUsers", response_model=User)
async def create_users(user: User):
    new_user = {"name": user.name, "email": user.email}
    #new_user["password"] = f.encrypt(user.password.encode("utf-8"))
    with Session(engine) as session:
        result = session.execute(users.insert().values(new_user))
        session.commit()
        return session.execute(users.select().where(users.c.id == result.lastrowid)).first()



@user.get("/usersList/{id}",response_model=User)
async def get_user(id: int):
        with Session(engine) as session:
            return session.execute(users.select().where(users.c.id == id)).first()


@user.delete("/deletUsers/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int):
    with Session(engine) as session:
        result = session.execute(users.delete().where(users.c.id == id))
        session.commit()
        return HTTP_204_NO_CONTENT


@user.put("/usersUpdate/{id}", response_model=User)
async def update_user(id: int, user: User):
    
    updated_user = {"name": user.name, "email": user.email}
    with Session(engine) as session:
        result = session.execute(users.update().values(updated_user).where(users.c.id == id))
        session.commit()
    return session.execute(users.select().where(users.c.id == id)).first()



