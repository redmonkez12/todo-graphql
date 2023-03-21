import strawberry


@strawberry.type
class TodoResponse:
    todo_id: int
    label: str
