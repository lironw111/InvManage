# methods to interact with the DB

from typing import List
from models import ProductRead
from models import ProductCreate
from database import *

__all__ = ("ProductRepository",)


class ProductRepository:
    @staticmethod
    def list() -> List[ProductRead]:
        """Retrieve all the available products"""
        return list(collection.find())

    @staticmethod
    def delete(product_name):
        """" Delete Product by name """
        if collection.delete_one({"name": product_name}).deleted_count:
            return 1
        else:
            return 0

    @staticmethod
    def create(create: ProductCreate):
        """" Create New Product """
        return collection.insert_one({"name": create.name, "description": create.description, "category": create.category, "quantity": create.quantity}).inserted_id

    @staticmethod
    def update(product_name: str, quantity: int):
        """" Update quantity to product  """
        return collection.update_one({"name": product_name}, {"$set": {'quantity': quantity}})







