import pytest
from faker import Faker

from app.api.api_v1.api import schema
from app.tests.context import Context
from app.tests.queries.create_user import CREATE_USER_MUTATION
from app.tests.queries.current_user import CURRENT_USER_QUERY
from app.tests.queries.login import LOGIN

fake = Faker()


@pytest.mark.asyncio
async def test_current_user() -> None:
    username = fake.name()
    result = await schema.execute(
        CREATE_USER_MUTATION,
        variable_values={
            "avatarImg": fake.image_url(),
            "description": fake.sentence(),
            "isPublic": True,
            "password": "Password",
            "username": username,
        },
    )
    assert result.data.get("createUser", {}).get("username") == username
    login_result = await schema.execute(
        LOGIN,
        variable_values={
            "username": username,
            "password": "Password",
        },
    )
    assert login_result.data.get("login", {}).get("__typename") == "LoginSuccess"
    token = login_result.data.get("login", {}).get("token", {}).get("accessToken", None)
    current_user_result = await schema.execute(
        CURRENT_USER_QUERY, context_value=Context(token=f"Bearer {token}")
    )
    assert (
        current_user_result.data.get("currentUser", {}).get("username", "") == username
    )
