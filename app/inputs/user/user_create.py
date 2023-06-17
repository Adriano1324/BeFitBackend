import strawberry


@strawberry.input
class UserCreate:
    username: str
    description: str | None
    avatar_img: str
    is_public: bool
    password: str
