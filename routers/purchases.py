from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from config.db import engine
from models.user import users
from models.purchases import purchases

purchase = APIRouter()

#@purchase.get("/users/{id}")
#def read_user_purchases(id: int):
#    with Session(engine) as session:
#        user = session.query(users).join(prods).order_by(users.c.id).filter(users.id == id, prods.condition).first()
#        if not user:
#            raise HTTPException(status_code=404, detail="User not found")
#        return list(user)
    
@purchase.get("/users/{id}/purchases")
def read_user_purchases(id: int):
    with Session(engine) as session:
        user = session.query(users).filter(users.c.id == id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        user_purchases = session.query(purchases).join(users, users.c.id == purchases.c.user_id).filter(users.c.id == id).all()
        return [purchase.to_dict() for purchase in user_purchases]
    




      