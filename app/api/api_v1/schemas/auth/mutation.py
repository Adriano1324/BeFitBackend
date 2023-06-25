"""
This module contains mutations for auth
"""
import strawberry

from app.fragments import LoginResult
from app.resolvers import login_user


@strawberry.type
class Mutation:  # pylint: disable=too-few-public-methods
    """
    This is mutations class used to store all mutations for users
    """

    @strawberry.field
    async def login(self, username: str, password: str) -> LoginResult:
        """
        :param username: is user username
        :param password: is user password
        :return: one of following types LoginSuccessScalar | UserNotFoundScalar | LoginErrorScalar
            If LoginSuccessScalar User and token are returned
            If UserNotFoundScalar User with provided username didn't exist
            If LoginErrorScalar Password is wrong or something other went wrong
        """
        user = await login_user(username=username, password=password)
        return user
