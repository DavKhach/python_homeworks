import os
from contextlib import asynccontextmanager

import uvicorn, aiofiles
from fastapi import FastAPI
from dotenv import load_dotenv

from auth import router as auth_router


load_dotenv()
USERS_FILE = os.getenv("USERS_File", "users.json")
TASKS_FILE = os.getenv("TASKS_FILE", "tasks.json")
PORT = int(os.getenv("PORT"))

async def init_files():
    for file in [USERS_FILE, TASKS_FILE]:
        if not os.path.exists(file):
            async with aiofiles.open(file, mode="w") as fs:
                await fs.write("[]")

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App is starting up...")
    await init_files()
    yield
    print("App is shutting down...")

app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "FastAPI is running..."}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=PORT)
