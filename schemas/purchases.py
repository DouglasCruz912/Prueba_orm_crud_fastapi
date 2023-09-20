from typing import Optional
from pydantic import BaseModel


class Purchases(BaseModel):
    id: Optional[int] = None
    user_id: int
    product_id: int


