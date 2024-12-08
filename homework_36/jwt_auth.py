import datetime

from jose import jwt
from fastapi import HTTPException, status
from jose.exceptions import ExpiredSignatureError, JWTError

from config import Config


config = Config()
ALGORITHM = "HS256"
EXPIRES_IN = 5

def create_jwt_token(user: dict):
    expires = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=EXPIRES_IN)
    data = user.copy()
    data["exp"] = expires
    auth_token = jwt.encode(data, config.SECRET_KEY, algorithm=ALGORITHM)
    return auth_token

def verify_jwt_token(token):
    try:
        username = jwt.decode(token, config.SECRET_KEY, algorithms=ALGORITHM)
        return username.get("sub")
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")