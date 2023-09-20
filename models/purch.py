from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine
from sqlalchemy.orm import relationship

purch = Table("purchases", meta, Column(
    "id", Integer, primary_key=True), 
    Column("user_id", Integer, ForeignKey("users.id")), 
    Column("product_id", Integer, ForeignKey("products.id")))

user = relationship("User", back_populates="purchases")
product = relationship("Product", back_populates="purchases")

meta.create_all(engine)