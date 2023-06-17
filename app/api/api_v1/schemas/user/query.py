"""
This module contains queries for user
"""
import strawberry

from app.fragments import MeResponse
from app.security import Info


@strawberry.type
class Query:
    @strawberry.field
    async def me(self, info: Info) -> MeResponse:
        """
        This method returns actual user from context
        """
        return info.context.user
