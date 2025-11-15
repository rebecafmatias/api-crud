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

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    supplier_email: Optional[EmailStr] = None

class ProductResponse(ProductBase):
    id: int

    class Config:
        orm_mode = True