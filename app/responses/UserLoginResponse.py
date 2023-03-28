import strawberry

from app.errors.ErrorResponse import ErrorResponse


@strawberry.type
class UserLoginResponse:
    access_token: str
    token_type: str


LoginResultResponse = strawberry.union("LoginResultResponse", [UserLoginResponse, ErrorResponse])