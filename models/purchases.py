from sqlalchemy import ForeignKey, Table, Column
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine
from sqlalchemy.orm import relationship



purchases = Table("purchases", meta, Column(
    "id", Integer, primary_key=True),
    Column("user_id", Integer,ForeignKey('users.id')),
    Column("product_id", Integer, ForeignKey('products.id')),
    Column("price", Integer),
    Column("quantity", Integer),
    Column("date", Date))
    
user = relationship("User", back_populates="users")
products = relationship("Product", back_populates="products")
 
meta.create_all(engine)