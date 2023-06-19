"""
This module contains context to store authenticated user data
"""
from functools import cached_property
from typing import TypeAlias

from strawberry.fastapi import BaseContext
from strawberry.types import Info as _Info
from strawberry.types.info import RootValueType

from app.scalars import ExpiredToken as ExpiredTokenScalar
from app.scalars import MissingToken as MissingTokenScalar
from app.scalars import User as UserScalar

from .authentication import get_current_user


class Context(BaseContext):  # pylint: disable=too-few-public-methods
    """
    This is context for app
    """

    @cached_property
    def user(self) -> UserScalar | MissingTokenScalar | ExpiredTokenScalar:
        """
        :return: Based on authentication header one of following types is returned
            If UserScalar Token was correct and user is returned
            If MissingTokenScalar Token was not provided
            If ExpiredTokenScalar Token is expired
        """
        if not self.request:
            return MissingTokenScalar()

        authorization = self.request.headers.get("Authorization", None)
        if authorization is None:
            return MissingTokenScalar()
        return get_current_user(authorization)


Info: TypeAlias = _Info[Context, RootValueType]
