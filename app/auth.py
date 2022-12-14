#Python
import uuid
from jose import jwt
from pydantic.networks import EmailStr
from passlib.context import CryptContext
from datetime import datetime, timedelta

#FastAPI
from fastapi.security import OAuth2PasswordBearer

#App
from app.settings import TokensConfig


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login/")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)


