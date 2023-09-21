from typing import Optional
from pydantic import BaseModel
from sqlalchemy import inspect
from datetime import date

class Purchases(BaseModel):
    id: Optional[int] = None
    user_id: int
    product_id: int
    price: int
    quantity: int
    date: date

    def to_dict(self):
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}