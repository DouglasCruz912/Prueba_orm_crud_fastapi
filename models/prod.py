from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine
from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.orm import relationship


prods = Table("poducts", meta, Column(
    "id", Integer, primary_key=True), 
    Column("prodName", String(255)),
    Column("precioProd", Integer))
    
meta.create_all(engine)