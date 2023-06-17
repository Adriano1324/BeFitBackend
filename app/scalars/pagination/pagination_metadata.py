import strawberry


@strawberry.type
class PaginationMetadata:
    total: int
    page: int
    size: int
    pages: int
