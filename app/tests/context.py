"""
This module contains context to store authenticated user data
"""
from functools import cached_property

from strawberry.fastapi import BaseContext

from app.scalars import ExpiredToken as ExpiredTokenScalar
from app.scalars import MissingToken as MissingTokenScalar
from app.scalars import User as UserScalar
from app.security.authentication import get_current_user


class Context(BaseContext):  # pylint: disable=too-few-public-methods
    """
    This is context for app
    """

    def __init__(self, token: str):
        super().__init__()
        self.token = token

    @cached_property
    def user(self) -> UserScalar | MissingTokenScalar | ExpiredTokenScalar:
        """
        :return: Based on authentication header one of following types is returned
            If UserScalar Token was correct and user is returned
            If MissingTokenScalar Token was not provided
            If ExpiredTokenScalar Token is expired
        """
        if not self.token:
            return MissingTokenScalar()

        authorization = self.token
        if authorization is None:
            return MissingTokenScalar()
        return get_current_user(authorization)
