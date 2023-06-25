"""
This module contains queries for user
"""
import strawberry

from app.fragments import MeResponse
from app.security import Info


@strawberry.type
class Query:  # pylint: disable=too-few-public-methods
    """
    This is Query class used to store all query for users
    """

    @strawberry.field
    async def current_user(self, info: Info) -> MeResponse:
        """
        :param info: This object store information about selected fields and actual user
        :return: one of following types UserScalar | MissingTokenScalar | ExpiredTokenScalar
            If UserScalar is returned this mean that token is correct and user data are returned
            If MissingTokenScalar This means issue with token and user should log in again
            If ExpiredTokenScalar This means token is expired and user should log in again
        """
        return info.context.user
