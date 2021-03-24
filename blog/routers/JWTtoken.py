from typing import Optional
from datetime import datetime, timedelta
from jose import JWTError, jwt


# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/?h=jwt#about-jwt
# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "592e37c9a1c4027c08044ddc3b657e584e3e72460b0ccf43bf518e417760b047"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt