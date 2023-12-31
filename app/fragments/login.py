"""
This module contains all fragments for login
"""
import strawberry

from app.scalars import LoginError, LoginSuccess, UserNotFound

LoginResult = strawberry.union("LoginResult", (LoginSuccess, LoginError, UserNotFound))
