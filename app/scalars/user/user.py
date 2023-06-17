import strawberry


@strawberry.type
class User:
    id: int
    username: str
    description: str | None
    avatar_img: str
    is_active: bool
    is_public: bool


@strawberry.type
class UserExists:
    msg: str = "User with this name already exists"


@strawberry.type
class UserNotFound:
    msg: str = "User with this name didn't exist"
