import os
from contextlib import asynccontextmanager

import uvicorn, aiofiles
from fastapi import FastAPI
from dotenv import load_dotenv

from config import Config
from auth import router as auth_router


load_dotenv()
config = Config()

async def init_files():
    for file in config.FILE_PATH:
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
    uvicorn.run("main:app", port=config.PORT, reload=True)
