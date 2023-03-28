import strawberry
from strawberry.types import Info

from app.auth.token import create_access_token
from app.errors.ErrorResponse import ErrorResponse
from app.request.LoginRequest import LoginRequest
from app.request.UserCreateRequest import CreateUserRequest
from app.responses.UserLoginResponse import LoginResultResponse, UserLoginResponse
from app.services.UserService import UserService, CreateUserModel


@strawberry.type
class UserMutation:

    @strawberry.mutation
    async def create_user(self, info: Info, data: CreateUserRequest) -> CreateUserModel:
        user_service: UserService = info.context["user_service"]

        new_user = await user_service.create_user(data)
        return new_user

    @strawberry.mutation
    async def login_user(self, info: Info, data: LoginRequest) -> LoginResultResponse:
        try:
            user_service: UserService = info.context["user_service"]

            user = await user_service.login(data)

            access_token = create_access_token(
                data={"sub": user.username}
            )

            return UserLoginResponse(access_token=access_token, token_type="bearer")
        except Exception as e:
            print(e)
            return ErrorResponse(message="something went wrong", code="ERROR")
