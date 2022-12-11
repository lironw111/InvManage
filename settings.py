import pydantic

__all__ = ("mongo_settings",)


class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"


class MongoSettings(BaseSettings):
    uri: str = "mongodb://mongo:27017/"
    database: str = "Storage"
    collection: str = "products"

    class Config(BaseSettings.Config):
        env_prefix = "MONGO_"


mongo_settings = MongoSettings()
