import strawberry


@strawberry.type
class TodoDuplication:
    label: str
    message: str
