from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    username: str = Field(...)
    email: EmailStr
    password: str = Field(...)

class Movie(BaseModel):
    title: str = Optional
    genre: str = Optional
    rating: float = Field(..., ge=1, le=10)

class Rental(BaseModel):
    user: str = Field(...)
    movie: str = Field(...)
    rental_duration: int

class TokenData(BaseModel):
    username: str

class LoginRequest(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
