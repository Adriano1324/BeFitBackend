import strawberry


@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        return Book(title=title, author=author)
