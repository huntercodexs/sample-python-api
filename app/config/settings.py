import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb://admin:admin123@localhost:27017/test?authSource=admin&directConnection=true&tls=false&serverSelectionTimeoutMS=1000&connectTimeoutMS=1000&socketTimeoutMS=1000")
DATABASE_NAME = os.getenv("DATABASE_NAME", "users_db")
