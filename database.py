# This file defines the DB connection
from enum import unique

from settings import mongo_settings as settings
from pymongo import MongoClient
from pymongo.collection import Collection

__all__ = ("client", "collection")

client = MongoClient(settings.uri)
collection: Collection = client[settings.database][settings.collection]
#collection.create_index("name")
#collection.create_index('name', unique=True)
