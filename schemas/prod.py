from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    id: Optional[int] = None
    prodName: str
    prodPrice: int

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}