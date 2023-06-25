"""
This module contains scalars for token
"""
import strawberry


@strawberry.type
class Token:
    """
    This class contains data for token
    """

    access_token: str
    token_type: str


@strawberry.type
class ExpiredToken:
    """
    This class contains data for expired token
    """

    msg: str = "Token is expired, please login again"


@strawberry.type
class MissingToken:
    """
    This class contains data for missing token
    """

    msg: str = "Token is missing, please login"
