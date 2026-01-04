import os

from pydantic.v1 import BaseSettings

MONGO_URI = os.getenv("MONGO_URI", "mongodb://root:MongoDB2019!@localhost:27017/test?authSource=admin&directConnection=true&tls=false&serverSelectionTimeoutMS=1000&connectTimeoutMS=1000&socketTimeoutMS=1000")
DATABASE_NAME = os.getenv("DATABASE_NAME", "users_db")

class Settings(BaseSettings):
    order_service_url: str = os.getenv("ORDER_SERVICE_URL", "http://localhost:8081")
    payment_service_url: str = os.getenv("PAYMENT_SERVICE_URL", "http://localhost:8082")

settings = Settings()
