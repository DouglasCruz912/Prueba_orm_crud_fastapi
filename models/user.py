from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import *
from config.db import meta, engine
from sqlalchemy.orm import relationship

users = Table("users", meta, Column(
    "id", Integer, primary_key=True), 
    Column("name", String(255)), 
    Column("email", String(255)))

meta.create_all(engine)
