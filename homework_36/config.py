import os
from typing import Optional
from dotenv import load_dotenv


load_dotenv()

class Config:
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.init_env()
        return cls.__instance

    def init_env(self):
        self.PORT = self.get_env("PORT", cast=int)
        self.FILE_PATH = self.get_env("FILE_PATH").split(",")
        self.SECRET_KEY = self.get_env("SECRET_KEY")

    def get_env(self, key: str, cast: Optional[type] = None):
        value = os.getenv(key)
        if not value:
            raise ValueError(f"Env does not have specified key: {key}")
        if cast is not None:
            return cast(value)
        return value