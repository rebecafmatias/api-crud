from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schema import ProductCreate, ProductUpdate, ProductResponse
from typing import List
from crud import create_product, get_all_products, get_product_by_id, update_product, delete_product

router = APIRouter()

# Creating a route to select all products

@router.get("/products/", response_model=List[ProductResponse])
def read_products(db: Session = Depends(get_db)):
    products = get_all_products(db)
    return products
 
# Creating a route to select a product by ID

@router.get("/products/{product_id}", response_model=ProductResponse)
def read_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Creating a route to add a new product

@router.post("/products/", response_model=ProductResponse)
def create_new_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = create_product(db, product)
    return db_product

# Creating a route to update a product by ID

@router.put("/products/{product_id}", response_model=ProductResponse)
def update_prduct_by_id(product_id: int, product_update: ProductUpdate, db: Session = Depends(get_db)):
    product = update_product(db, product_id, product_update)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
# Creating a route to delete a product by ID

@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product_by_id(product_id: int, db: Session = Depends(get_db)):
    product = delete_product(db, product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product