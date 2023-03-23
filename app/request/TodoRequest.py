import strawberry


@strawberry.type
class TodoRequest:
    label: str
