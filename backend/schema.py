from pydantic import BaseModel, PositiveFloat, EmailStr
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: PositiveFloat
    category: Optional[str] = None
    supplier_email: EmailStr

class ProductCreate(ProductBase):
    pass