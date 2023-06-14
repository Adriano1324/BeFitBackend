"""
This module is responsible for registering all routers
"""
import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig

from .schemas.user.mutation import Mutation as UserMutation
from .schemas.user.query import Query as UserQuery


@strawberry.type
class Query(UserQuery):
    """
    This is base query class which inherits from all modules
    """


@strawberry.type
class Mutation(UserMutation):
    """
    This is base mutation class which inherits from all modules
    """


schema = strawberry.Schema(
    query=Query, mutation=Mutation, config=StrawberryConfig(auto_camel_case=True)
)

graph_ql_router_v1: GraphQLRouter = GraphQLRouter(schema)
