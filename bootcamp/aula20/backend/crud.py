from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel


def get_product(db: Session, product_id: int):
    """
    funcao que recebe um id e retorna somente ele
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()


def get_products(db: Session):
    """
    funcao que retorna todos os elementos
    """
    return db.query(ProductModel).all()


def create_product(db: Session, product: ProductCreate):
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db: Session, product_id: int):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


def update_product(db: Session, product_id: int, product: ProductUpdate):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.categoria is not None:
        db_product.categoria = product.categoria
    if product.email_fornecedor is not None:
        db_product.email_fornecedor = product.email_fornecedor

    db.commit()
    return db_product
