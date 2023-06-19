"""
This module contains all functions to authenticate user
"""
from datetime import datetime, timedelta

from jose import ExpiredSignatureError, JWTError, jwt
from passlib.context import CryptContext

from app.core.config import settings
from app.scalars import ExpiredToken as ExpiredTokenScalar
from app.scalars import User as UserScalar

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    :param plain_password: Password provided by user
    :param hashed_password: Password hash from db
    :return: true if provided password match to password hash
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    :param password: Provided password
    :return: Generated password hash
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    :param data: Dict of data which should be stored in token
    :param expires_delta: Timedelta how long token should be valid
    :return: JWT token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def get_current_user(token: str) -> UserScalar | ExpiredTokenScalar:
    """
    :param token: Token to decode
    :return: One of following types UserScalar | ExpiredTokenScalar
        If UserScalar then token is valid
        If ExpiredTokenScalar then user should log in again because of expired token
    """
    try:
        payload: dict = jwt.decode(
            token.replace("Bearer ", ""),
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
        del payload["exp"]
        return UserScalar(**payload)
    except ExpiredSignatureError:
        return ExpiredTokenScalar()
    except JWTError:  # we want separately catch errors other than expired token
        return ExpiredTokenScalar()
