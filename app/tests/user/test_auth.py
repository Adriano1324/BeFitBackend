import pytest
from faker import Faker

from app.api.api_v1.api import schema
from app.tests.queries.create_user import CREATE_USER_MUTATION
from app.tests.queries.login import LOGIN

fake = Faker()


@pytest.mark.asyncio
async def test_login_user() -> None:
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
    assert isinstance(
        login_result.data.get("login", {}).get("user").get("username", None), str
    )


@pytest.mark.asyncio
async def test_login_user_bad_username() -> None:
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
            "username": f"{username}_bad",
            "password": "Password",
        },
    )
    assert login_result.data.get("login", {}).get("__typename") == "UserNotFound"
    assert (
        login_result.data.get("login", {}).get("msg")
        == "User with this name didn't exist"
    )


@pytest.mark.asyncio
async def test_login_user_bad_password() -> None:
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
            "password": "Password_bad",
        },
    )
    print(login_result)
    assert login_result.data.get("login", {}).get("__typename") == "LoginError"
    assert login_result.data.get("login", {}).get("msg") == "Wrong password"
