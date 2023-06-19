"""
This module contains scalars for user
"""
import strawberry


@strawberry.type
class User:
    """
    This class contains data for user
    """

    id: int
    username: str
    description: str | None
    avatar_img: str
    is_active: bool
    is_public: bool


@strawberry.type
class UserExists:
    """
    This class contains data for user error during creating user
    """

    msg: str = "User with this name already exists"


@strawberry.type
class UserNotFound:
    """
    This class contains data for user error when user was not found
    """

    msg: str = "User with this name didn't exist"
