from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine


purchases = Table("purchases", meta, Column(
    "id", Integer, primary_key=True),
    Column("user_id", Integer),
    Column("product_id", Integer),
    Column("price", Integer),
    Column("quantity", Integer),
    Column("date", Date))
 
meta.create_all(engine)