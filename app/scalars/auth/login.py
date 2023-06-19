"""
This module contains scalars for login
"""
import strawberry

from app.scalars.auth.token import Token
from app.scalars.user.user import User


@strawberry.type
class LoginSuccess:
    """
    This class contains data returned after successful logging in
    """

    user: User
    token: Token


@strawberry.type
class LoginError:
    """
    This class contains data returned after issue with logging in
    """

    msg: str = "Wrong password"
