"""
This Module contains settings class which store configuration for app
"""
from typing import Any, Dict, List

from pydantic import PostgresDsn  # pylint: disable=no-name-in-module
from pydantic import BaseSettings, validator


class Settings(BaseSettings):  # pylint: disable=too-few-public-methods
    """
    This class inherits from BaseSettings and store all settings for app
    """

    # SECRET_KEY: str = secrets.token_urlsafe(32)
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    ALGORITHM: str = "HS256"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    PROJECT_NAME: str = "BeFit"

    POSTGRES_SERVER: str = ""
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = ""
    SQLALCHEMY_DATABASE_URI: PostgresDsn | None = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(  # pylint: disable=no-self-argument
        cls,
        value: str | None,
        values: Dict[str, Any],  # pylint: disable=no-self-argument
    ) -> Any:
        """
        :param value: Is string value for  SQLALCHEMY_DATABASE_URI
        :param values: Store all settings for app in dict
        :return: If SQLALCHEMY_DATABASE_URI is configured then is returned
            if didn't build db url from other parameters
        """
        if isinstance(value, str):
            return value
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:  # pylint: disable=too-few-public-methods
        """
        This class store configuration for Settings
        """

        case_sensitive = True


settings = Settings()
