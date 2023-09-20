from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from config.db import engine
from models.user import users

purchase = APIRouter()

@purchase.get("/users/{user_id}/purchases")
def read_user_purchases(user_id: int):
    with Session(engine) as session:
        user = session.query(users).filter(users.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return {"purchases": [purchase.product.id for purchase in user.purchases]}