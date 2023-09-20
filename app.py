from fastapi import FastAPI
from routers.user import user
from routers.prod import prod
from routers.purch import purchase

app = FastAPI()
    

app.include_router(user)
app.include_router(prod)
app.include_router(purchase)