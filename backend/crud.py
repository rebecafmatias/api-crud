from sqlalchemy.orm import Session
from schema import ProductUpdate, ProductCreate
from models import ProductModel

# Function to get all products
def get_all_products(db: Session):
    return db.query(ProductModel).all()

# Function to get a product by ID
def get_product_by_id(db: Session, product_id: int):
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

# Function to create a new product
def create_product(db: Session, product: ProductCreate):
    # Transforming Pydantic model to SQLAlchemy model
    db_product = ProductModel(**product.model_dump())
    # Adding and committing the new product to the database
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Function to delete a product by ID
def delete_product(db: Session, product_id: int):  
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

# Function to update an existing product
def update_product(db: Session, product_id: int, product_update: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product:
        # Updating fields of the product
        for key, value in product_update.model_dump(exclude_unset=True).items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product 
