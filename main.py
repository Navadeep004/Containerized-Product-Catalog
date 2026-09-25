import os

from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI(title="Product Catalog API")

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

client = MongoClient(MONGO_URL)
db = client["product_catalog"]
products_collection = db["products"]


@app.get("/health")
def health():
    try:
        client.admin.command("ping")
        return {"status": "healthy", "database": "connected"}
    except Exception:
        return {"status": "unhealthy", "database": "disconnected"}


@app.get("/products")
def get_products():
    products = list(products_collection.find({}, {"_id": 0}))

    if not products:
        return [
            {"id": 1, "name": "Laptop", "price": 65000},
            {"id": 2, "name": "Mouse", "price": 800},
            {"id": 3, "name": "Keyboard", "price": 1500}
        ]

    return products