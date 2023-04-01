import strawberry

from app.errors.ErrorResponse import ErrorResponse


@strawberry.type
class ChangePasswordResponse:
    message: str


ChangeResultResponse = strawberry.union(
    "ChangeResultResponse", (ChangePasswordResponse, ErrorResponse),
)
