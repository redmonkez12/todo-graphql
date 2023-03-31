import strawberry

from app.errors.ErrorResponse import ErrorResponse


@strawberry.type
class EmptyResponse:
    xxx: str


ChangePasswordResponse = strawberry.union(
    "ChangePasswordResponse", [EmptyResponse, ErrorResponse],
)
