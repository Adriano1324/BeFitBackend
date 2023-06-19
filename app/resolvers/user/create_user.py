"""
This module contains resolver for creating user
"""
from sqlalchemy import insert, select

from app.db.async_session import get_session
from app.inputs import UserCreate as UserCreateInput
from app.models import User as UserModel
from app.scalars import User as UserScalar
from app.scalars import UserExists as UserExistsScalar
from app.security import get_password_hash
from app.utils.resolvers import get_valid_data


async def add_user(user_in: UserCreateInput) -> UserScalar | UserExistsScalar:
    """
    This function is to create user in db
    :param user_in: UserInput
    :return: one of UserScalar | UserExistsScalar
        If UserScalar means that user was correctly created
        If UserExistsScalar User with this username already exists
    """
    async with get_session() as s:
        select_existing_user_sql = select(UserModel.username).filter(
            UserModel.username == user_in.username
        )
        existing_db_user = (await s.execute(select_existing_user_sql)).first()
        if existing_db_user is not None:
            return UserExistsScalar()
        insert_user_query = insert(UserModel).values(
            username=user_in.username,
            description=user_in.description,
            avatar_img=user_in.avatar_img,
            is_active=True,
            is_public=user_in.is_public,
            password_hash=get_password_hash(user_in.password),
        )
        await s.execute(insert_user_query)

        select_new_user_sql = select(UserModel).filter(
            UserModel.username == user_in.username
        )

        db_user = (await s.execute(select_new_user_sql)).scalars().unique().one()
        await s.commit()

    user_dict = get_valid_data(db_user, UserModel)
    del user_dict["password_hash"]
    return UserScalar(**user_dict)
