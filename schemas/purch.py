from typing import Optional
from pydantic import BaseModel


class Compra(BaseModel):
    id: Optional[int] = None
    user_id: int
    product_id: int


