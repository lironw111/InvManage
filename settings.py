import pydantic

__all__ = ("mongo_settings",)


class MongoSettings(pydantic.BaseSettings):
    uri: str = "mongodb://mongo:27017/"
    database: str = "Storage"
    collection: str = "products"


mongo_settings = MongoSettings()
