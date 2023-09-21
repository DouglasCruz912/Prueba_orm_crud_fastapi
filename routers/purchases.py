from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from config.db import engine
from models.user import users
from models.purchases import purchases
from schemas.purchases import Purchases

purchase = APIRouter()

#@purchase.get("/users/{id}")
#def read_user_purchases(id: int):
#    with Session(engine) as session:
#        user = session.query(users).join(prods).order_by(users.c.id).filter(users.id == id, prods.condition).first()
#        if not user:
#            raise HTTPException(status_code=404, detail="User not found")
#        return list(user)
    
@purchase.get("/purchases", response_model=list[Purchases])
def read_user_purchases(id: int):
        with Session(engine) as session:
         return session.execute(purchases.select()).fetchall()
    

