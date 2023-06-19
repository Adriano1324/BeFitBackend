"""
This module contains resolver to login user
"""
from sqlalchemy import select

from app.db.async_session import get_session
from app.models import User as UserModel
from app.scalars import LoginError as LoginErrorScalar
from app.scalars import LoginSuccess as LoginSuccessScalar
from app.scalars import Token as TokenScalar
from app.scalars import User as UserScalar
from app.scalars import UserNotFound as UserNotFoundScalar
from app.security import create_access_token, verify_password
from app.utils.resolvers import get_valid_data


async def login_user(
    username: str, password: str
) -> LoginSuccessScalar | UserNotFoundScalar | LoginErrorScalar:
    """
    This function is responsible to log in user
    :param username: User username
    :param password: User password
    :return: one of LoginSuccessScalar | UserNotFoundScalar | LoginErrorScalar
        If LoginSuccessScalar User data and token are returned
        If UserNotFoundScalar Username is incorrect
        If LoginErrorScalar Password is incorrect
    """
    async with get_session() as s:
        select_new_user_sql = select(UserModel).filter(UserModel.username == username)
        db_user = (await s.execute(select_new_user_sql)).scalars().unique().first()
        await s.commit()

    if db_user is None:
        return UserNotFoundScalar()
    if not verify_password(
        plain_password=password, hashed_password=str(db_user.password_hash)
    ):
        return LoginErrorScalar()
    user_dict = get_valid_data(db_user, UserModel)
    del user_dict["password_hash"]
    token = create_access_token(user_dict)

    return LoginSuccessScalar(
        user=UserScalar(**user_dict),
        token=TokenScalar(access_token=token, token_type="Bearer"),
    )
