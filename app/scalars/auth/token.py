import strawberry


@strawberry.type
class Token:
    access_token: str
    token_type: str


@strawberry.type
class ExpiredToken:
    msg: str = "Token is expired, please login again"


@strawberry.type
class MissingToken:
    msg: str = "Token is missing, please login"
