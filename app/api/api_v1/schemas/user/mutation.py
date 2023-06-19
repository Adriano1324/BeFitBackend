"""
This module contains mutations for users
"""
import strawberry

from app.fragments import CreateUserResponse
from app.inputs import UserCreate
from app.resolvers import add_user
from app.scalars import User, UserExists


@strawberry.type
class Mutation:  # pylint: disable=too-few-public-methods
    """
    This is mutations class used to store all mutations for users
    """

    @strawberry.mutation
    async def create_user(self, user_obj: UserCreate) -> CreateUserResponse:
        """
        :param user_obj: This object store information about new user
        :return: one of following types User | UserExists
            If User is returned this means that new user was correctly created
            If UserExists is returned this means that user with this username already exists
        """
        user: User | UserExists = await add_user(user_in=user_obj)
        return user
