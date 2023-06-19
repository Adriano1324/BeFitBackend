"""
This module contains all fragments for user
"""
import strawberry

from app.scalars import ExpiredToken, MissingToken, User, UserExists

CreateUserResponse = strawberry.union("CreateUserResponse", (User, UserExists))
MeResponse = strawberry.union("MeResponse", (User, MissingToken, ExpiredToken))
