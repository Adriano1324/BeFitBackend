import strawberry

from app.scalars.auth.token import Token
from app.scalars.user.user import User


@strawberry.type
class LoginSuccess:
    user: User
    token: Token


@strawberry.type
class LoginError:
    message: str = "Wrong password"
