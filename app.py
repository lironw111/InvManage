# FastAPI app definition, initialization and definition of routes #


import uvicorn
from fastapi import FastAPI, HTTPException
from models import *
from repository import ProductRepository
from fastapi.responses import RedirectResponse


__all__ = ("app", "run")


app = FastAPI()


"""@app.get('/')
def hello():
    return RedirectResponse(url='/docs')"""


@app.get("/product", response_model=list[ProductRead], description="List all the available products")
def _list_product():
    try:
        return ProductRepository.list()
    except:
        raise HTTPException(status_code=500, detail="Internal server error: Unable to get list of products")


@app.delete("/product/{product_name}", description="Delete a single product by its name")
def _delete_product(product_name):
    try:
        if ProductRepository.delete(product_name):
            return "Product deleted"
        else:
            return "Unable to delete product. Maybe it doesn't exist "
    except:
        raise HTTPException(status_code=404, detail="Couldn't delete product")


@app.post("/product/add", description="Create new Product")
def _create_product(create: ProductCreate):
    try:
        ProductRepository.create(create)
        return "Product Created"
    except:
        raise HTTPException(status_code=404, detail="Couldn't create product")


@app.patch("/product/{name}", description="Update a single product quantity")
def _update_quantity(name, quantity: int):
    try:
        if quantity > 0:
            ProductRepository.update(name, quantity)
            return "Quantity updated"
        else:
            return "Quantity must be number greater than zero"
    except:
        raise HTTPException(status_code=404, detail="Can't update quantity")


#def run():
  #  """Run the API using Uvicorn"""
  #  uvicorn.run(app)

