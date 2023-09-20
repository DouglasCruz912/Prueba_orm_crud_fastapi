from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine
from sqlalchemy import Table, Column



prods = Table("products", meta, Column(
    "id", Integer, primary_key=True), 
    Column("prodName", String(255)),
    Column("prodPrice", Integer))
    
meta.create_all(engine)