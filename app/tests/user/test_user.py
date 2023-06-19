import pytest
from faker import Faker

from app.api.api_v1.api import schema
from app.tests.queries.create_user import CREATE_USER_MUTATION

fake = Faker()


@pytest.mark.asyncio
async def test_create_user() -> None:
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
    assert result.data.get("createUser", {}).get("username") == username  # type: ignore


@pytest.mark.asyncio
async def test_create_user_with_existing_username() -> None:
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
    assert result.data.get("createUser", {}).get("username") == username  # type: ignore
    result_2 = await schema.execute(
        CREATE_USER_MUTATION,
        variable_values={
            "avatarImg": fake.image_url(),
            "description": fake.sentence(),
            "isPublic": True,
            "password": "Password",
            "username": username,
        },
    )
    assert (
        result_2.data.get("createUser", {}).get("__typename") == "UserExists"  # type: ignore
    )
    assert (
        result_2.data.get("createUser", {}).get("msg")  # type: ignore
        == "User with this name already exists"
    )
