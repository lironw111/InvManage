from pydantic import BaseModel, Field

__all__ = ("ProductCreate",)


class ProductCreate(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    category: str = Field(...)
    quantity: int = Field(...)
