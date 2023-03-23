import strawberry


@strawberry.type
class TodoNotFound:
    id: int
    message: str
