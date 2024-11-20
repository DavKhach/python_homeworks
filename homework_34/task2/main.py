from fastapi import FastAPI, HTTPException


app = FastAPI()

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
        ]

products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500}
           ]


@app.get("/users")
async def get_users():
    return users


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/users")
async def create_user(user: dict):
    user["id"] = max(u["id"] for u in users) + 1
    users.append(user)
    return user


@app.put("/users/{user_id}")
async def update_user(user_id: int, updated_user: dict):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user.update(updated_user)
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        users.remove(user)
        return {"detail": "User deleted"}
    else:
        raise HTTPException(status_code=404, detail="User not found")


@app.get("/products")
async def get_products():
    return products


@app.get("/products/{product_id}")
async def get_product(product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@app.post("/products")
async def create_product(product: dict):
    product["id"] = max(p["id"] for p in products) + 1
    products.append(product)
    return product


@app.put("/products/{product_id}")
async def update_product(product_id: int, updated_product: dict):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        product.update(updated_product)
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@app.delete("/products/{product_id}")
async def delete_product(product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        products.remove(product)
        return {"detail": "Product deleted"}
    else:
        raise HTTPException(status_code=404, detail="Product not found")
