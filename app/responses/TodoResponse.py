import strawberry


@strawberry.type
class TodoResponse:
    id: int
    label: str
