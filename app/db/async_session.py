"""
This module contains definition async session
"""
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from app.core.config import settings

engine: AsyncEngine = create_async_engine(
    str(settings.SQLALCHEMY_DATABASE_URI), poolclass=NullPool
)
async_session = sessionmaker(  # type: ignore
    engine,
    autoflush=False,
    expire_on_commit=False,
    autocommit=False,
    class_=AsyncSession,
)


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    This is context manager for connection with database
    """
    async with async_session() as session:
        async with session.begin():
            try:
                yield session
            finally:
                await session.close()
