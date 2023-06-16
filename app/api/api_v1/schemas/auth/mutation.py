import strawberry

from app.fragments import LoginResult
from app.resolvers import login_user


@strawberry.type
class Mutation:
    @strawberry.field
    async def login(self, username: str, password: str) -> LoginResult:
        # Your domain-specific authentication logic would go here
        user = await login_user(username=username, password=password)
        return user
