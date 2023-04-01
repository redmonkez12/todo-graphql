import strawberry


@strawberry.type
class EmptyResponse:
    message: str
