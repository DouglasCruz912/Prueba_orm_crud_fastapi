from typing import Optional
from pydantic import BaseModel


class Product(BaseModel):
    id: Optional[int] = None
    prodName: str
    prodPrice: int