import strawberry


@strawberry.type
class ErrorResponse:
    message: str = "Something went wrong"
    code: str = "INTERNAL_SERVER_ERROR"
