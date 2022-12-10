from fastapi import FastAPI
import pymongo

app = FastAPI()

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Storage"]
col = db["products"]

mylist = [
  { "ID":1, "name": "iphone 14 pro", "description": "iphone 14 pro 256GB white", "category": "apple", "quantity":"20"},
  { "ID":2, "name": "Samsung Galaxy S20", "description": "Samsung Galaxy S20 128GB black", "category": "samsung", "quantity":"15"},
  { "ID":3, "name": "iphone 13 max", "description": "iphone 13 max 256GB black", "category": "apple", "quantity":"3"},
  { "ID":4, "name": "Xiaomi Redmi 9A", "description": "Xiaomi Redmi 9A 32GB gray", "category": "xiaomi", "quantity":"7"},
  { "ID":5, "name": "Xiaomi Poco X4", "description": "Xiaomi Poco X4 Pro 5G black", "category": "xiaomi", "quantity":"10"},
  { "ID":6, "name": "Samsung Galaxy S22", "description": "Samsung Galaxy S22 128GB white", "category": "samsung", "quantity":"4"},
  { "ID":7, "name": "Samsung Galaxy S22 Ultra", "description": "Samsung Galaxy S22 Ultra 12GB red", "category": "samsung", "quantity":"9"},
  { "ID":8, "name": "Apple iPhone 11 128GB", "description": "Apple iPhone 11 128GB black", "category": "apple", "quantity":"6"},
  { "ID":9, "name": "Asus ROG", "description": "Asus ROG Phone 6 16GB white", "category": "asus", "quantity":"8"},
  { "ID":10, "name": "Asus Zenfone 9", "description": "Asus Zenfone 9 8GB gray", "category": "sasus", "quantity":"10"}

]

x = col.insert_many(mylist)
