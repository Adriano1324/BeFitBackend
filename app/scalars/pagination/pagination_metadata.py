"""
This module contains scalars for pagination
"""
import strawberry


@strawberry.type
class PaginationMetadata:
    """
    This class contains data for pagination
    """

    total: int
    page: int
    size: int
    pages: int
