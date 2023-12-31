from fastapi import APIRouter, status
from config.db import conn
from models.prod import prods
from schemas.prod import Product
from cryptography.fernet import Fernet
from starlette.status import *
from sqlalchemy.orm import Session
from config.db import engine


key = Fernet.generate_key()
f = Fernet(key)

prod = APIRouter()


@prod.get("/products", response_model=list[Product])
async def get_prods():
        with Session(engine) as session:
         return session.execute(prods.select()).fetchall()


@prod.post("/products", response_model=Product)
async def create_prods(prod: Product):
    new_prod = {"prodName": prod.prodName, "prodPrice": prod.prodPrice}
    with Session(engine) as session:
        result = session.execute(prods.insert().values(new_prod))
        session.commit()
        return session.execute(prods.select().where(prods.c.id == result.lastrowid)).first()



@prod.get("/products/{id}",response_model=Product)
async def get_prods(id: int):
        with Session(engine) as session:
            return session.execute(prods.select().where(prods.c.id == id)).first()


@prod.delete("/products/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_prods(id: int):
    with Session(engine) as session:
        result = session.execute(prods.delete().where(prods.c.id == id))
        session.commit()
        return HTTP_204_NO_CONTENT


@prod.put("/products/{id}", response_model=Product)
async def update_prods(id: int, prod: Product):
    
    updated_prod = {"prodName": prod.prodName, "prodPrice": prod.prodPrice}
    with Session(engine) as session:
        result = session.execute(prods.update().values(updated_prod).where(prods.c.id == id))
        session.commit()
    return session.execute(prods.select().where(prods.c.id == id)).first()