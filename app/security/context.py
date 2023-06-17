from functools import cached_property
from typing import TypeAlias

from strawberry.fastapi import BaseContext
from strawberry.types import Info as _Info
from strawberry.types.info import RootValueType

from app.scalars import ExpiredToken as ExpiredTokenScalar
from app.scalars import MissingToken as MissingTokenScalar
from app.scalars import User as UserScalar
from app.security import get_current_user


class Context(BaseContext):
    @cached_property
    def user(self) -> UserScalar | MissingTokenScalar | ExpiredTokenScalar:
        if not self.request:
            return MissingTokenScalar()

        authorization = self.request.headers.get("Authorization", None)
        if authorization is None:
            return MissingTokenScalar()
        return get_current_user(authorization)


Info: TypeAlias = _Info[Context, RootValueType]
