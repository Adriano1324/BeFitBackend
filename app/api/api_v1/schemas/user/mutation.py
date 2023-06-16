import strawberry

from app.fragments import CreateUserResponse
from app.inputs import UserCreate
from app.resolvers import add_user
from app.scalars import User, UserExists
from app.security import Info


@strawberry.type
class Mutation:
    @strawberry.mutation
    async def create_user(self, info: Info, user_obj: UserCreate) -> CreateUserResponse:
        user: User | UserExists = await add_user(info=info, user_in=user_obj)
        return user
