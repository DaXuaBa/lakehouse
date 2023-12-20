from datetime import datetime, timedelta
from typing import Optional
from jose import jwt
from jose.exceptions import JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi.param_functions import Depends
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from backend.db.database import get_db
from backend.db.db_user import *

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY_ACCESS = 'fba012a2a0c9c3d884fdf15843f2aa438bac1b5e8527875ecd7187e3ce494158'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 5
REFRESS_TOKEN_EXPIRE_MINUTES = 30000

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({'iat': datetime.utcnow(), 'exp': expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY_ACCESS, algorithm=ALGORITHM)
  return encoded_jwt

def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(REFRESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({'iat': datetime.utcnow(), 'exp': expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY_ACCESS, algorithm=ALGORITHM)
  return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY_ACCESS, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user = get_user_by_username(username, db)

    if user is None:
        raise credentials_exception
    return user