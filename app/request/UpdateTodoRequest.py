import strawberry


@strawberry.input
class UpdateTodoRequest:
    id: int
    label: str
